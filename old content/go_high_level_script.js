
// GoHighLevel Custom Script Element
// Copy this entire script into your GoHighLevel custom script element

const contentSections = {
  "header": {
    "title": "Start Your Journey to U.S. Permanent Residency Today!",
    "subtitle": "Simply input your email below to get started with your",
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
    "subtitle": "Simply input your email below to get started with your",
    "formAction": "https://api.leadpages.io/integration/v1/forms/9VMjf6tVkJFYaJyoiEhwNQ/submissions",
    "buttonText": "START MY FREE VISA PROFILE REVIEW"
  },
  "footer": {
    "copyright": "\u00a9 2025 All rights reserved",
    "company": "NextStep USA",
    "address": "COLOMBO & HURD, PL",
    "links": [
      {
        "text": "Privacy Policy",
        "url": "assets/colombohurdlaw.com/privacy-policy/index.html"
      },
      {
        "text": "Site Map",
        "url": "assets/colombohurdlaw.com/sitemap.xml"
      }
    ]
  }
};

// Rendering functions (same as in index_structured.html)
function renderHeader() {
    return `
        <header class="site-header">
            <nav class="main-navigation">
                <div class="logo">
                    <img src="${contentSections.header.logo}" alt="NextStep USA Logo">
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
}

function renderHero() {
    return `
        <section class="hero-section">
            <div class="hero-content">
                <h1 class="hero-title">${contentSections.header.title}</h1>
                <p class="hero-subtitle">${contentSections.header.subtitle}</p>
                <div class="hero-cta">
                    <button class="cta-button">${contentSections.header.ctaText}</button>
                </div>
            </div>
        </section>
    `;
}

function renderBenefits() {
    const benefitsHTML = contentSections.benefits.items.map(item => `
        <div class="benefit-item">
            <h3>${item.title}</h3>
            <p>${item.description}</p>
        </div>
    `).join('');
    
    return `
        <section class="benefits-section">
            <h2>${contentSections.benefits.title}</h2>
            <div class="benefits-grid">
                ${benefitsHTML}
            </div>
        </section>
    `;
}

function renderProcess() {
    const stepsHTML = contentSections.process.steps.map(step => `
        <div class="step">
            <div class="step-number">${step.number}</div>
            <h3>${step.title}</h3>
            <p>${step.description}</p>
        </div>
    `).join('');
    
    return `
        <section class="process-section">
            <h2>${contentSections.process.title}</h2>
            <div class="process-steps">
                ${stepsHTML}
            </div>
        </section>
    `;
}

function renderTestimonials() {
    const testimonialsHTML = contentSections.testimonials.items.map(item => `
        <div class="testimonial">
            <p>"${item.quote}"</p>
            <cite>- ${item.author}</cite>
        </div>
    `).join('');
    
    return `
        <section class="testimonials-section">
            <h2>${contentSections.testimonials.title}</h2>
            <div class="testimonials-grid">
                ${testimonialsHTML}
            </div>
        </section>
    `;
}

function renderCTA() {
    return `
        <section class="cta-section">
            <h2>${contentSections.cta.title}</h2>
            <p>${contentSections.cta.subtitle}</p>
            <form class="cta-form" action="${contentSections.cta.formAction}" method="POST">
                <input type="email" name="email" placeholder="Enter your email" required>
                <button type="submit">${contentSections.cta.buttonText}</button>
            </form>
        </section>
    `;
}

function renderFooter() {
    const linksHTML = contentSections.footer.links.map(link => 
        `<a href="${link.url}">${link.text}</a>`
    ).join(' | ');
    
    return `
        <footer class="site-footer">
            <div class="footer-content">
                <div class="footer-info">
                    <p>${contentSections.footer.copyright}<br>${contentSections.footer.company}</p>
                    <p>${contentSections.footer.address}</p>
                </div>
                <div class="footer-links">
                    ${linksHTML}
                </div>
            </div>
        </footer>
    `;
}

function renderFullPage() {
    return `
        ${renderHeader()}
        ${renderHero()}
        ${renderBenefits()}
        ${renderProcess()}
        ${renderTestimonials()}
        ${renderCTA()}
        ${renderFooter()}
    `;
}

// Render the content
document.write(renderFullPage());
