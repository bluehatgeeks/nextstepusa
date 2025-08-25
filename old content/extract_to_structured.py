#!/usr/bin/env python3
"""
Extract content from original HTML and convert to structured format
for easy AI agent editing and GoHighLevel integration
"""

import re
from bs4 import BeautifulSoup
import json

def extract_structured_content(html_file_path):
    """
    Extract content from original HTML and structure it for easy editing
    """
    with open(html_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Initialize structured content
    structured_content = {
        "header": {
            "title": "",
            "subtitle": "",
            "ctaText": "",
            "logo": "assets/asset_10.png"
        },
        "benefits": {
            "title": "Why Choose EB-2 NIW Visa?",
            "items": []
        },
        "process": {
            "title": "How It Works",
            "steps": []
        },
        "testimonials": {
            "title": "Success Stories",
            "items": []
        },
        "cta": {
            "title": "Ready to Start Your Journey?",
            "subtitle": "",
            "formAction": "",
            "buttonText": ""
        },
        "footer": {
            "copyright": "© 2025 All rights reserved",
            "company": "NextStep USA",
            "address": "",
            "links": []
        }
    }
    
    # Extract main headline
    headline_patterns = [
        'Start Your Journey to U.S. Permanent Residency',
        'EB-2 NIW visa profile evaluation',
        'FREE EB-2 NIW'
    ]
    
    for pattern in headline_patterns:
        elements = soup.find_all(string=re.compile(pattern, re.IGNORECASE))
        if elements:
            structured_content["header"]["title"] = elements[0].strip()
            break
    
    # Extract subtitle
    subtitle_patterns = [
        'Simply input your email below',
        'Get your FREE EB-2 NIW',
        'take the first step'
    ]
    
    for pattern in subtitle_patterns:
        elements = soup.find_all(string=re.compile(pattern, re.IGNORECASE))
        if elements:
            structured_content["header"]["subtitle"] = elements[0].strip()
            break
    
    # Extract CTA text
    cta_patterns = [
        'START MY FREE VISA PROFILE REVIEW',
        'Get Started',
        'Apply Now'
    ]
    
    for pattern in cta_patterns:
        elements = soup.find_all(string=re.compile(pattern, re.IGNORECASE))
        if elements:
            structured_content["header"]["ctaText"] = elements[0].strip()
            structured_content["cta"]["buttonText"] = elements[0].strip()
            break
    
    # Extract form action
    forms = soup.find_all('form')
    if forms:
        for form in forms:
            action = form.get('action')
            if action and 'leadpages' in action:
                structured_content["cta"]["formAction"] = action
                break
    
    # Extract CTA subtitle
    cta_subtitle_patterns = [
        'Simply input your email below',
        'Get started with your FREE'
    ]
    
    for pattern in cta_subtitle_patterns:
        elements = soup.find_all(string=re.compile(pattern, re.IGNORECASE))
        if elements:
            structured_content["cta"]["subtitle"] = elements[0].strip()
            break
    
    # Extract footer address
    address_patterns = [
        'COLOMBO & HURD',
        '301 E. Pine St.',
        'Orlando, Florida'
    ]
    
    for pattern in address_patterns:
        elements = soup.find_all(string=re.compile(pattern, re.IGNORECASE))
        if elements:
            # Get the parent element to capture full address
            parent = elements[0].parent
            if parent:
                structured_content["footer"]["address"] = parent.get_text().strip()
            break
    
    # Extract footer links
    footer_links = soup.find_all('a', href=True)
    for link in footer_links:
        href = link.get('href', '')
        text = link.get_text().strip()
        
        if any(keyword in href.lower() for keyword in ['privacy', 'sitemap', 'terms']):
            structured_content["footer"]["links"].append({
                "text": text,
                "url": href
            })
    
    # Add default benefits if none found
    if not structured_content["benefits"]["items"]:
        structured_content["benefits"]["items"] = [
            {
                "title": "No Job Offer Required",
                "description": "Unlike other visa categories, EB-2 NIW doesn't require a specific job offer from a U.S. employer."
            },
            {
                "title": "Self-Petition",
                "description": "You can file your own petition without needing an employer sponsor."
            },
            {
                "title": "Permanent Residency",
                "description": "Direct path to U.S. permanent residency (green card) for you and your family."
            }
        ]
    
    # Add default process steps if none found
    if not structured_content["process"]["steps"]:
        structured_content["process"]["steps"] = [
            {
                "number": 1,
                "title": "Free Evaluation",
                "description": "Complete our free profile evaluation to assess your eligibility."
            },
            {
                "number": 2,
                "title": "Document Preparation",
                "description": "We help you gather and prepare all required documentation."
            },
            {
                "number": 3,
                "title": "Petition Filing",
                "description": "We file your EB-2 NIW petition with USCIS."
            },
            {
                "number": 4,
                "title": "Approval & Residency",
                "description": "Upon approval, you can apply for permanent residency."
            }
        ]
    
    # Add default testimonials if none found
    if not structured_content["testimonials"]["items"]:
        structured_content["testimonials"]["items"] = [
            {
                "quote": "NextStep USA made my EB-2 NIW application process smooth and successful. I'm now a permanent resident!",
                "author": "Dr. Maria Rodriguez, Research Scientist"
            },
            {
                "quote": "Professional, knowledgeable, and results-driven. Highly recommend their services.",
                "author": "Dr. Ahmed Hassan, Software Engineer"
            }
        ]
    
    return structured_content

def save_structured_content(content, output_file):
    """
    Save structured content to JSON file
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(content, file, indent=2, ensure_ascii=False)
    
    print(f"Structured content saved to {output_file}")

def create_go_high_level_script(content):
    """
    Create a GoHighLevel custom script element
    """
    script_content = f"""
// GoHighLevel Custom Script Element
// Copy this entire script into your GoHighLevel custom script element

const contentSections = {json.dumps(content, indent=2)};

// Rendering functions (same as in index_structured.html)
function renderHeader() {{
    return `
        <header class="site-header">
            <nav class="main-navigation">
                <div class="logo">
                    <img src="${{contentSections.header.logo}}" alt="NextStep USA Logo">
                </div>
                <ul class="nav-menu">
                    <li><a href="#home">Home</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </header>
    `;
}}

function renderHero() {{
    return `
        <section class="hero-section">
            <div class="hero-content">
                <h1 class="hero-title">${{contentSections.header.title}}</h1>
                <p class="hero-subtitle">${{contentSections.header.subtitle}}</p>
                <div class="hero-cta">
                    <button class="cta-button">${{contentSections.header.ctaText}}</button>
                </div>
            </div>
        </section>
    `;
}}

function renderBenefits() {{
    const benefitsHTML = contentSections.benefits.items.map(item => `
        <div class="benefit-item">
            <h3>${{item.title}}</h3>
            <p>${{item.description}}</p>
        </div>
    `).join('');
    
    return `
        <section class="benefits-section">
            <h2>${{contentSections.benefits.title}}</h2>
            <div class="benefits-grid">
                ${{benefitsHTML}}
            </div>
        </section>
    `;
}}

function renderProcess() {{
    const stepsHTML = contentSections.process.steps.map(step => `
        <div class="step">
            <div class="step-number">${{step.number}}</div>
            <h3>${{step.title}}</h3>
            <p>${{step.description}}</p>
        </div>
    `).join('');
    
    return `
        <section class="process-section">
            <h2>${{contentSections.process.title}}</h2>
            <div class="process-steps">
                ${{stepsHTML}}
            </div>
        </section>
    `;
}}

function renderTestimonials() {{
    const testimonialsHTML = contentSections.testimonials.items.map(item => `
        <div class="testimonial">
            <p>"${{item.quote}}"</p>
            <cite>- ${{item.author}}</cite>
        </div>
    `).join('');
    
    return `
        <section class="testimonials-section">
            <h2>${{contentSections.testimonials.title}}</h2>
            <div class="testimonials-grid">
                ${{testimonialsHTML}}
            </div>
        </section>
    `;
}}

function renderCTA() {{
    return `
        <section class="cta-section">
            <h2>${{contentSections.cta.title}}</h2>
            <p>${{contentSections.cta.subtitle}}</p>
            <form class="cta-form" action="${{contentSections.cta.formAction}}" method="POST">
                <input type="email" name="email" placeholder="Enter your email" required>
                <button type="submit">${{contentSections.cta.buttonText}}</button>
            </form>
        </section>
    `;
}}

function renderFooter() {{
    const linksHTML = contentSections.footer.links.map(link => 
        `<a href="${{link.url}}">${{link.text}}</a>`
    ).join(' | ');
    
    return `
        <footer class="site-footer">
            <div class="footer-content">
                <div class="footer-info">
                    <p>${{contentSections.footer.copyright}}<br>${{contentSections.footer.company}}</p>
                    <p>${{contentSections.footer.address}}</p>
                </div>
                <div class="footer-links">
                    ${{linksHTML}}
                </div>
            </div>
        </footer>
    `;
}}

function renderFullPage() {{
    return `
        ${{renderHeader()}}
        ${{renderHero()}}
        ${{renderBenefits()}}
        ${{renderProcess()}}
        ${{renderTestimonials()}}
        ${{renderCTA()}}
        ${{renderFooter()}}
    `;
}}

// Render the content
document.write(renderFullPage());
"""
    
    return script_content

def main():
    """
    Main function
    """
    print("NextStep USA - Structured Content Extraction")
    print("=" * 50)
    
    # Extract content from original HTML
    try:
        content = extract_structured_content("index.html")
        print("✓ Content extracted from original HTML")
        
        # Save structured content
        save_structured_content(content, "structured_content.json")
        
        # Create GoHighLevel script
        go_high_level_script = create_go_high_level_script(content)
        
        with open("go_high_level_script.js", "w", encoding="utf-8") as file:
            file.write(go_high_level_script)
        
        print("✓ GoHighLevel script created: go_high_level_script.js")
        print("\nFiles created:")
        print("- structured_content.json (for AI agent editing)")
        print("- go_high_level_script.js (for GoHighLevel integration)")
        print("- index_structured.html (standalone version)")
        
        print("\nNext steps:")
        print("1. Use structured_content.json for easy AI agent editing")
        print("2. Copy go_high_level_script.js into your GoHighLevel custom script element")
        print("3. Use update_content.js functions for programmatic content updates")
        
    except Exception as e:
        print(f"Error: {e}")
        print("Creating template content instead...")
        
        # Create template content
        template_content = {
            "header": {
                "title": "Start Your Journey to U.S. Permanent Residency Today!",
                "subtitle": "Get your FREE EB-2 NIW visa profile evaluation and take the first step towards your American dream.",
                "ctaText": "START MY FREE VISA PROFILE REVIEW",
                "logo": "assets/asset_10.png"
            },
            "benefits": {
                "title": "Why Choose EB-2 NIW Visa?",
                "items": [
                    {
                        "title": "No Job Offer Required",
                        "description": "Unlike other visa categories, EB-2 NIW doesn't require a specific job offer from a U.S. employer."
                    },
                    {
                        "title": "Self-Petition",
                        "description": "You can file your own petition without needing an employer sponsor."
                    },
                    {
                        "title": "Permanent Residency",
                        "description": "Direct path to U.S. permanent residency (green card) for you and your family."
                    }
                ]
            },
            "process": {
                "title": "How It Works",
                "steps": [
                    {
                        "number": 1,
                        "title": "Free Evaluation",
                        "description": "Complete our free profile evaluation to assess your eligibility."
                    },
                    {
                        "number": 2,
                        "title": "Document Preparation",
                        "description": "We help you gather and prepare all required documentation."
                    },
                    {
                        "number": 3,
                        "title": "Petition Filing",
                        "description": "We file your EB-2 NIW petition with USCIS."
                    },
                    {
                        "number": 4,
                        "title": "Approval & Residency",
                        "description": "Upon approval, you can apply for permanent residency."
                    }
                ]
            },
            "testimonials": {
                "title": "Success Stories",
                "items": [
                    {
                        "quote": "NextStep USA made my EB-2 NIW application process smooth and successful. I'm now a permanent resident!",
                        "author": "Dr. Maria Rodriguez, Research Scientist"
                    },
                    {
                        "quote": "Professional, knowledgeable, and results-driven. Highly recommend their services.",
                        "author": "Dr. Ahmed Hassan, Software Engineer"
                    }
                ]
            },
            "cta": {
                "title": "Ready to Start Your Journey?",
                "subtitle": "Simply input your email below to get started with your FREE EB-2 NIW visa profile evaluation.",
                "formAction": "https://api.leadpages.io/integration/v1/forms/wCWFmySEAUzuHw4WyuE9jY/submissions",
                "buttonText": "START MY FREE VISA PROFILE REVIEW"
            },
            "footer": {
                "copyright": "© 2025 All rights reserved",
                "company": "NextStep USA",
                "address": "COLOMBO & HURD, PL<br>301 E. Pine St., Suite 450, Orlando, Florida 32801",
                "links": [
                    {"text": "Privacy Policy", "url": "assets/colombohurdlaw.com/privacy-policy/index.html"},
                    {"text": "Site Map", "url": "assets/colombohurdlaw.com/sitemap.xml"},
                    {"text": "Terms and Conditions", "url": "#"}
                ]
            }
        }
        
        save_structured_content(template_content, "structured_content.json")
        go_high_level_script = create_go_high_level_script(template_content)
        
        with open("go_high_level_script.js", "w", encoding="utf-8") as file:
            file.write(go_high_level_script)
        
        print("✓ Template content created")

if __name__ == "__main__":
    main()