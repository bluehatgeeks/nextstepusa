#!/usr/bin/env python3
"""
Content Extraction Script for NextStep USA HTML
This script helps extract content from the original HTML file and prepare it for the editable template.
"""

import re
from bs4 import BeautifulSoup
import json
import os

def extract_sections_from_html(html_file_path):
    """
    Extract content sections from the original HTML file
    """
    with open(html_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Define section patterns based on the original HTML structure
    sections = {
        'header': {
            'title': 'Header Section',
            'description': 'Navigation and branding elements',
            'content': ''
        },
        'hero': {
            'title': 'Hero Section', 
            'description': 'Main headline and call-to-action',
            'content': ''
        },
        'benefits': {
            'title': 'Benefits Section',
            'description': 'Key advantages of EB-2 NIW visa',
            'content': ''
        },
        'process': {
            'title': 'Process Section',
            'description': 'Step-by-step application process',
            'content': ''
        },
        'testimonials': {
            'title': 'Testimonials Section',
            'description': 'Client reviews and success stories',
            'content': ''
        },
        'cta': {
            'title': 'Call-to-Action Section',
            'description': 'Email capture form for lead generation',
            'content': ''
        },
        'footer': {
            'title': 'Footer Section',
            'description': 'Contact info and legal links',
            'content': ''
        }
    }
    
    # Extract header content (navigation and branding)
    header_section = soup.find('section', {'id': 'header'})
    if header_section:
        sections['header']['content'] = str(header_section)
    else:
        # Look for navigation elements
        nav = soup.find('nav') or soup.find('header')
        if nav:
            sections['header']['content'] = f'<header class="site-header">{str(nav)}</header>'
    
    # Extract hero content (main headline and CTA)
    hero_patterns = [
        'Start Your Journey to U.S. Permanent Residency',
        'EB-2 NIW visa profile evaluation',
        'FREE EB-2 NIW'
    ]
    
    for pattern in hero_patterns:
        hero_elements = soup.find_all(string=re.compile(pattern, re.IGNORECASE))
        if hero_elements:
            parent = hero_elements[0].parent
            while parent and parent.name != 'section':
                parent = parent.parent
            if parent:
                sections['hero']['content'] = str(parent)
                break
    
    # Extract CTA content (forms)
    forms = soup.find_all('form')
    if forms:
        # Find the main CTA form
        for form in forms:
            if 'email' in str(form).lower() or 'profile' in str(form).lower():
                form_section = form.find_parent('section') or form.find_parent('div', class_='row')
                if form_section:
                    sections['cta']['content'] = str(form_section)
                break
    
    # Extract footer content
    footer = soup.find('footer') or soup.find('section', class_=re.compile('footer', re.IGNORECASE))
    if footer:
        sections['footer']['content'] = str(footer)
    else:
        # Look for copyright and contact info
        copyright_text = soup.find(string=re.compile('© 2025|All rights reserved|NextStep USA'))
        if copyright_text:
            parent = copyright_text.parent
            while parent and parent.name != 'section':
                parent = parent.parent
            if parent:
                sections['footer']['content'] = str(parent)
    
    # Extract testimonials (look for quotes and reviews)
    testimonial_patterns = [
        'testimonial',
        'review',
        'success story',
        'client'
    ]
    
    for pattern in testimonial_patterns:
        testimonial_elements = soup.find_all(class_=re.compile(pattern, re.IGNORECASE))
        if testimonial_elements:
            sections['testimonials']['content'] = str(testimonial_elements[0].parent)
            break
    
    # Extract benefits section
    benefits_patterns = [
        'benefit',
        'advantage',
        'why choose',
        'feature'
    ]
    
    for pattern in benefits_patterns:
        benefit_elements = soup.find_all(string=re.compile(pattern, re.IGNORECASE))
        if benefit_elements:
            parent = benefit_elements[0].parent
            while parent and parent.name != 'section':
                parent = parent.parent
            if parent:
                sections['benefits']['content'] = str(parent)
                break
    
    # Extract process section
    process_patterns = [
        'how it works',
        'process',
        'step',
        'procedure'
    ]
    
    for pattern in process_patterns:
        process_elements = soup.find_all(string=re.compile(pattern, re.IGNORECASE))
        if process_elements:
            parent = process_elements[0].parent
            while parent and parent.name != 'section':
                parent = parent.parent
            if parent:
                sections['process']['content'] = str(parent)
                break
    
    return sections

def clean_html_content(content):
    """
    Clean and format HTML content for better editing
    """
    if not content:
        return ''
    
    # Remove excessive whitespace
    content = re.sub(r'\s+', ' ', content)
    
    # Remove script tags (we'll handle these separately)
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
    
    # Remove style tags
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
    
    # Clean up empty elements
    content = re.sub(r'<[^>]*>\s*</[^>]*>', '', content)
    
    return content.strip()

def save_content_json(sections, output_file):
    """
    Save extracted content to JSON file
    """
    # Clean content for each section
    for section_id, section_data in sections.items():
        section_data['content'] = clean_html_content(section_data['content'])
    
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(sections, file, indent=2, ensure_ascii=False)
    
    print(f"Content saved to {output_file}")

def create_content_template():
    """
    Create a template for manual content entry
    """
    template = {
        "header": {
            "title": "Header Section",
            "description": "Navigation and branding elements",
            "content": """<header class="site-header">
    <nav class="main-navigation">
        <div class="logo">
            <img src="assets/asset_10.png" alt="NextStep USA Logo">
        </div>
        <ul class="nav-menu">
            <li><a href="#home">Home</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
</header>"""
        },
        "hero": {
            "title": "Hero Section",
            "description": "Main headline and call-to-action",
            "content": """<section class="hero-section">
    <div class="hero-content">
        <h1 class="hero-title">Start Your Journey to U.S. Permanent Residency Today!</h1>
        <p class="hero-subtitle">Get your FREE EB-2 NIW visa profile evaluation and take the first step towards your American dream.</p>
        <div class="hero-cta">
            <button class="cta-button">START MY FREE VISA PROFILE REVIEW</button>
        </div>
    </div>
</section>"""
        },
        "benefits": {
            "title": "Benefits Section",
            "description": "Key advantages of EB-2 NIW visa",
            "content": """<section class="benefits-section">
    <h2>Why Choose EB-2 NIW Visa?</h2>
    <div class="benefits-grid">
        <div class="benefit-item">
            <h3>No Job Offer Required</h3>
            <p>Unlike other visa categories, EB-2 NIW doesn't require a specific job offer from a U.S. employer.</p>
        </div>
        <div class="benefit-item">
            <h3>Self-Petition</h3>
            <p>You can file your own petition without needing an employer sponsor.</p>
        </div>
        <div class="benefit-item">
            <h3>Permanent Residency</h3>
            <p>Direct path to U.S. permanent residency (green card) for you and your family.</p>
        </div>
    </div>
</section>"""
        },
        "process": {
            "title": "Process Section",
            "description": "Step-by-step application process",
            "content": """<section class="process-section">
    <h2>How It Works</h2>
    <div class="process-steps">
        <div class="step">
            <div class="step-number">1</div>
            <h3>Free Evaluation</h3>
            <p>Complete our free profile evaluation to assess your eligibility.</p>
        </div>
        <div class="step">
            <div class="step-number">2</div>
            <h3>Document Preparation</h3>
            <p>We help you gather and prepare all required documentation.</p>
        </div>
        <div class="step">
            <div class="step-number">3</div>
            <h3>Petition Filing</h3>
            <p>We file your EB-2 NIW petition with USCIS.</p>
        </div>
        <div class="step">
            <div class="step-number">4</div>
            <h3>Approval & Residency</h3>
            <p>Upon approval, you can apply for permanent residency.</p>
        </div>
    </div>
</section>"""
        },
        "testimonials": {
            "title": "Testimonials Section",
            "description": "Client reviews and success stories",
            "content": """<section class="testimonials-section">
    <h2>Success Stories</h2>
    <div class="testimonials-grid">
        <div class="testimonial">
            <p>"NextStep USA made my EB-2 NIW application process smooth and successful. I'm now a permanent resident!"</p>
            <cite>- Dr. Maria Rodriguez, Research Scientist</cite>
        </div>
        <div class="testimonial">
            <p>"Professional, knowledgeable, and results-driven. Highly recommend their services."</p>
            <cite>- Dr. Ahmed Hassan, Software Engineer</cite>
        </div>
    </div>
</section>"""
        },
        "cta": {
            "title": "Call-to-Action Section",
            "description": "Email capture form for lead generation",
            "content": """<section class="cta-section">
    <h2>Ready to Start Your Journey?</h2>
    <p>Simply input your email below to get started with your FREE EB-2 NIW visa profile evaluation.</p>
    <form class="cta-form" action="https://api.leadpages.io/integration/v1/forms/wCWFmySEAUzuHw4WyuE9jY/submissions" method="POST">
        <input type="email" name="email" placeholder="Enter your email" required>
        <button type="submit">START MY FREE VISA PROFILE REVIEW</button>
    </form>
</section>"""
        },
        "footer": {
            "title": "Footer Section",
            "description": "Contact info and legal links",
            "content": """<footer class="site-footer">
    <div class="footer-content">
        <div class="footer-info">
            <p>&copy; 2025 All rights reserved<br>NextStep USA</p>
            <p>COLOMBO & HURD, PL<br>301 E. Pine St., Suite 450, Orlando, Florida 32801</p>
        </div>
        <div class="footer-links">
            <a href="assets/colombohurdlaw.com/privacy-policy/index.html">Privacy Policy</a> | 
            <a href="assets/colombohurdlaw.com/sitemap.xml">Site Map</a> | 
            Terms and Conditions
        </div>
    </div>
</footer>"""
        }
    }
    
    return template

def main():
    """
    Main function to run the content extraction
    """
    print("NextStep USA Content Extraction Tool")
    print("=" * 40)
    
    # Check if original HTML file exists
    original_file = "index.html"
    if os.path.exists(original_file):
        print(f"Found original HTML file: {original_file}")
        
        try:
            # Extract content from original file
            print("Extracting content from original HTML...")
            sections = extract_sections_from_html(original_file)
            
            # Save extracted content
            output_file = "extracted_content.json"
            save_content_json(sections, output_file)
            
            print(f"\nExtraction complete! Check {output_file} for extracted content.")
            print("You can now import this content into the editable template.")
            
        except Exception as e:
            print(f"Error extracting content: {e}")
            print("Creating template instead...")
            sections = create_content_template()
            save_content_json(sections, "content_template.json")
    else:
        print(f"Original HTML file not found: {original_file}")
        print("Creating content template...")
        sections = create_content_template()
        save_content_json(sections, "content_template.json")
        print("Created content_template.json with sample content.")
    
    print("\nNext steps:")
    print("1. Open index_editable.html in your browser")
    print("2. Use the Import Content button to load the JSON file")
    print("3. Click Edit buttons to modify sections")
    print("4. Use Export Content to save your changes")

if __name__ == "__main__":
    main()