import os, requests, re
from datetime import datetime

# 1. Configuration
TOKEN = os.getenv('PROJECT_ACCESS_TOKEN')
ORG = "5G-MAG"

# 2. Add all 10 project IDs here
PROJECT_MAP = {
    44: "pages/5gbroadcast.md", 
    # Add others as you go: 45: "pages/another-project.md",
}

def fetch_project_data(num):
    url = 'https://api.github.com/graphql'
    headers = {"Authorization": f"bearer {TOKEN}"}
    query = """
    query($org: String!, $num: Int!) {
      organization(login: $org) {
        projectV2(number: $num) {
          items(first: 100) {
            nodes {
              content {
                ... on Issue { title, url, repository { name } }
                ... on PullRequest { title, url, repository { name } }
              }
              fieldValueByName(name: "Status") {
                ... on ProjectV2ItemFieldSingleSelectValue { name }
              }
            }
          }
        }
      }
    }
    """
    vars = {"org": ORG, "num": num}
    resp = requests.post(url, json={'query': query, 'variables': vars}, headers=headers)
    return resp.json()

def generate_markdown(data):
    nodes = data.get('data', {}).get('organization', {}).get('projectV2', {}).get('items', {}).get('nodes', [])
    
    # YOUR EXACT PHASES
    phases = ["Candidate", "Under Study", "Work in Progress", "Completed", "Not pursued"]
    board = {p: [] for p in phases}
    
    for n in nodes:
        content = n.get('content')
        if not content: continue
        
        status_info = n.get('fieldValueByName')
        status = status_info['name'] if status_info else "Candidate"
        
        if status in board:
            repo = content.get('repository', {}).get('name', 'General')
            board[status].append(f"- **{repo}**: [{content['title']}]({content['url']})")

    # This creates the clean layout for your page
    output = "\n---\n\n## Live Development Status\n"
    output += f"*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')} UTC*\n\n"
    
    for p in phases:
        if board[p]:
            output += f"### {p}\n" + "\n".join(board[p]) + "\n\n"
    
    return output

def update_file(path, new_content):
    if not os.path.exists(path):
        print(f"❌ File not found: {path}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        file_text = f.read()

    # We search for the marker OR the previous update's header to overwrite it
    # This ensures the "HERE_IS_THE_KANBAN_BOARD" gets replaced once, 
    # and then the script keeps updating that same spot.
    start_m = ""
    end_m = ""
    marker = "HERE_IS_THE_KANBAN_BOARD"

    if start_m in file_text:
        # If we already have the HTML markers, replace between them
        pattern = rf"{start_m}.*?{end_m}"
        replacement = f"{start_m}\n{new_content}\n{end_m}"
        updated_text = re.sub(pattern, replacement, file_text, flags=re.DOTALL)
    elif marker in file_text:
        # If it's the first time, replace the text marker with HTML markers + content
        replacement = f"{start_m}\n{new_content}\n{end_m}"
        updated_text = file_text.replace(marker, replacement)
    else:
        # Fallback: append to bottom
        updated_text = file_text + f"\n{start_m}\n{new_content}\n{end_m}"

    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated_text)

if __name__ == "__main__":
    for num, path in PROJECT_MAP.items():
        data = fetch_project_data(num)
        content = generate_markdown(data)
        update_file(path, content)
        print(f"🎉 Updated {path}")
