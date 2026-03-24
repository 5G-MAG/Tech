import os, requests, re
from datetime import datetime

# 1. Config
TOKEN = os.getenv('PROJECT_ACCESS_TOKEN')
ORG = "5G-MAG"

# 2. UPDATED PATH: Ensure this matches your repo folder structure
PROJECT_MAP = {
    44: "pages/5gbroadcast.md", 
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
        # Default to "Candidate" if no status is set
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
        print(f"❌ ERROR: File not found at: {path}. Check your folder names!")
        return

    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Flexible search for the HTML markers
    start_m = ""
    end_m = ""

    if start_m not in text:
        print(f"⚠️ WARNING: Could not find '{start_m}' in {path}")
        return

    pattern = rf"{start_m}.*?{end_m}"
    replacement = f"{start_m}\n{new_content}\n{end_m}"
    updated_text = re.sub(pattern, replacement, text, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated_text)
    print(f"✅ SUCCESS: Updated {path}")

if __name__ == "__main__":
    if not TOKEN:
        print("❌ ERROR: PROJECT_ACCESS_TOKEN secret is missing in GitHub Settings.")
    else:
        for num, path in PROJECT_MAP.items():
            print(f"Processing Project #{num}...")
            data = fetch_project_data(num)
            content = generate_markdown(data)
            update_file(path, content)
