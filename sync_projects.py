import os, requests, re
from datetime import datetime

# 1. Configuration
TOKEN = os.getenv('PROJECT_ACCESS_TOKEN')
ORG = "5G-MAG"

# 2. Add all 10 project IDs and their corresponding file paths here
PROJECT_MAP = {
    44: "pages/5g-broadcast.md", 
    # Example: 45: "docs/another-page.md",
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

    output = "\n---\n\n## Live Development Status\n"
    output += f"*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')} UTC*\n\n"
    for p in phases:
        if board[p]:
            output += f"### {p}\n" + "\n".join(board[p]) + "\n\n"
    return output

def update_file(path, new_content):
    if not os.path.exists(path):
        print(f"Skipping {path}: File not found.")
        return
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # The markers the script looks for
    start_marker = ""
    end_marker = ""

    if start_marker not in text:
        print(f"Skipping {path}: Markers not found.")
        return

    pattern = rf"{start_marker}.*?{end_marker}"
    replacement = f"{start_marker}\n{new_content}\n{end_marker}"
    updated_text = re.sub(pattern, replacement, text, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated_text)
    print(f"Successfully updated {path}")

if __name__ == "__main__":
    for num, path in PROJECT_MAP.items():
        data = fetch_project_data(num)
        update_file(path, generate_markdown(data))
