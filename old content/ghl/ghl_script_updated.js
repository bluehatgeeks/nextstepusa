// ========================================
// GO HIGH LEVEL CUSTOM SCRIPT ELEMENT
// ========================================
// Copy this entire script into your GoHighLevel custom script element

const contentSections = {
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
};

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
