#!/usr/bin/env python3
import os
import re
import requests
import urllib.parse
from pathlib import Path

def download_file(url, local_path):
    """Download a file from URL to local path"""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        # Write file
        with open(local_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {url} -> {local_path}")
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

def extract_urls_from_html(html_content):
    """Extract all external URLs from HTML content"""
    urls = set()
    
    # Find all URLs in various attributes
    patterns = [
        r'href=["\']([^"\']+)["\']',
        r'src=["\']([^"\']+)["\']',
        r'url\(["\']?([^"\')\s]+)["\']?\)',
        r'content=["\']([^"\']+)["\']',
        r'data-src=["\']([^"\']+)["\']',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, html_content, re.IGNORECASE)
        for match in matches:
            if match.startswith('http'):
                urls.add(match)
    
    return urls

def create_local_path(url, base_dir="assets"):
    """Create a local file path for a URL"""
    parsed = urllib.parse.urlparse(url)
    
    # Create a safe filename from the URL
    path_parts = parsed.netloc.split('.')
    if len(path_parts) > 2:
        # For subdomains, use the main domain
        domain = '.'.join(path_parts[-2:])
    else:
        domain = parsed.netloc
    
    # Get the path and filename
    path = parsed.path
    if not path or path == '/':
        path = '/index.html'
    
    # Create local path
    local_path = os.path.join(base_dir, domain, path.lstrip('/'))
    
    # Ensure we have a filename
    if not os.path.basename(local_path):
        local_path = os.path.join(local_path, 'index.html')
    
    return local_path

def main():
    # Read the HTML file
    with open('niw_full.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Extract all URLs
    urls = extract_urls_from_html(html_content)
    
    print(f"Found {len(urls)} external URLs")
    
    # Download each file
    downloaded_count = 0
    for url in urls:
        local_path = create_local_path(url)
        if download_file(url, local_path):
            downloaded_count += 1
    
    print(f"Successfully downloaded {downloaded_count} files")

if __name__ == "__main__":
    main()

