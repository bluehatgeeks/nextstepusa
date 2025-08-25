#!/usr/bin/env python3
"""
Update Script for GoHighLevel Content Management
This script helps update the ghl_script.js file with new content
"""

import json
import re
import os

def load_content_from_json(json_file):
    """Load content from JSON file"""
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return None

def update_ghl_script(content, output_file="ghl_script_updated.js"):
    """Update the ghl_script.js with new content"""
    
    # Read the original script template
    script_template = '''// ========================================
// GO HIGH LEVEL CUSTOM SCRIPT ELEMENT
// ========================================
// Copy this entire script into your GoHighLevel custom script element

const contentSections = {content_sections};

// ========================================
// RENDERING FUNCTIONS
// ========================================

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

// ========================================
// STYLES
// ========================================

const styles = `
<style>
    /* Reset and base styles */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Inter', sans-serif;
        line-height: 1.6;
        color: #333;
    }
    
    /* Header styles */
    .site-header {
        background: #fff;
        padding: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .main-navigation {
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 2rem;
    }
    
    .logo img {
        height: 40px;
    }
    
    .nav-menu {
        display: flex;
        list-style: none;
        gap: 2rem;
    }
    
    .nav-menu a {
        text-decoration: none;
        color: #333;
        font-weight: 500;
    }
    
    /* Hero section */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 4rem 2rem;
        text-align: center;
    }
    
    .hero-content {
        max-width: 800px;
        margin: 0 auto;
    }
    
    .hero-title {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    
    .cta-button {
        background: #28a745;
        color: white;
        border: none;
        padding: 1rem 2rem;
        font-size: 1.1rem;
        border-radius: 5px;
        cursor: pointer;
        font-weight: bold;
    }
    
    /* Section styles */
    section {
        padding: 4rem 2rem;
    }
    
    section h2 {
        text-align: center;
        margin-bottom: 3rem;
        font-size: 2.5rem;
    }
    
    /* Benefits section */
    .benefits-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .benefit-item {
        text-align: center;
        padding: 2rem;
        background: #f8f9fa;
        border-radius: 10px;
    }
    
    .benefit-item h3 {
        margin-bottom: 1rem;
        color: #667eea;
    }
    
    /* Process section */
    .process-steps {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .step {
        text-align: center;
        padding: 2rem;
    }
    
    .step-number {
        width: 60px;
        height: 60px;
        background: #667eea;
        color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        font-weight: bold;
        margin: 0 auto 1rem;
    }
    
    /* Testimonials */
    .testimonials-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
        gap: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .testimonial {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
    }
    
    .testimonial p {
        font-style: italic;
        margin-bottom: 1rem;
    }
    
    .testimonial cite {
        color: #667eea;
        font-weight: bold;
    }
    
    /* CTA section */
    .cta-section {
        background: #667eea;
        color: white;
        text-align: center;
    }
    
    .cta-form {
        max-width: 500px;
        margin: 2rem auto 0;
        display: flex;
        gap: 1rem;
    }
    
    .cta-form input[type="email"] {
        flex: 1;
        padding: 1rem;
        border: none;
        border-radius: 5px;
        font-size: 1rem;
    }
    
    .cta-form button {
        background: #28a745;
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 5px;
        cursor: pointer;
        font-weight: bold;
    }
    
    /* Footer */
    .site-footer {
        background: #333;
        color: white;
        padding: 2rem;
        text-align: center;
    }
    
    .footer-content {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .footer-links a {
        color: white;
        text-decoration: none;
        margin: 0 0.5rem;
    }
    
    .footer-links a:hover {
        text-decoration: underline;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2rem;
        }
        
        .cta-form {
            flex-direction: column;
        }
        
        .nav-menu {
            display: none;
        }
    }
</style>
`;

// ========================================
// RENDER THE PAGE
// ========================================

// Add styles to head
document.head.insertAdjacentHTML('beforeend', styles);

// Render the content
document.write(renderFullPage());
'''
    
    # Convert content to JSON string with proper formatting
    content_json = json.dumps(content, indent=4, ensure_ascii=False)
    
    # Replace the placeholder in the template
    updated_script = script_template.replace('{content_sections}', content_json)
    
    # Write the updated script
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(updated_script)
    
    print(f"✅ Updated script saved to: {output_file}")
    return True

def main():
    """Main function"""
    print("🔄 GoHighLevel Script Updater")
    print("=" * 40)
    
    # Check for content file
    content_file = "content_template.json"
    if not os.path.exists(content_file):
        print(f"❌ Content file not found: {content_file}")
        print("Please provide a JSON file with your content.")
        return
    
    # Load content
    print(f"📂 Loading content from: {content_file}")
    content = load_content_from_json(content_file)
    
    if not content:
        print("❌ Failed to load content")
        return
    
    # Update script
    print("🔄 Updating ghl_script.js...")
    success = update_ghl_script(content, "ghl_script_updated.js")
    
    if success:
        print("\n✅ Script updated successfully!")
        print("📋 Next steps:")
        print("1. Review ghl_script_updated.js")
        print("2. Copy the content to your GoHighLevel custom script element")
        print("3. Test the page in GoHighLevel")
    else:
        print("❌ Failed to update script")

if __name__ == "__main__":
    main()