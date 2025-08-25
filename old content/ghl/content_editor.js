// ========================================
// CONTENT EDITOR FOR AI AGENTS
// ========================================
// This file contains functions for AI agents to easily update content

// ========================================
// CONTENT UPDATE FUNCTIONS
// ========================================

// Update main headline
function updateMainHeadline(newHeadline) {
    contentSections.header.title = newHeadline;
    console.log('✅ Main headline updated to:', newHeadline);
    return true;
}

// Update hero subtitle
function updateHeroSubtitle(newSubtitle) {
    contentSections.header.subtitle = newSubtitle;
    console.log('✅ Hero subtitle updated to:', newSubtitle);
    return true;
}

// Update CTA button text
function updateCTAButtonText(newText) {
    contentSections.header.ctaText = newText;
    contentSections.cta.buttonText = newText;
    console.log('✅ CTA button text updated to:', newText);
    return true;
}

// Update logo path
function updateLogo(newLogoPath) {
    contentSections.header.logo = newLogoPath;
    console.log('✅ Logo updated to:', newLogoPath);
    return true;
}

// ========================================
// BENEFITS SECTION FUNCTIONS
// ========================================

// Add a new benefit
function addBenefit(title, description) {
    contentSections.benefits.items.push({
        title: title,
        description: description
    });
    console.log('✅ New benefit added:', title);
    return true;
}

// Update a specific benefit
function updateBenefit(index, title, description) {
    if (contentSections.benefits.items[index]) {
        contentSections.benefits.items[index] = {
            title: title,
            description: description
        };
        console.log('✅ Benefit updated at index', index);
        return true;
    } else {
        console.error('❌ Benefit index not found:', index);
        return false;
    }
}

// Remove a benefit
function removeBenefit(index) {
    if (contentSections.benefits.items[index]) {
        const removed = contentSections.benefits.items.splice(index, 1)[0];
        console.log('✅ Benefit removed:', removed.title);
        return true;
    } else {
        console.error('❌ Benefit index not found:', index);
        return false;
    }
}

// Update benefits section title
function updateBenefitsTitle(newTitle) {
    contentSections.benefits.title = newTitle;
    console.log('✅ Benefits title updated to:', newTitle);
    return true;
}

// ========================================
// PROCESS SECTION FUNCTIONS
// ========================================

// Add a new process step
function addProcessStep(title, description) {
    const stepNumber = contentSections.process.steps.length + 1;
    contentSections.process.steps.push({
        number: stepNumber,
        title: title,
        description: description
    });
    console.log('✅ New process step added:', title);
    return true;
}

// Update a specific process step
function updateProcessStep(index, title, description) {
    if (contentSections.process.steps[index]) {
        contentSections.process.steps[index] = {
            number: index + 1,
            title: title,
            description: description
        };
        console.log('✅ Process step updated at index', index);
        return true;
    } else {
        console.error('❌ Process step index not found:', index);
        return false;
    }
}

// Remove a process step
function removeProcessStep(index) {
    if (contentSections.process.steps[index]) {
        const removed = contentSections.process.steps.splice(index, 1)[0];
        // Renumber remaining steps
        contentSections.process.steps.forEach((step, i) => {
            step.number = i + 1;
        });
        console.log('✅ Process step removed:', removed.title);
        return true;
    } else {
        console.error('❌ Process step index not found:', index);
        return false;
    }
}

// Update process section title
function updateProcessTitle(newTitle) {
    contentSections.process.title = newTitle;
    console.log('✅ Process title updated to:', newTitle);
    return true;
}

// ========================================
// TESTIMONIALS SECTION FUNCTIONS
// ========================================

// Add a new testimonial
function addTestimonial(quote, author) {
    contentSections.testimonials.items.push({
        quote: quote,
        author: author
    });
    console.log('✅ New testimonial added from:', author);
    return true;
}

// Update a specific testimonial
function updateTestimonial(index, quote, author) {
    if (contentSections.testimonials.items[index]) {
        contentSections.testimonials.items[index] = {
            quote: quote,
            author: author
        };
        console.log('✅ Testimonial updated at index', index);
        return true;
    } else {
        console.error('❌ Testimonial index not found:', index);
        return false;
    }
}

// Remove a testimonial
function removeTestimonial(index) {
    if (contentSections.testimonials.items[index]) {
        const removed = contentSections.testimonials.items.splice(index, 1)[0];
        console.log('✅ Testimonial removed from:', removed.author);
        return true;
    } else {
        console.error('❌ Testimonial index not found:', index);
        return false;
    }
}

// Update testimonials section title
function updateTestimonialsTitle(newTitle) {
    contentSections.testimonials.title = newTitle;
    console.log('✅ Testimonials title updated to:', newTitle);
    return true;
}

// ========================================
// CTA SECTION FUNCTIONS
// ========================================

