#!/usr/bin/env python3
"""
Comprehensive script to inline all external CSS and JavaScript files into index.html
to make it completely self-contained.
"""

import os
import re
import base64
from pathlib import Path

def read_file_content(file_path):
    """Read file content and return as string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def get_asset_path(href):
    """Convert href to local asset path."""
    if href.startswith('assets/'):
        return href
    elif href.startswith('/assets/'):
        return href[1:]  # Remove leading slash
    elif href.startswith('./assets/'):
        return href[2:]  # Remove leading ./
    return None

def inline_css(html_content):
    """Inline all external CSS files."""
    # Find all CSS link tags
    css_pattern = r'<link[^>]*href=["\']([^"\']*\.css[^"\']*)["\'][^>]*>'
    
    def replace_css(match):
        href = match.group(1)
        asset_path = get_asset_path(href)
        
        if asset_path and os.path.exists(asset_path):
            print(f"Inlining CSS: {asset_path}")
            css_content = read_file_content(asset_path)
            return f'<style type="text/css">\n{css_content}\n</style>'
        else:
            print(f"Warning: CSS file not found: {href}")
            return match.group(0)  # Keep original link
    
    return re.sub(css_pattern, replace_css, html_content)

def inline_js(html_content):
    """Inline all external JavaScript files."""
    # Find all script tags with src
    js_pattern = r'<script[^>]*src=["\']([^"\']*\.js[^"\']*)["\'][^>]*></script>'
    
    def replace_js(match):
        src = match.group(1)
        asset_path = get_asset_path(src)
        
        if asset_path and os.path.exists(asset_path):
            print(f"Inlining JavaScript: {asset_path}")
            js_content = read_file_content(asset_path)
            return f'<script type="text/javascript">\n{js_content}\n</script>'
        else:
            print(f"Warning: JavaScript file not found: {src}")
            return match.group(0)  # Keep original script
    
    return re.sub(js_pattern, replace_js, html_content)

def add_missing_assets(html_content):
    """Add any missing asset files that might be referenced but not linked."""
    # List of known asset files that should be inlined
    known_assets = [
        # CSS files
        'assets/asset_0.css',
        'assets/asset_1.css', 
        'assets/asset_62.css',
        'assets/leadpages.net/fonts/font-awesome/6.4.2/css/all.min.css',
        'assets/leadpages.net/fonts/opensans_typeset.css',
        'assets/lpcontent.net/fonts/9NnXuxthGCqvt67qHe2ZbV/Mxo7FHokCB2yC7kRgMtruY.css',
        
        # JavaScript files
        'assets/asset_2.js',
        'assets/asset_19.js',
        'assets/asset_20.js',
        'assets/asset_21.js',
        'assets/asset_22.js',
        'assets/asset_23.js',
        'assets/asset_24.js',
        'assets/asset_25.js',
        'assets/asset_30.js',
        'assets/asset_31.js',
        'assets/asset_32.js',
        'assets/asset_33.js',
        'assets/senja.io/dist/platform.js',
        'assets/niwapproval.io/rt.js',
        'assets/neverbounce.com/widget/dist/NeverBounce.js'
    ]
    
    # Check if any of these files exist and add them if they're not already inlined
    for asset in known_assets:
        if os.path.exists(asset):
            if asset.endswith('.css'):
                # Check if CSS is already inlined
                if f'assets/{asset.split("/")[-1]}' not in html_content:
                    print(f"Adding missing CSS: {asset}")
                    css_content = read_file_content(asset)
                    # Add to head section
                    html_content = html_content.replace('</head>', f'<style type="text/css">\n{css_content}\n</style>\n</head>')
            elif asset.endswith('.js'):
                # Check if JS is already inlined
                if f'assets/{asset.split("/")[-1]}' not in html_content:
                    print(f"Adding missing JavaScript: {asset}")
                    js_content = read_file_content(asset)
                    # Add before closing body tag
                    html_content = html_content.replace('</body>', f'<script type="text/javascript">\n{js_content}\n</script>\n</body>')
    
    return html_content

def main():
    """Main function to process the HTML file."""
    input_file = "index.html"
    output_file = "index_complete_self_contained.html"
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found!")
        return
    
    print("Reading index.html...")
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    print("Inlining CSS files...")
    html_content = inline_css(html_content)
    
    print("Inlining JavaScript files...")
    html_content = inline_js(html_content)
    
    print("Adding any missing assets...")
    html_content = add_missing_assets(html_content)
    
    print(f"Writing complete self-contained HTML to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("Done! The complete self-contained HTML file has been created.")
    print(f"Original size: {os.path.getsize(input_file)} bytes")
    print(f"New size: {os.path.getsize(output_file)} bytes")

if __name__ == "__main__":
    main()


