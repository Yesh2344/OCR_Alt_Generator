#!/usr/bin/env python

import argparse
import os
from google.cloud import vision
from google.oauth2 import service_account
import io

def truncate(text, max_length=100):
    """Truncate text to 100 chars with '...' if longer."""
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text

def generate_alt_text(text, labels):
    """Make alt text from text and labels."""
    if text and labels:
        return f"Image containing the text '{truncate(text)}' and depicting {', '.join(labels[:3])}"
    elif text:
        return f"Image with text: '{truncate(text)}'"
    elif labels:
        return f"Image of {', '.join(labels[:3])}"
    else:
        return "Image with no detectable text or labels"

def analyze_image(image_path):
    """Hit up Google Cloud Vision API to analyze the image."""
    # Load credentials explicitly
    credentials = service_account.Credentials.from_service_account_file(
        "C:/Users/91964/Downloads/ocr1alt-672e6c2b4ece.json"  # Replace with your actual path
    )
    client = vision.ImageAnnotatorClient(credentials=credentials)

    # Check if image file can be read
    try:
        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()
        if not content:
            raise ValueError("Image file is empty")
    except Exception as e:
        raise Exception(f"Failed to read image file: {e}")

    image = vision.Image(content=content)

    # OCR the text
    try:
        text_response = client.text_detection(image=image)
        texts = text_response.text_annotations
        extracted_text = texts[0].description if texts else ""
    except Exception as e:
        raise Exception(f"Text detection failed: {e}")

    # Recognize objects
    try:
        label_response = client.label_detection(image=image)
        labels = [label.description for label in label_response.label_annotations]
    except Exception as e:
        raise Exception(f"Label detection failed: {e}")

    return extracted_text, labels

def main():
    """Handle the command-line vibes and run the show."""
    parser = argparse.ArgumentParser(description="Automatic Alt Text Generator")
    parser.add_argument("image_path", type=str, help="Path to your image")
    args = parser.parse_args()

    # Verify image path
    if not os.path.exists(args.image_path):
        print(f"Error: '{args.image_path}' doesn’t exist.")
        return
    if not os.path.isfile(args.image_path):
        print(f"Error: '{args.image_path}' is not a file.")
        return

    try:
        text, labels = analyze_image(args.image_path)
        alt_text = generate_alt_text(text, labels)
        print(f"Suggested alt text: {alt_text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()