# Automatic Alt Text Generator

This tool uses the **Google Cloud Vision API** to automatically generate alt text for images.

---

## 2. Set Up Google Cloud Vision API

1. **Go to the [Google Cloud Console](https://console.cloud.google.com/).**
2. **Create a project** (or use an existing one).
3. **Enable the Cloud Vision API**:
   - Navigate to **APIs & Services > Library**, search for `"Cloud Vision API"`, and click **Enable**.
4. **Create a service account**:
   - Go to **IAM & Admin > Service Accounts > Create Service Account**.
   - Name it (e.g., `vision-api-user`), assign the role **"Cloud Vision API User"** or **"Editor"**, and click **Done**.
5. **Generate a JSON key**:
   - Select your service account, go to **Keys > Add Key > JSON**, and download the file (e.g., `vision-key.json`).
   - Place the JSON file in a secure location (e.g., `/path/to/vision-key.json`).

---

## 3. Update the Script

Edit `alt_text_generator.py` to point to your JSON key file:

```python
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    "/path/to/vision-key.json"  # Replace with your actual path
)
