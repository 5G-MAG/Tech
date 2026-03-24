import os, requests
from datetime import datetime

TOKEN = os.getenv('PROJECT_ACCESS_TOKEN')
ORG = "5G-MAG"

# ADD ALL 10 PROJECTS HERE
PROJECT_MAP = {
    44: {"title": "Reference Tools", "filename": "roadmap-tools.md"},
    # 45: {"title": "Project Name", "filename": "roadmap-name.md"},
    # ... continue until you have all 10
}

def fetch_data(num):
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
    headers = {"Authorization": f"bearer {TOKEN}"}
    resp = requests.post('https://api.github.com/graphql', json={'query': query, 'variables': {"org": ORG, "num": num}}, headers=headers)
    return resp.json()

def run():
    for num, info in PROJECT_MAP.items():
        data = fetch_data(num)
        nodes = data.get('data', {}).get('organization', {}).get('projectV2', {}).get('items', {}).get('nodes', [])
        
        # Group by Status
        cols = ["💡 Pitch", "📅 To Do", "🏗️ In Progress", "👀 In Review", "✅ Done"]
        board = {c: [] for c in cols}
        for n in nodes:
            content = n.get('content')
            if not content: continue
            status = (n.get('fieldValueByName') or {}).get('name', "📅 To Do")
            if status in board:
                board[status].append(f"- **{content['repository']['name']}**: [{content['title']}]({content['url']})")

        # Write the File
        with open(f"docs/{info['filename']}", "w", encoding="utf-8") as f:
            f.write(f"---\nlayout: default\ntitle: {info['title']}\nparent: Roadmaps\n---\n\n")
            f.write(f"# {info['title']} Board\n*Synced: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n")
            for c in cols:
                if board[c]:
                    f.write(f"## {c}\n" + "\n".join(board[c]) + "\n\n")

if __name__ == "__main__":
    run()
