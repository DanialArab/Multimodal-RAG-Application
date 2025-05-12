import os
import requests

# Create the directories
def create_directories(base_dir):
    directories = ["images", "text", "tables"]
    for dir in directories:
        os.makedirs(os.path.join(base_dir, dir), exist_ok=True)


def download_pdf(pdf_url, save_path):
    """
    Download the PDF from the given URL and save it to the specified path.
    """
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()  # Check if the request was successful

        # Save the content to the specified file
        with open(save_path, "wb") as f:
            f.write(response.content)

        print(f"Successfully downloaded {pdf_url} to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the file: {e}")

