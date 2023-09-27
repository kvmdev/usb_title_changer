import os
import eyed3

# Function to change the title of an MP3 file
def change_mp3_title(file_path, new_title):
    audiofile = eyed3.load(file_path)
    audiofile.tag.title = new_title
    audiofile.tag.save()

# Function to browse through the USB drive and change titles
def change_titles_in_usb(usb_path):
    new_title = input("Put a new title for the files")
    for root, _, files in os.walk(usb_path):
        for filename in files:
            if filename.endswith(".mp3"):
                mp3_path = os.path.join(root, filename)
                change_mp3_title(mp3_path, new_title)
                print(f"Title changed for {filename} to {new_title}")

if __name__ == "__main__":
    usb_drive_path = input("Enter the path to your USB drive: ")
    change_titles_in_usb(usb_drive_path)