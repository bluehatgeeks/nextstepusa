#!/usr/bin/env python3
"""
Script to inline all external CSS and JavaScript files into index.html
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

def main():
    """Main function to process the HTML file."""
    input_file = "index.html"
    output_file = "index_self_contained.html"
    
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
    
    print(f"Writing self-contained HTML to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("Done! The self-contained HTML file has been created.")
    print(f"Original size: {os.path.getsize(input_file)} bytes")
    print(f"New size: {os.path.getsize(output_file)} bytes")

if __name__ == "__main__":
    main()


