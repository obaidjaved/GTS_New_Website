import os
import re

# File paths
WORKSPACE_DIR = r"d:\new-globotech-website-main"
SRC_DIR = os.path.join(WORKSPACE_DIR, "src")

# The 10 HTML files that need header and footer unification
PAGES = [
    ("Home", "homepage.html"),
    ("Web-Dev", "web-development.html"),
    ("About", "aboutus.html"),
    ("Blog", "blog.html"),
    ("Contact", "contact.html"),
    ("Services", "services.html"),
    ("ai-solutions", "ai-solutions.html"),
    ("digital-marketing", "digital-marketing.html"),
    ("e-commerce-solutions", "e-commerce-solutions.html"),
    ("mobile-app", "mobile-app.html"),
]

# Source of truth page
SOURCE_PAGE_PATH = os.path.join(SRC_DIR, "Web-Dev", "web-development.html")

def find_nav_css_block(content):
    start_idx = content.find("/* ── NAV ── */")
    if start_idx == -1:
        return None
    
    curr_idx = start_idx + 15
    while True:
        next_comment_idx = content.find("/* ── ", curr_idx)
        if next_comment_idx == -1:
            end_style_idx = content.find("</style>", curr_idx)
            return (start_idx, end_style_idx)
        
        comment_text = content[next_comment_idx:next_comment_idx+40]
        if "SIDE DRAWER" in comment_text:
            curr_idx = next_comment_idx + 10
            continue
        else:
            return (start_idx, next_comment_idx)

def find_footer_css_block(content):
    start_idx = content.find("/* ── FOOTER (dark premium) ── */")
    if start_idx == -1:
        start_idx = content.find("/* ── FOOTER ── */")
    if start_idx == -1:
        return None
    
    curr_idx = start_idx + 15
    next_comment_idx = content.find("/*", curr_idx)
    end_style_idx = content.find("</style>", curr_idx)
    
    candidates = []
    if next_comment_idx != -1:
        candidates.append(next_comment_idx)
    if end_style_idx != -1:
        candidates.append(end_style_idx)
        
    if not candidates:
        return None
    return (start_idx, min(candidates))

def extract_nav_html_block(content):
    start_idx = content.find('<div class="nav-wrap">')
    if start_idx == -1:
        start_idx = content.find('<div class="nav-wrap"')
    if start_idx == -1:
        return None
    
    idx = start_idx
    depth = 0
    while idx < len(content):
        if content[idx:idx+4] == '<div':
            depth += 1
            idx += 4
        elif content[idx:idx+5] == '</div':
            depth -= 1
            idx += 5
            if depth == 0:
                end_idx = content.find('>', idx)
                if end_idx != -1:
                    return (start_idx, end_idx + 1)
        else:
            idx += 1
    return None

def extract_footer_html_block(content):
    start_idx = content.find('<footer')
    if start_idx == -1:
        return None
    end_tag = '</footer>'
    end_idx = content.find(end_tag, start_idx)
    if end_idx == -1:
        return None
    return (start_idx, end_idx + len(end_tag))

def find_nav_js_block(content):
    # Find all possible start markers
    starts = []
    for marker in [
        "// ── Mega Menu ──",
        "// ── Mega Menu — PATCHED",
        "// ── Hamburger nav toggle ──",
        "const ham = document.querySelector('.nav-hamburger');",
        "const ham = document.querySelector(\".nav-hamburger\");",
        "document.getElementById('nav-services-trigger')"
    ]:
        idx = content.find(marker)
        if idx != -1:
            starts.append(idx)
            
    if not starts:
        return None
        
    start_idx = min(starts)
    
    # Walk backward to find if there is a "(function" or "//" comment we missed
    search_limit = max(0, start_idx - 150)
    comment_idx = content.rfind("//", search_limit, start_idx)
    func_idx = content.rfind("(function", search_limit, start_idx)
    
    # Ensure it's not a function call like setTimeout(function
    if func_idx != -1 and func_idx > 0 and content[func_idx-1].isalnum():
        func_idx = -1
        
    if comment_idx != -1 and comment_idx < start_idx:
        start_idx = comment_idx
    elif func_idx != -1 and func_idx < start_idx:
        start_idx = func_idx
        
    # Find the end of the navigation JS block by locating "})();" after keywords
    ends = []
    for keyword in ["mega-services", "nav-drawer", "nav-hamburger"]:
        k_idx = content.find(keyword, start_idx)
        if k_idx != -1:
            end_idx = content.find("})();", k_idx)
            if end_idx != -1:
                ends.append(end_idx + 5)
                
    if not ends:
        end_idx = content.find("})();", start_idx)
        if end_idx != -1:
            return (start_idx, end_idx + 5)
        return None
        
    return (start_idx, max(ends))

