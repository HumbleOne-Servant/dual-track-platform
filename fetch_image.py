# FILE: C:\DualTrackLearning_Online\fetch_image.py
# BOX 1 OF 2: NETWORK CLIENT AND DISK DIRECTORY LOCK
import os
import urllib.request

def download_open_web_image():
    # Example destination path matching your local repository structure
    save_directory = r"C:\DualTrackLearning_Online\curriculum"
    target_filename = "downloaded_sample.png"
    full_save_path = os.path.join(save_directory, target_filename)
    
    # A generic, open web address that doesn't block automated scripts
    sample_url = "https://picsum.photos"
    
    print(f"⏳ Attempting to bridge link connection to: {sample_url}")
    
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
# BOX 2 OF 2: DATA STREAM STAGER AND COMPILATION CHECK
    try:
        # Commands the terminal to fetch the image bytes and write them to disk
        urllib.request.urlretrieve(sample_url, full_save_path)
        print(f"✅ Success! Image safely downloaded and saved to: {full_save_path}")
    except Exception as e:
        print(f"❌ Connection Blocked: The server refused the request. Error: {e}")

if __name__ == "__main__":
    download_open_web_image()
