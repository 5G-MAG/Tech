import os, requests, re
from datetime import datetime

# 1. Configuration
TOKEN = os.getenv('PROJECT_ACCESS_TOKEN')
ORG = "5G-MAG"
# IMPORTANT: Ensure 'pages/' matches your folder name exactly!
PROJECT_MAP = {
    44: "pages/5gbroadcast.md", 
}

def fetch_data(num):
    url = 'https://api.github.com/graphql'
    headers = {"Authorization": f"bearer {TOKEN}"}
    query = """query($org: String!, $num: Int!) {
      organization(login: $org) {
        projectV2(number: $num) {
          items(first: 100) {
            nodes {
              content { ... on Issue { title, url, repository { name } } }
              fieldValueByName(name: "Status") { ... on ProjectV2ItemFieldSingleSelectValue { name } }
            }
          }
        }
      }
    }"""
    resp = requests.post(url, json={'query': query, 'variables': {"org": ORG, "num": num}}, headers=headers)
    return resp.json()

def generate_markdown(data):
    nodes = data.get('data', {}).get('organization', {}).get('projectV2', {}).get('items', {}).get('nodes', [])
    phases = ["Candidate", "Under Study", "Work in Progress", "Completed", "Not pursued"]
    board = {p: [] for p in phases}
    
    for n in nodes:
        content = n.get('content')
        if not content: continue
        status = (n.get('fieldValueByName') or {}).get('name', "Candidate")
        if status in board:
            repo = content.get('repository', {}).get('name', 'General')
            board[status].append(f"- **{repo}**: [{content['title']}]({content['url']})")

    output = f"\n\n## Live Roadmap (Updated {datetime.now().strftime('%Y-%m-%d %H:%M')} UTC)\n"
    for p in phases:
        if board[p]:
            output += f"### {p}\n" + "\n".join(board[p]) + "\n\n"
    return output

def update_file(path, content):
    if not os.path.exists(path):
        print(f"❌ File not found: {path}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        file_text = f.read()

    marker = "HERE_IS_THE_KANBAN_BOARD"

    if marker in file_text:
        # Replace the marker with the board
        new_text = file_text.replace(marker, content)
        print(f"✅ Replaced marker in {path}")
    else:
        # If marker is missing, append to bottom so we see progress
        new_text = file_text + content
        print(f"⚠️ Marker not found in {path}, appended to bottom.")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_text)

if __name__ == "__main__":
    for num, path in PROJECT_MAP.items():
        data = fetch_data(num)
        board_md = generate_markdown(data)
        update_file(path, board_md)
