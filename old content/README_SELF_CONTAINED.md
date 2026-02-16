# Self-Contained HTML Files

This directory now contains self-contained versions of the original `index.html` file with all external CSS and JavaScript files inlined.

## Files Created

### 1. `index_self_contained.html` (613 KB)
- **Purpose**: Basic self-contained version
- **Contents**: Original HTML with linked external files inlined
- **Size**: 613,248 bytes (51% larger than original)

### 2. `index_complete_self_contained.html` (1.9 MB)
- **Purpose**: Complete self-contained version with all assets
- **Contents**: Original HTML + all linked files + additional asset files found in the assets directory
- **Size**: 1,982,709 bytes (389% larger than original)

## What Was Inlined

### CSS Files
- Font Awesome CSS (`assets/leadpages.net/fonts/font-awesome/6.4.2/css/all.min.css`)
- Open Sans font CSS (`assets/leadpages.net/fonts/opensans_typeset.css`)
- Inter font CSS (`assets/lpcontent.net/fonts/9NnXuxthGCqvt67qHe2ZbV/Mxo7FHokCB2yC7kRgMtruY.css`)
- Main CSS files (`assets/asset_0.css`, `assets/asset_1.css`, `assets/asset_62.css`)

### JavaScript Files
- Senja platform script (`assets/senja.io/dist/platform.js`)
- NIW approval script (`assets/niwapproval.io/rt.js`)
- NeverBounce widget script (`assets/neverbounce.com/widget/dist/NeverBounce.js`)
- Various asset JavaScript files (`assets/asset_*.js`)

## Usage

### For Basic Self-Contained Version
Use `index_self_contained.html` if you only need the files that were originally linked in the HTML.

### For Complete Self-Contained Version
Use `index_complete_self_contained.html` if you want all the asset files included, even if they weren't explicitly linked in the original HTML.

## Benefits

1. **Portability**: The HTML file can be moved anywhere without needing the assets directory
2. **Offline Usage**: All resources are contained within a single file
3. **Simplified Deployment**: No need to manage separate CSS and JavaScript files
4. **Reduced HTTP Requests**: All styles and scripts load with the initial HTML request

## Trade-offs

1. **File Size**: The self-contained files are significantly larger
2. **Caching**: Browsers can't cache individual CSS/JS files separately
3. **Maintenance**: Changes require updating the entire HTML file
4. **Initial Load Time**: Larger file size means longer initial download

## Scripts Used

Two Python scripts were created to generate these files:

1. `inline_assets.py` - Creates the basic self-contained version
2. `inline_all_assets.py` - Creates the complete self-contained version

## Original File

The original `index.html` (405 KB) remains unchanged and can still be used if you prefer to keep the external asset structure.


