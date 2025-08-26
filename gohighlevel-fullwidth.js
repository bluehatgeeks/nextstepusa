/**
 * GoHighLevel Full Width JavaScript Override
 * This script dynamically applies full-width styles to specific elements
 * after the page has loaded and GoHighLevel has finished rendering.
 */

(function() {
    'use strict';

    // Configuration - update these IDs as needed
    const TARGET_IDS = [
        'row-ELNl3507un',
        'col-ErNvk53zim'
    ];

    // CSS styles to apply
    const FULL_WIDTH_STYLES = {
        width: '100%',
        maxWidth: '100%',
        minWidth: '100%',
        margin: '0',
        padding: '0',
        boxSizing: 'border-box',
        position: 'relative',
        left: '0',
        right: '0',
        transform: 'none',
        float: 'none',
        display: 'block'
    };

    // Function to apply styles to an element
    function applyFullWidthStyles(element) {
        if (!element) return;
        
        // Apply styles directly to the element
        Object.keys(FULL_WIDTH_STYLES).forEach(property => {
            element.style.setProperty(property, FULL_WIDTH_STYLES[property], 'important');
        });

        // Also apply to all child elements that might have width restrictions
        const childSelectors = [
            '.container',
            '[class*="container"]',
            '.layout',
            '[class*="layout"]',
            '.inner-column',
            '[class*="inner-column"]',
            '[class*="css-"]',
            '[class*="flex"]'
        ];

        childSelectors.forEach(selector => {
            const children = element.querySelectorAll(selector);
            children.forEach(child => {
                child.style.setProperty('width', '100%', 'important');
                child.style.setProperty('max-width', '100%', 'important');
                child.style.setProperty('margin', '0', 'important');
                child.style.setProperty('padding', '0', 'important');
                child.style.setProperty('box-sizing', 'border-box', 'important');
            });
        });

        console.log('Applied full-width styles to:', element.id || element.className);
    }

    // Function to find elements by various selector patterns
    function findTargetElements() {
        const elements = [];
        
        TARGET_IDS.forEach(targetId => {
            // Try exact ID match
            let element = document.getElementById(targetId);
            if (element) {
                elements.push(element);
            }

            // Try partial ID match
            const partialMatches = document.querySelectorAll(`[id*="${targetId}"]`);
            partialMatches.forEach(el => {
                if (!elements.includes(el)) {
                    elements.push(el);
                }
            });

            // Try class + ID combination
            const classMatches = document.querySelectorAll(`[class*="${targetId}"]`);
            classMatches.forEach(el => {
                if (!elements.includes(el)) {
                    elements.push(el);
                }
            });
        });

        return elements;
    }

    // Function to apply styles to all target elements
    function applyStylesToTargets() {
        const elements = findTargetElements();
        
        if (elements.length === 0) {
            console.log('No target elements found. Retrying in 1 second...');
            return false;
        }

        elements.forEach(applyFullWidthStyles);
        console.log(`Applied styles to ${elements.length} elements`);
        return true;
    }

    // Function to wait for elements to be available
    function waitForElements(maxAttempts = 20, interval = 500) {
        let attempts = 0;
        
        const checkAndApply = () => {
            attempts++;
            
            if (applyStylesToTargets()) {
                console.log('Successfully applied full-width styles');
                return;
            }
            
            if (attempts >= maxAttempts) {
                console.log('Max attempts reached. Elements may not exist or have different IDs.');
                return;
            }
            
            setTimeout(checkAndApply, interval);
        };
        
        checkAndApply();
    }

    // Function to handle dynamic content changes
    function observeDOMChanges() {
        const observer = new MutationObserver((mutations) => {
            let shouldReapply = false;
            
            mutations.forEach((mutation) => {
                if (mutation.type === 'childList') {
                    mutation.addedNodes.forEach((node) => {
                        if (node.nodeType === Node.ELEMENT_NODE) {
                            // Check if any of our target IDs are in the new content
                            TARGET_IDS.forEach(targetId => {
                                if (node.id && node.id.includes(targetId)) {
                                    shouldReapply = true;
                                }
                                if (node.querySelector && node.querySelector(`[id*="${targetId}"]`)) {
                                    shouldReapply = true;
                                }
                            });
                        }
                    });
                }
            });
            
            if (shouldReapply) {
                console.log('DOM changes detected, reapplying styles...');
                setTimeout(applyStylesToTargets, 100);
            }
        });
        
        observer.observe(document.body, {
            childList: true,
            subtree: true,
            attributes: true,
            attributeFilter: ['id', 'class']
        });
    }

    // Main execution function
    function init() {
        console.log('GoHighLevel Full Width Override initialized');
        
        // Wait for DOM to be ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => {
                setTimeout(waitForElements, 100);
                observeDOMChanges();
            });
        } else {
            setTimeout(waitForElements, 100);
            observeDOMChanges();
        }
    }

    // Start the script
    init();

    // Also try again after a longer delay to catch any late-loading content
    setTimeout(applyStylesToTargets, 2000);
    setTimeout(applyStylesToTargets, 5000);

})();
