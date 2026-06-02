import os
import re

WORKSPACE_DIR = r"d:\new-globotech-website-main"
SRC_DIR = os.path.join(WORKSPACE_DIR, "src")

TARGET_FILES = [
    os.path.join(SRC_DIR, "Web-Dev", "web-development.html"),
    os.path.join(SRC_DIR, "Services", "services.html"),
    os.path.join(SRC_DIR, "mobile-app", "mobile-app.html"), # already clean but verify
]

def clean_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (does not exist)")
        return
        
    print(f"Cleaning {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove CSS stylesheet rules
    # Testimonials CSS
    t_start = content.find("/* ── TESTIMONIALS (dark contrast) ── */")
    if t_start != -1:
        next_comment_idx = content.find("/* ── ", t_start + 40)
        if next_comment_idx == -1:
            next_comment_idx = content.find("</style>", t_start + 40)
        if next_comment_idx != -1:
            print("  Removed testimonials CSS styles.")
            content = content[:t_start] + content[next_comment_idx:]

    # FAQ CSS
    faq_start = content.find("/* ── FAQ ── */")
    if faq_start != -1:
        next_comment_idx = content.find("/* ── ", faq_start + 15)
        if next_comment_idx == -1:
            next_comment_idx = content.find("</style>", faq_start + 15)
        if next_comment_idx != -1:
            print("  Removed FAQ CSS styles.")
            content = content[:faq_start] + content[next_comment_idx:]

    # 2. Remove HTML section markup
    # Testimonials section
    test_sec_start = content.find('<section class="testimonials">')
    if test_sec_start == -1:
        test_sec_start = content.find('<section class="testimonials')
    if test_sec_start != -1:
        test_sec_end = content.find('</section>', test_sec_start)
        if test_sec_end != -1:
            print("  Removed testimonials HTML markup.")
            content = content[:test_sec_start] + content[test_sec_end + 10:]

    # FAQ section
    faq_sec_start = content.find('<section class="faq">')
    if faq_sec_start == -1:
        faq_sec_start = content.find('<section class="faq')
    if faq_sec_start != -1:
        faq_sec_end = content.find('</section>', faq_sec_start)
        if faq_sec_end != -1:
            print("  Removed FAQ HTML markup.")
            content = content[:faq_sec_start] + content[faq_sec_end + 10:]

    # 3. Remove FAQ Toggling JS logic
    faq_js_start = content.find("function toggleFaq")
    if faq_js_start != -1:
        depth = 0
        idx = content.find("{", faq_js_start)
        if idx != -1:
            while idx < len(content):
                if content[idx] == '{':
                    depth += 1
                elif content[idx] == '}':
                    depth -= 1
                    if depth == 0:
                        print("  Removed toggleFaq JS code.")
                        content = content[:faq_js_start] + content[idx + 1:]
                        break
                idx += 1

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    for f in TARGET_FILES:
        clean_file(f)
    print("Cleanup process complete!")

if __name__ == "__main__":
    main()
