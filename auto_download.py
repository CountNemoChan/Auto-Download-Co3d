import os
import time
import subprocess

def download_dataset(download_folder):
    cmd = f"python ./co3d/download_dataset.py --download_folder {download_folder}"
    max_retries = 100
    retries = 0
    success = False

    while not success and retries < max_retries:
        try:
            print(f"Attempt {retries + 1} of {max_retries}...")
            subprocess.run(cmd, shell=True, check=True)
            success = True
            print("Download completed successfully.")
        except subprocess.CalledProcessError as e:
            retries += 1
            print(f"Error encountered: {e}. Retrying in 5 seconds...")
            time.sleep(5)

    if not success:
        print(f"Failed to download dataset after {max_retries} attempts.")

if __name__ == "__main__":
    download_folder = "/mnt/pfs/data/posediffusion_co3d/"
    download_dataset(download_folder)
