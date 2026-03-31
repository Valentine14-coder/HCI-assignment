# Adding Sol Plaatje Municipality Logo Background

The FixMyCommunity website is now set up to display the Sol Plaatje Municipality logo as a background image with a subtle overlay to maintain text readability.

## How to Add the Logo Image

### Step 1: Save the Logo Image
1. Save the Sol Plaatje Municipality logo image as: `sol-plaatje-logo.png`
2. Place it in the `static/images/` folder:
   ```
   Django/
   └── static/
       └── images/
           └── sol-plaatje-logo.png
   ```

### Step 2: File Format & Recommendations
- **Format**: PNG, JPG, or WebP
- **Size**: 1920x1080px or larger for best quality
- **File Size**: Keep under 500KB for fast loading
- **Orientation**: Landscape recommended

### Step 3: Test the Background
Run the development server:
```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

The logo should now appear as a background with a semi-transparent overlay to ensure text remains readable.

## Customizing the Overlay

If you want to adjust the overlay transparency (current setting is 95%, or 0.95), edit the `templates/base.html` file:

```css
background-image: 
    linear-gradient(135deg, rgba(102, 126, 234, 0.95), rgba(118, 75, 162, 0.95)),
    url('{% static "images/sol-plaatje-logo.png" %}');
```

Change the `0.95` values (0 = transparent, 1 = opaque):
- **0.7** = More transparent, logo more visible
- **0.95** = Current (default, text-friendly)
- **1.0** = Fully opaque gradient, logo barely visible

## Directory Structure
```
Django/
├── static/
│   └── images/
│       └── sol-plaatje-logo.png  ← Place logo here
├── templates/
│   └── base.html                 ← Background styling configured
├── fixmycommunity_config/
│   └── settings.py              ← Static files configured
└── ... other files
```

## Production Note
For production deployment, run:
```bash
python manage.py collectstatic
```

This will copy all static files to the `staticfiles/` directory.

---

**Status**: ✅ Ready for logo image  
**Static Files**: ✅ Configured  
**CSS**: ✅ Updated for background display