// Update CTA section title
function updateCTATitle(newTitle) {
    contentSections.cta.title = newTitle;
    console.log('✅ CTA title updated to:', newTitle);
    return true;
}

// Update CTA subtitle
function updateCTASubtitle(newSubtitle) {
    contentSections.cta.subtitle = newSubtitle;
    console.log('✅ CTA subtitle updated to:', newSubtitle);
    return true;
}

// Update form action URL
function updateFormAction(newAction) {
    contentSections.cta.formAction = newAction;
    console.log('✅ Form action updated to:', newAction);
    return true;
}

// ========================================
// FOOTER SECTION FUNCTIONS
// ========================================

// Update company name
function updateCompanyName(newName) {
    contentSections.footer.company = newName;
    console.log('✅ Company name updated to:', newName);
    return true;
}

// Update footer address
function updateFooterAddress(newAddress) {
    contentSections.footer.address = newAddress;
    console.log('✅ Footer address updated to:', newAddress);
    return true;
}

// Update copyright text
function updateCopyright(newCopyright) {
    contentSections.footer.copyright = newCopyright;
    console.log('✅ Copyright updated to:', newCopyright);
    return true;
}

// Add a footer link
function addFooterLink(text, url) {
    contentSections.footer.links.push({
        text: text,
        url: url
    });
    console.log('✅ Footer link added:', text);
    return true;
}

// Update a footer link
function updateFooterLink(index, text, url) {
    if (contentSections.footer.links[index]) {
        contentSections.footer.links[index] = {
            text: text,
            url: url
        };
        console.log('✅ Footer link updated at index', index);
        return true;
    } else {
        console.error('❌ Footer link index not found:', index);
        return false;
    }
}

// Remove a footer link
function removeFooterLink(index) {
    if (contentSections.footer.links[index]) {
        const removed = contentSections.footer.links.splice(index, 1)[0];
        console.log('✅ Footer link removed:', removed.text);
        return true;
    } else {
        console.error('❌ Footer link index not found:', index);
        return false;
    }
}

// ========================================
// UTILITY FUNCTIONS
// ========================================

// Get current content as JSON
function getCurrentContent() {
    return JSON.stringify(contentSections, null, 2);
}

// Load content from JSON
function loadContentFromJSON(jsonString) {
    try {
        const newContent = JSON.parse(jsonString);
        Object.assign(contentSections, newContent);
        console.log('✅ Content loaded from JSON');
        return true;
    } catch (error) {
        console.error('❌ Error loading content:', error);
        return false;
    }
}

// Export content to JSON file (for browser download)
function exportContent() {
    const dataStr = JSON.stringify(contentSections, null, 2);
    const dataBlob = new Blob([dataStr], {type: 'application/json'});
    const url = URL.createObjectURL(dataBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'nextstep_content.json';
    link.click();
    URL.revokeObjectURL(url);
    console.log('✅ Content exported to nextstep_content.json');
}

// Preview changes (for testing)
function previewChanges() {
    console.log('📋 Current Content Preview:');
    console.log('Header Title:', contentSections.header.title);
    console.log('Benefits Count:', contentSections.benefits.items.length);
    console.log('Process Steps Count:', contentSections.process.steps.length);
    console.log('Testimonials Count:', contentSections.testimonials.items.length);
    console.log('Company Name:', contentSections.footer.company);
}

// ========================================
// AI AGENT USAGE EXAMPLES
// ========================================

/*
// Example 1: Update main messaging
updateMainHeadline("Transform Your Future with EB-2 NIW Visa");
updateHeroSubtitle("Join thousands who have successfully obtained U.S. permanent residency through our proven EB-2 NIW program.");

// Example 2: Add new benefit
addBenefit("Faster Processing", "EB-2 NIW petitions often receive faster processing times compared to other visa categories.");

// Example 3: Add new testimonial
addTestimonial("The team at NextStep USA was incredibly professional and guided me through every step of the process.", "Dr. Sarah Johnson, Data Scientist");

// Example 4: Update company information
updateCompanyName("NextStep Immigration Services");
updateFooterAddress("123 Main Street, Suite 100, New York, NY 10001");

// Example 5: Preview all changes
previewChanges();

// Example 6: Export updated content
exportContent();
*/

console.log('🎯 Content Editor loaded successfully!');
console.log('📝 Available functions:');
console.log('- updateMainHeadline(), updateHeroSubtitle(), updateCTAButtonText()');
console.log('- addBenefit(), updateBenefit(), removeBenefit()');
console.log('- addProcessStep(), updateProcessStep(), removeProcessStep()');
console.log('- addTestimonial(), updateTestimonial(), removeTestimonial()');
console.log('- updateCTATitle(), updateCTASubtitle(), updateFormAction()');
console.log('- updateCompanyName(), updateFooterAddress(), updateCopyright()');
console.log('- addFooterLink(), updateFooterLink(), removeFooterLink()');
console.log('- getCurrentContent(), loadContentFromJSON(), exportContent(), previewChanges()');