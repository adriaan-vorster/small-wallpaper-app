import os
import random
import shutil
import ctypes
from pathlib import Path


def set_random_wallpaper(src_folder, username):
    # Get the path to the Themes folder
    themes_folder = Path(f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Themes")

    # List all files in the source folder
    files = [f for f in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, f))]

    if not files:
        print("No files found in the source folder.")
        return

    # Select a random file
    random_file = random.choice(files)
    src_file = os.path.join(src_folder, random_file)

    # Define the destination file path
    dest_file = themes_folder / "TranscodedWallpaper"

    # Copy the file to the destination
    shutil.copy(src_file, dest_file)
    print(f"Copied {src_file} to {dest_file}")

    # Refresh the desktop to apply the new wallpaper
    ctypes.windll.user32.SystemParametersInfoW(0x0014, 0, str(dest_file), 0x0001)
    print("Desktop wallpaper updated.")


if __name__ == "__main__":
    # Path to the folder containing the images
    src_folder = "[Your Wallpaper Dir]"

    # Replace 'your_username' with your actual username
    username = "[Your Username]"

    set_random_wallpaper(src_folder, username)
