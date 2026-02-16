// ========================================
// CONTENT UPDATE SCRIPT FOR AI AGENTS
// ========================================
// This script shows how AI agents can easily update content
// by modifying the contentSections object

// Example: Update the main headline
function updateMainHeadline(newHeadline) {
    contentSections.header.title = newHeadline;
    console.log('Main headline updated to:', newHeadline);
}

// Example: Update hero subtitle
function updateHeroSubtitle(newSubtitle) {
    contentSections.header.subtitle = newSubtitle;
    console.log('Hero subtitle updated to:', newSubtitle);
}

// Example: Update CTA button text
function updateCTAButtonText(newText) {
    contentSections.header.ctaText = newText;
    contentSections.cta.buttonText = newText;
    console.log('CTA button text updated to:', newText);
}

// Example: Add a new benefit
function addBenefit(title, description) {
    contentSections.benefits.items.push({
        title: title,
        description: description
    });
    console.log('New benefit added:', title);
}

// Example: Update a specific benefit
function updateBenefit(index, title, description) {
    if (contentSections.benefits.items[index]) {
        contentSections.benefits.items[index] = {
            title: title,
            description: description
        };
        console.log('Benefit updated at index', index);
    }
}

// Example: Add a new testimonial
function addTestimonial(quote, author) {
    contentSections.testimonials.items.push({
        quote: quote,
        author: author
    });
    console.log('New testimonial added from:', author);
}

// Example: Update footer address
function updateFooterAddress(newAddress) {
    contentSections.footer.address = newAddress;
    console.log('Footer address updated');
}

// Example: Update company name
function updateCompanyName(newName) {
    contentSections.footer.company = newName;
    console.log('Company name updated to:', newName);
}

// Example: Get current content for review
function getCurrentContent() {
    return JSON.stringify(contentSections, null, 2);
}

// Example: Load content from JSON
function loadContentFromJSON(jsonString) {
    try {
        const newContent = JSON.parse(jsonString);
        Object.assign(contentSections, newContent);
        console.log('Content loaded from JSON');
        return true;
    } catch (error) {
        console.error('Error loading content:', error);
        return false;
    }
}

// ========================================
// AI AGENT USAGE EXAMPLES
// ========================================

// Example 1: Update main messaging
// updateMainHeadline("Transform Your Future with EB-2 NIW Visa");
// updateHeroSubtitle("Join thousands who have successfully obtained U.S. permanent residency through our proven EB-2 NIW program.");

// Example 2: Add new benefit
// addBenefit("Faster Processing", "EB-2 NIW petitions often receive faster processing times compared to other visa categories.");

// Example 3: Update testimonial
// addTestimonial("The team at NextStep USA was incredibly professional and guided me through every step of the process.", "Dr. Sarah Johnson, Data Scientist");

// Example 4: Update company information
// updateCompanyName("NextStep Immigration Services");
// updateFooterAddress("123 Main Street, Suite 100, New York, NY 10001");

// ========================================
// CONTENT STRUCTURE REFERENCE
// ========================================
/*
contentSections = {
    header: {
        title: "Main headline",
        subtitle: "Hero subtitle", 
        ctaText: "Button text",
        logo: "logo path"
    },
    benefits: {
        title: "Benefits section title",
        items: [
            {
                title: "Benefit title",
                description: "Benefit description"
            }
        ]
    },
    process: {
        title: "Process section title",
        steps: [
            {
                number: 1,
                title: "Step title",
                description: "Step description"
            }
        ]
    },
    testimonials: {
        title: "Testimonials section title",
        items: [
            {
                quote: "Customer quote",
                author: "Customer name and title"
            }
        ]
    },
    cta: {
        title: "CTA section title",
        subtitle: "CTA subtitle",
        formAction: "Form submission URL",
        buttonText: "Submit button text"
    },
    footer: {
        copyright: "Copyright text",
        company: "Company name",
        address: "Company address",
        links: [
            {
                text: "Link text",
                url: "Link URL"
            }
        ]
    }
}
*/

console.log('Content update functions loaded. Use these functions to modify content easily.');