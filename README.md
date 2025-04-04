# Automatic Alt Text Generator

A Python script that uses Google Cloud Vision API to analyze images, extract text via OCR (Optical Character Recognition), and detect objects/labels, then generates accessibility-friendly alt text. Perfect for web developers or anyone looking to automate image descriptions.

## Features

- **OCR**: Extracts text from images (e.g., signs, receipts, handwritten notes).
- **Image Recognition**: Identifies objects or scenes (e.g., "dog," "car," "landscape").
- **Alt Text Generation**: Combines text and labels into concise descriptions like "Image with text: 'Stop' showing traffic sign."

## Prerequisites

- **Python 3.x**: Ensure Python is installed (`python --version`).
- **Google Cloud Account**: Required for Vision API access.
- **Service Account Key**: A JSON key file from Google Cloud for authentication.

## Setup

### 1. Install Dependencies

Install the required Python library:

```bash
pip install google-cloud-vision google-auth
```
2. Set Up Google Cloud Vision API
Go to the Google Cloud Console.
Create a project (or use an existing one).
Enable the Cloud Vision API:
Navigate to APIs & Services > Library, search for "Cloud Vision API," and click Enable.
Create a service account:
Go to IAM & Admin > Service Accounts > Create Service Account.
Name it (e.g., vision-api-user), assign the role "Cloud Vision API User" or "Editor", and click Done.
Generate a JSON key:
Select your service account, go to Keys > Add Key > JSON, and download the file (e.g., vision-key.json).
Place the JSON file in a secure location (e.g., /path/to/vision-key.json).
3. Update the Script
Edit alt_text_generator.py to point to your JSON key file:

python

Collapse

Wrap

Copy
credentials = service_account.Credentials.from_service_account_file(
    "/path/to/vision-key.json"  # Replace with your actual path
)
Usage
Run the script from the command line with an image file:

bash

Collapse

Wrap

Copy
python alt_text_generator.py path/to/your_image.jpg
Example Output
Input: An image of a stop sign.
Output: Suggested alt text: Image with text: 'Stop' showing traffic sign
Input: A photo of a dog.
Output: Suggested alt text: Image of dog
Troubleshooting
"File not found" Error: Ensure the image path and JSON key path are correct.
API Errors: Verify the Vision API is enabled and the service account has the right permissions.
No Output: Check that the image is valid and readable (e.g., .jpg, .png).
Project Structure
text

Collapse

Wrap

Copy
alt_text_generator/
├── alt_text_generator.py  # Main script
├── vision-key.json        # Service account key (not tracked in Git)
└── README.md              # This file
Notes
Security: Do not commit vision-key.json to Git. Add it to .gitignore:
bash

Collapse

Wrap

Copy
vision-key.json
Limitations: Alt text is truncated to 100 characters for brevity; adjust truncate() in the script if needed.
Contributing
Feel free to fork this repo, tweak the code, and submit a pull request with improvements!

License
This project is unlicensed—use it however you like!

text

Collapse

Wrap

Copy

