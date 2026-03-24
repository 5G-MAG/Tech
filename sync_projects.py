import os, requests, re
from datetime import datetime

TOKEN = os.getenv('PROJECT_ACCESS_TOKEN')
ORG = "5G-MAG"
PROJECT_MAP = {44: "pages/5gbroadcast.md"} 

def update_file(path, num):
    print(f"--- Processing {path} ---")
    
    if not os.path.exists(path):
        print(f"❌ ERROR: The file '{path}' does not exist in this location.")
        # Let's see what files ARE there
        print(f"DEBUG: Current directory contents: {os.listdir('.')}")
        if os.path.exists('pages'): print(f"DEBUG: 'pages' folder contents: {os.listdir('pages')}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        file_text = f.read()
    
    marker = "HERE_IS_THE_KANBAN_BOARD"
    
    if marker not in file_text:
        print(f"❌ ERROR: Could not find the marker '{marker}' inside the file.")
        print(f"DEBUG: First 50 characters of file: {file_text[:50]}")
        return

    print(f"✅ FOUND: Marker found in {path}. Fetching data from GitHub...")
    
    # (Data fetching logic here...)
    # For this test, let's just put a timestamp to prove it works
    new_content = f"\n\n### TEST UPDATE: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC\n\n"
    
    updated_text = file_text.replace(marker, new_content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated_text)
    print(f"🎉 SUCCESS: File updated in memory.")

if __name__ == "__main__":
    for num, path in PROJECT_MAP.items():
        update_file(path, num)
