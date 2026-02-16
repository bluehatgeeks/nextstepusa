# GoHighLevel Content Management System

## 📁 GHL Folder Structure

```
ghl/
├── ghl_script.js          # Ready-to-use GoHighLevel custom script
├── content_editor.js      # AI agent editing functions
├── content_template.json  # Content template/structure
└── README.md             # This documentation
```

## 🚀 Quick Start

### For GoHighLevel Integration:
1. Copy the entire content of `ghl_script.js`
2. Paste it into your GoHighLevel custom script element
3. The page will render automatically

### For AI Agent Editing:
1. Use functions from `content_editor.js` to modify content
2. Update the `contentSections` object in `ghl_script.js`
3. Copy the updated script to GoHighLevel

## 🎯 AI Agent Usage

### Basic Content Updates:
```javascript
// Update main messaging
updateMainHeadline("Transform Your Future with EB-2 NIW Visa");
updateHeroSubtitle("Join thousands who have successfully obtained U.S. permanent residency");

// Add new content
addBenefit("Faster Processing", "EB-2 NIW petitions often receive faster processing times");
addTestimonial("The team was incredibly professional", "Dr. Sarah Johnson, Data Scientist");

// Update company info
updateCompanyName("NextStep Immigration Services");
updateFooterAddress("123 Main Street, Suite 100, New York, NY 10001");
```

### Content Structure:
```javascript
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
```

## 🔧 Available Functions

### Header Functions:
- `updateMainHeadline(newHeadline)`
- `updateHeroSubtitle(newSubtitle)`
- `updateCTAButtonText(newText)`
- `updateLogo(newLogoPath)`

### Benefits Functions:
- `addBenefit(title, description)`
- `updateBenefit(index, title, description)`
- `removeBenefit(index)`
- `updateBenefitsTitle(newTitle)`

### Process Functions:
- `addProcessStep(title, description)`
- `updateProcessStep(index, title, description)`
- `removeProcessStep(index)`
- `updateProcessTitle(newTitle)`

### Testimonials Functions:
- `addTestimonial(quote, author)`
- `updateTestimonial(index, quote, author)`
- `removeTestimonial(index)`
- `updateTestimonialsTitle(newTitle)`

### CTA Functions:
- `updateCTATitle(newTitle)`
- `updateCTASubtitle(newSubtitle)`
- `updateFormAction(newAction)`

### Footer Functions:
- `updateCompanyName(newName)`
- `updateFooterAddress(newAddress)`
- `updateCopyright(newCopyright)`
- `addFooterLink(text, url)`
- `updateFooterLink(index, text, url)`
- `removeFooterLink(index)`

### Utility Functions:
- `getCurrentContent()` - Get content as JSON
- `loadContentFromJSON(jsonString)` - Load content from JSON
- `exportContent()` - Download content as JSON file
- `previewChanges()` - Preview current content

## 📋 Workflow

### For Content Updates:
1. Use editing functions to modify content
2. Test changes in browser console
3. Export updated content to JSON
4. Update `ghl_script.js` with new content
5. Copy updated script to GoHighLevel

### For New Content Creation:
1. Start with `content_template.json`
2. Modify content using editing functions
3. Export final content
4. Create new `ghl_script.js` with updated content

### For Team Collaboration:
1. Export content to JSON
2. Share JSON files with team members
3. Each person edits their assigned sections
4. Merge changes by importing/exporting JSON files

## 🎨 Customization

### Styling:
The styles are included in the `ghl_script.js` file. To customize:
1. Modify the CSS in the `styles` variable
2. Update colors, fonts, spacing as needed
3. Test changes in browser before deploying

### Content Sections:
To add new sections:
1. Add section data to `contentSections`
2. Create rendering function
3. Add to `renderFullPage()` function
4. Add corresponding CSS styles

## 🔒 Security Notes

- All content is client-side only
- No data is sent to external servers
- Content is stored in the script itself
- Export/import uses local file system

## 🆘 Troubleshooting

### Script Not Rendering:
- Check for JavaScript errors in browser console
- Ensure all content is properly formatted
- Verify JSON syntax is valid

### Content Not Updating:
- Clear browser cache
- Check function return values
- Use `previewChanges()` to verify updates

### GoHighLevel Issues:
- Ensure script is pasted completely
- Check for any special characters
- Test in browser first before adding to GoHighLevel

## 📞 Support

If you encounter issues:
1. Check browser console for errors
2. Use `previewChanges()` to verify content
3. Export content before making major changes
4. Test changes in browser before deploying to GoHighLevel

---

**This system provides a clean, structured approach to managing your NextStep USA content for both AI agents and GoHighLevel integration.**