import os
import time
import zipfile
from PIL import Image
from unihiker import Display, Button

# Initialize display and buttons
display = Display()
button_a = Button('A')  # Left button
button_b = Button('B')  # Right button

# Paths to folders
zip_folder = "/mnt/usb/zipped_images/"   # Folder with ZIP files
image_folder = "/mnt/usb/unzipped_images/"  # Folder for extracted images

# Ensure the destination folder exists
os.makedirs(image_folder, exist_ok=True)

# Function to unzip files
def unzip_files(source_folder, destination_folder):
    for file_name in os.listdir(source_folder):
        if file_name.endswith('.zip'):
            zip_path = os.path.join(source_folder, file_name)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(destination_folder)
            print(f"Extracted: {file_name}")

# Unzip files from the zip folder to the image folder
unzip_files(zip_folder, image_folder)

# List all image files in the unzipped folder (you can add more extensions if needed)
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

# Sort the files if necessary
image_files.sort()

# Function to display an image on the UniHiker screen
def display_image(image_path):
    image = Image.open(image_path)
    display.show_image(image)

# Index for the current image
current_index = 0

# Display the first image initially
if image_files:
    display_image(os.path.join(image_folder, image_files[current_index]))

try:
    while True:
        if image_files:
            # Check if the left button is pressed (previous image)
            if button_a.is_pressed():
                current_index = (current_index - 1) % len(image_files)
                display_image(os.path.join(image_folder, image_files[current_index]))
                time.sleep(0.5)  # Debounce delay

            # Check if the right button is pressed (next image)
            if button_b.is_pressed():
                current_index = (current_index + 1) % len(image_files)
                display_image(os.path.join(image_folder, image_files[current_index]))
                time.sleep(0.5)  # Debounce delay

        else:
            print("No images found in the folder.")
            break

except KeyboardInterrupt:
    print("Stopped by user.")