def strip_active_classes(nav_html):
    # Replace class="active" with empty string
    nav_html = re.sub(r'\s*class="active"', '', nav_html)
    # Handle mega-item classes
    nav_html = re.sub(r'class="mega-item\s+active"', 'class="mega-item"', nav_html)
    nav_html = re.sub(r'class="active\s+mega-item"', 'class="mega-item"', nav_html)
    return nav_html

def main():
    print("=== Unifying Website Headers and Footers ===")
    
    # 1. Read source of truth page
    with open(SOURCE_PAGE_PATH, 'r', encoding='utf-8') as f:
        src_content = f.read()
        
    # 2. Extract style/HTML/JS components
    nav_css_range = find_nav_css_block(src_content)
    footer_css_range = find_footer_css_block(src_content)
    nav_html_range = extract_nav_html_block(src_content)
    footer_html_range = extract_footer_html_block(src_content)
    nav_js_range = find_nav_js_block(src_content)
    
    if not all([nav_css_range, footer_css_range, nav_html_range, footer_html_range, nav_js_range]):
        print("ERROR: Failed to extract all blocks from source of truth!")
        print(f"nav_css: {nav_css_range}")
        print(f"footer_css: {footer_css_range}")
        print(f"nav_html: {nav_html_range}")
        print(f"footer_html: {footer_html_range}")
        print(f"nav_js: {nav_js_range}")
        return
        
    nav_css_template = src_content[nav_css_range[0]:nav_css_range[1]]
    footer_css_template = src_content[footer_css_range[0]:footer_css_range[1]]
    nav_html_template = src_content[nav_html_range[0]:nav_html_range[1]]
    footer_html_template = src_content[footer_html_range[0]:footer_html_range[1]]
    nav_js_template = src_content[nav_js_range[0]:nav_js_range[1]]
    
    # Standardize links inside the templates
    nav_html_template = nav_html_template.replace('href="web-development.html"', 'href="../Web-Dev/web-development.html"')
    footer_html_template = footer_html_template.replace('href="web-development.html"', 'href="../Web-Dev/web-development.html"')
    
    # Update footer CSS columns to support exactly 4 columns
    footer_css_template = footer_css_template.replace(
        "grid-template-columns: minmax(240px, 1.8fr) repeat(4, minmax(140px, 1fr))",
        "grid-template-columns: minmax(240px, 1.8fr) repeat(3, minmax(140px, 1fr))"
    )
    footer_css_template = footer_css_template.replace(
        "grid-template-columns:minmax(240px,1.8fr) repeat(4,minmax(140px,1fr))",
        "grid-template-columns: minmax(240px, 1.8fr) repeat(3, minmax(140px, 1fr))"
    )
    
    # Clean template: strip any active indicators
    nav_html_template = strip_active_classes(nav_html_template)
    
    print("Extracted source templates successfully!")
    print(f"Nav CSS length: {len(nav_css_template)} bytes")
    print(f"Footer CSS length: {len(footer_css_template)} bytes")
    print(f"Nav HTML length: {len(nav_html_template)} bytes")
    print(f"Footer HTML length: {len(footer_html_template)} bytes")
    print(f"Nav JS length: {len(nav_js_template)} bytes")
    print("--------------------------------------------------")
    
    for folder, filename in PAGES:
        filepath = os.path.join(SRC_DIR, folder, filename)
        print(f"Processing {folder}/{filename}...")
        
        if not os.path.exists(filepath):
            print(f"WARNING: File {filepath} does not exist. Skipping.")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract target ranges
        dest_nav_css_range = find_nav_css_block(content)
        dest_footer_css_range = find_footer_css_block(content)
        dest_nav_html_range = extract_nav_html_block(content)
        dest_footer_html_range = extract_footer_html_block(content)
        dest_nav_js_range = find_nav_js_block(content)
        
        if not all([dest_nav_css_range, dest_footer_css_range, dest_nav_html_range, dest_footer_html_range, dest_nav_js_range]):
            print(f"ERROR: Could not find all replacement ranges in {filename}!")
            print(f"nav_css: {dest_nav_css_range}")
            print(f"footer_css: {dest_footer_css_range}")
            print(f"nav_html: {dest_nav_html_range}")
            print(f"footer_html: {dest_footer_html_range}")
            print(f"nav_js: {dest_nav_js_range}")
            continue
            
        # Strip/set active classes in Navigation HTML specifically for this page
        nav_html = nav_html_template
        
        # Decide active states
        if filename == "homepage.html":
            nav_html = nav_html.replace('href="../Home/homepage.html"', 'href="../Home/homepage.html" class="active"')
        elif filename == "services.html":
            nav_html = nav_html.replace('href="../Services/services.html"', 'href="../Services/services.html" class="active"')
        elif filename == "aboutus.html":
            nav_html = nav_html.replace('href="../About/aboutus.html"', 'href="../About/aboutus.html" class="active"')
        elif filename == "blog.html":
            nav_html = nav_html.replace('href="../Blog/blog.html"', 'href="../Blog/blog.html" class="active"')
        elif filename == "contact.html":
            nav_html = nav_html.replace('href="../Contact/contact.html"', 'href="../Contact/contact.html" class="active"')
        else:
            # It is a services sub-page
            # 1. Main Services nav link active
            nav_html = nav_html.replace('href="../Services/services.html"', 'href="../Services/services.html" class="active"')
            
            # 2. Sub-menu link active (mega menu and drawer)
            if filename == "web-development.html":
                nav_html = nav_html.replace('class="mega-item" href="../Web-Dev/web-development.html"', 'class="mega-item active" href="../Web-Dev/web-development.html"')
                nav_html = nav_html.replace('href="../Web-Dev/web-development.html">Web Development</a>', 'href="../Web-Dev/web-development.html" class="active">Web Development</a>')
            elif filename == "mobile-app.html":
                nav_html = nav_html.replace('class="mega-item" href="../mobile-app/mobile-app.html"', 'class="mega-item active" href="../mobile-app/mobile-app.html"')
                nav_html = nav_html.replace('href="../mobile-app/mobile-app.html">Mobile App</a>', 'href="../mobile-app/mobile-app.html" class="active">Mobile App</a>')
            elif filename == "ai-solutions.html":
                nav_html = nav_html.replace('class="mega-item" href="../ai-solutions/ai-solutions.html"', 'class="mega-item active" href="../ai-solutions/ai-solutions.html"')
                nav_html = nav_html.replace('href="../ai-solutions/ai-solutions.html">AI Solutions</a>', 'href="../ai-solutions/ai-solutions.html" class="active">AI Solutions</a>')
            elif filename == "e-commerce-solutions.html":
                nav_html = nav_html.replace('class="mega-item" href="../e-commerce-solutions/e-commerce-solutions.html"', 'class="mega-item active" href="../e-commerce-solutions/e-commerce-solutions.html"')
                nav_html = nav_html.replace('href="../e-commerce-solutions/e-commerce-solutions.html">E-Commerce Solutions</a>', 'href="../e-commerce-solutions/e-commerce-solutions.html" class="active">E-Commerce Solutions</a>')
            elif filename == "digital-marketing.html":
                nav_html = nav_html.replace('class="mega-item" href="../digital-marketing/digital-marketing.html"', 'class="mega-item active" href="../digital-marketing/digital-marketing.html"')
                nav_html = nav_html.replace('href="../digital-marketing/digital-marketing.html">Digital Marketing</a>', 'href="../digital-marketing/digital-marketing.html" class="active">Digital Marketing</a>')
                
        # Perform replacements on content buffer.
        # We must replace from end-to-start of the file to keep index ranges accurate.
        blocks = [
            (dest_nav_js_range, nav_js_template),
            (dest_footer_html_range, footer_html_template),
            (dest_nav_html_range, nav_html),
            (dest_footer_css_range, footer_css_template),
            (dest_nav_css_range, nav_css_template)
        ]
        
        # Sort replacements descending by start position to keep offsets correct
        blocks.sort(key=lambda x: x[0][0], reverse=True)
        
        new_content = content
        for (start, end), replacement in blocks:
            new_content = new_content[:start] + replacement + new_content[end:]
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Successfully unified header & footer for {filename}!")
        
    print("=== All Pages Unified Successfully ===")

if __name__ == "__main__":
    main()
