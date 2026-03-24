import os, requests, re
from datetime import datetime

TOKEN = os.getenv('PROJECT_ACCESS_TOKEN')
ORG = "5G-MAG"
PROJECT_MAP = {44: "pages/5gbroadcast.md"}

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

    output = f"\n\n## Live Development Status\n*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')} UTC*\n\n"
    for p in phases:
        if board[p]:
            output += f"### {p}\n" + "\n".join(board[p]) + "\n\n"
    return output

def update_file(path, num):
    if not os.path.exists(path): return
    
    with open(path, 'r', encoding='utf-8') as f:
        file_text = f.read()

    # The STRICT Markers
    start_m = ""
    end_m = ""

    if start_m not in file_text:
        print(f"❌ ERROR: Markers missing in {path}. Please add them manually.")
        return

    data = fetch_data(num)
    new_board_content = generate_markdown(data)
    
    # regex replaces EVERYTHING between the markers
    pattern = rf"{start_m}.*?{end_m}"
    replacement = f"{start_m}{new_board_content}{end_m}"
    updated_text = re.sub(pattern, replacement, file_text, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated_text)
    print(f"✅ Clean update for {path}")

if __name__ == "__main__":
    for num, path in PROJECT_MAP.items():
        update_file(path, num)
