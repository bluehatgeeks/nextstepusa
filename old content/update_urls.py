#!/usr/bin/env python3
import re
import urllib.parse

def create_local_path(url):
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
    local_path = f"assets/{domain}{path}"
    
    # Ensure we have a filename
    if not local_path.split('/')[-1]:
        local_path = f"{local_path}index.html"
    
    return local_path

def update_urls_in_html(html_content):
    """Replace all external URLs with local paths"""
    
    def replace_url(match):
        url = match.group(1)
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
        local_path = f"assets/{domain}{path}"
        
        # Ensure we have a filename
        if not local_path.split('/')[-1]:
            local_path = f"{local_path}index.html"
        
        return f'href="{local_path}"'
    
    def replace_src(match):
        url = match.group(1)
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
        local_path = f"assets/{domain}{path}"
        
        # Ensure we have a filename
        if not local_path.split('/')[-1]:
            local_path = f"{local_path}index.html"
        
        return f'src="{local_path}"'
    
    def replace_content(match):
        url = match.group(1)
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
        local_path = f"assets/{domain}{path}"
        
        # Ensure we have a filename
        if not local_path.split('/')[-1]:
            local_path = f"{local_path}index.html"
        
        return f'content="{local_path}"'
    
    updated_content = html_content
    
    # Replace href attributes
    updated_content = re.sub(
        r'href=["\'](https?://[^"\']+)["\']',
        replace_url,
        updated_content,
        flags=re.IGNORECASE
    )
    
    # Replace src attributes
    updated_content = re.sub(
        r'src=["\'](https?://[^"\']+)["\']',
        replace_src,
        updated_content,
        flags=re.IGNORECASE
    )
    
    # Replace content attributes
    updated_content = re.sub(
        r'content=["\'](https?://[^"\']+)["\']',
        replace_content,
        updated_content,
        flags=re.IGNORECASE
    )
    
    return updated_content

def main():
    # Read the HTML file
    with open('niw_full.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Update URLs
    updated_content = update_urls_in_html(html_content)
    
    # Write the updated HTML
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("Updated index.html with local asset paths")

if __name__ == "__main__":
    main()
