# Automatic Alt Text Generator

A Python banger that uses Google Cloud Vision API to OCR text and recognize shit in images, then makes alt text.

## Features
- Pulls text with OCR
- Spots objects with image recognition
- Generates alt text like a boss

## Setup
1. Get a Google Cloud project, enable Vision API.
2. Grab a service account JSON key.
3. Set `GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json`.
4. Install: `pip install google-cloud-vision`.

## Run It
```bash
python alt_text_generator.py your_image.jpg
