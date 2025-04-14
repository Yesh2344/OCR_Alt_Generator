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
```
## Usage

Run the script from the command line with an image file:
```
python alt_text_generator.py path/to/your_image.jpg
```
## Example Output

```
Input: An image of a stop sign.
Output: Suggested alt text: Image with text: 'Stop' showing traffic sign

Input: A photo of a dog.
Output: Suggested alt text: Image of dog
```
## Troubleshooting

- "File not found" Error: Ensure the image path and JSON key path are correct.
- API Errors: Verify the Vision API is enabled and the service account has the right permissions.
- No Output: Check that the image is valid and readable (e.g., .jpg, .png).

## Project Structure

alt_text_generator/
├── alt_text_generator.py  # Main script
├── vision-key.json        # Service account key (not tracked in Git)
└── README.md              # This file

## Notes

- Security: Do not commit vision-key.json to Git. Add it to .gitignore:


```
vision-key.json
```
- Limitations: Alt text is truncated to 100 characters for brevity; adjust the truncate() function in the script if needed.


## Contributing

Feel free to fork this repo, tweak the code, and submit a pull request with improvements!
## License

This project is unlicensed—use it however you like!
## Contact

Email:yeswanthsoma83@gmail.com

Would you like me to create the Python script or a .gitignore file as well?

@YeswanthSoma
All Copyrights Reserved
