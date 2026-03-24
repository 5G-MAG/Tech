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
              content { ... on Issue { title, url } }
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
    
    # Updated phase order: Candidate first, Not Pursued last
    phases = ["Candidate", "Under Study", "Work in Progress", "Completed", "Not pursued"]
    board = {p: [] for p in phases}
    
    for n in nodes:
        content = n.get('content')
        if not content: continue
        status = (n.get('fieldValueByName') or {}).get('name', "Candidate")
        
        if status in board:
            # Style adjustment: 'Not pursued' items get a lighter, strike-through look
            is_ignored = status == "Not pursued"
            bg_color = "#f6f8fa" if is_ignored else "#ffffff"
            text_decor = "line-through" if is_ignored else "none"
            opacity = "0.6" if is_ignored else "1.0"

            card = f"""
    <div style="margin-bottom: 12px; padding: 15px; border: 1px solid #d1d5da; border-radius: 8px; background-color: {bg_color}; box-shadow: 0 1px 3px rgba(0,0,0,0.05); opacity: {opacity};">
        <a href="{content['url']}" style="text-decoration: {text_decor}; color: #0366d6; font-size: 15px; font-weight: 600; display: block;">
            {content['title']}
        </a>
    </div>"""
            board[status].append(card)

    output = f"\n\n<div id='kanban-display' style='font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Helvetica, Arial, sans-serif;'>\n"
    output += f"## Live Development Status\n"
    output += f"<p style='font-size: 12px; color: #586069; margin-bottom: 20px;'>Last Sync: {datetime.now().strftime('%Y-%m-%d %H:%M')} UTC</p>\n"
    
    for p in phases:
        if board[p]:
            output += f"\n<h3 style='border-bottom: 1px solid #eaecef; padding-bottom: 8px; margin-top: 30px; color: #24292e;'>{p}</h3>\n"
            output += "".join(board[p])
            
    output += "\n</div>\n\n"
    return output

def update_file(path, num):
    if not os.path.exists(path): return
    
    with open(path, 'r', encoding='utf-8') as f:
        file_text = f.read()

    start_m = "<!-- KANBAN_START -->"
    end_m = "<!-- KANBAN_END -->"

    if start_m not in file_text:
        print(f"❌ ERROR: Markers missing in {path}.")
        return

    data = fetch_data(num)
    new_board_content = generate_markdown(data)
    
    pattern = rf"{start_m}.*?{end_m}"
    replacement = f"{start_m}{new_board_content}{end_m}"
    updated_text = re.sub(pattern, replacement, file_text, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated_text)
    print(f"✅ Full board sync successful for {path}")

if __name__ == "__main__":
    for num, path in PROJECT_MAP.items():
        update_file(path, num)
