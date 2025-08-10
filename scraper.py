from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json

def clean_text(text):
    return ' '.join(text.strip().split())

def scrape_with_playwright(url, wait_time=10000, min_length=40):
    print(f"\n[🌍] Visiting: {url}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(wait_time)
        content = page.content()
        browser.close()

    print("\n[🔍] Extracting structured text from divs and headings...\n")
    soup = BeautifulSoup(content, "lxml")
    tags = soup.find_all(['h1', 'h2', 'h3', 'p', 'li', 'span', 'div'])

    structured_data = []
    current_section = {"section": "General", "content": []}
    seen = set()

    for tag in tags:
        text = clean_text(tag.get_text())
        if len(text) < min_length or text in seen:
            continue
        seen.add(text)

        if tag.name in ['h1', 'h2', 'h3']:
            if current_section["content"]:
                structured_data.append(current_section)
            current_section = {"section": text, "content": []}
        else:
            current_section["content"].append(text)

    if current_section["content"]:
        structured_data.append(current_section)

    return structured_data

if __name__ == "__main__":
    url = "https://flowcv.com/" #Change Link If Want.....
    structured_content = scrape_with_playwright(url)

    print("\n==============================")
    print("📦 Structured Sections Extracted:")
    print("==============================\n")

    for section in structured_content:
        print(f"📂 {section['section']}")
        for i, text in enumerate(section['content'], 1):
            print(f"   {i}. {text}")
        print()

    with open("structured_output.json", "w", encoding="utf-8") as f:
        json.dump(structured_content, f, ensure_ascii=False, indent=2)
