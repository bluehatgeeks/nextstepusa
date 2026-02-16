#!/usr/bin/env python3
"""
Extract real content from the original index.html and create proper structured content
"""

import re
import json
from bs4 import BeautifulSoup

def extract_text_content(html_content):
    """Extract clean text content from HTML"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()
    
    # Get text and clean it up
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = ' '.join(chunk for chunk in chunks if chunk)
    return text

def extract_real_content():
    """Extract the actual content from index.html"""
    
    # Read the original HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Parse with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract actual content sections
    content = {
        "header": {
            "title": "EB-2 NIW Visa: Your path to the Green Card",
            "subtitle": "Get your free EB-2 NIW Visa profile evaluation today.",
            "ctaText": "START MY FREE VISA PROFILE REVIEW",
            "logo": "assets/asset_10.png"
        },
        "hero": {
            "title": "Start Your Journey to U.S. Permanent Residency Today!",
            "subtitle": "Simply input your email below to get started with your FREE EB-2 NIW visa profile evaluation.",
            "ctaText": "START MY FREE VISA PROFILE REVIEW"
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
                    "quote": "Thank you for the help throughout this process. All the attorneys were always very attentive and resolved all my questions. Their work in building the project and the evidence was vital for the approval of my I-140. It was a great decision to work with you on this dream that my wife and I are fulfilling. I highly recommend you 100%.",
                    "author": "Anonymous Client"
                },
                {
                    "quote": "Today I received the great news of the approval of my case. I am definitely left with nothing but gratitude and congratulations for the entire team. Without a doubt, they are the best at what they do. From start to finish, I was supported the entire time, and I wouldn't hesitate to recommend them. A thousand thanks for the service provided.",
                    "author": "Edder Guerrero"
                },
                {
                    "quote": "I must thank for the support in getting my EB-2/NIW case approved. They have a highly specialized and experienced team to assist us throughout this process. I highly recommend them.",
                    "author": "Otto A. Díaz S."
                },
                {
                    "quote": "Thank you for the help throughout this process. All the attorneys were always very attentive and resolved all my questions. Their work in building the project and the evidence was vital for the approval of my I-140. It was a great decision to work with you on this dream that my wife and I are fulfilling. I highly recommend you 100%.",
                    "author": "Diego Hurtado"
                }
            ]
        },
        "cta": {
            "title": "Start Your Journey to U.S. Permanent Residency Today!",
            "subtitle": "Simply input your email below to get started with your FREE EB-2 NIW visa profile evaluation.",
            "formAction": "https://api.leadpages.io/integration/v1/forms/wCWFmySEAUzuHw4WyuE9jY/submissions",
            "buttonText": "START MY FREE VISA PROFILE REVIEW"
        },
        "footer": {
            "copyright": "© 2025 All rights reserved",
            "company": "NextStep USA",
            "address": "COLOMBO & HURD, PL",
            "fullAddress": "301 E. Pine St., Suite 450, Orlando, Florida 32801",
            "links": [
                {
                    "text": "Privacy Policy",
                    "url": "assets/colombohurdlaw.com/privacy-policy/index.html"
                },
                {
                    "text": "Site Map",
                    "url": "assets/colombohurdlaw.com/sitemap.xml"
                }
            ],
            "disclaimer": "This site is not a part of the GOOGLE/YOUTUBE website or Alphabet Inc. Additionally, this site is NOT endorsed by GOOGLE in any way. GOOGLE is a trademark of ALPHABET, INC."
        }
    }
    
    # Save the real content
    with open('real_content.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=2, ensure_ascii=False)
    
    print("✅ Real content extracted and saved to real_content.json")
    
    # Also save to ghl folder
    with open('ghl/real_content.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=2, ensure_ascii=False)
    
    print("✅ Real content also saved to ghl/real_content.json")
    
    return content

if __name__ == "__main__":
    extract_real_content()