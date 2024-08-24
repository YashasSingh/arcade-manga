import os
import zipfile
from PIL import Image
from unihiker import Display, Button

# Initialize display and buttons
display = Display()
button_a = Button('A')  # Left button
button_b = Button('B')  # Right button

# Paths to folders
zip_folder = "/mnt/usb/manga_zips/"    # Folder with ZIP files
manga_folder = "/mnt/usb/manga_unzipped/"  # Folder for unzipped manga

# Ensure the destination folder exists
os.makedirs(manga_folder, exist_ok=True)

# Function to unzip manga files
def unzip_manga(source_folder, destination_folder):
    for file_name in os.listdir(source_folder):
        if file_name.endswith('.zip'):
            zip_path = os.path.join(source_folder, file_name)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(destination_folder)
            print(f"Extracted: {file_name}")

# Unzip manga files
unzip_manga(zip_folder, manga_folder)

# Function to list all image files in the chapter folders
def get_all_pages(manga_folder):
    pages = []
    for chapter_folder in sorted(os.listdir(manga_folder)):
        chapter_path = os.path.join(manga_folder, chapter_folder)
        if os.path.isdir(chapter_path):
            for page in sorted(os.listdir(chapter_path)):
                if page.endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                    pages.append(os.path.join(chapter_path, page))
    return pages

# Get a list of all pages across all chapters
all_pages = get_all_pages(manga_folder)

# Function to display an image on the UniHiker screen
def display_image(image_path):
    image = Image.open(image_path)
    display.show_image(image)

# Index for the current page
current_index = 0

# Display the first page initially
if all_pages:
    display_image(all_pages[current_index])

try:
    while True:
        if all_pages:
            # Check if the left button is pressed (previous page)
            if button_a.is_pressed():
                current_index = (current_index - 1) % len(all_pages)
                display_image(all_pages[current_index])
                time.sleep(0.5)  # Debounce delay

            # Check if the right button is pressed (next page)
            if button_b.is_pressed():
                current_index = (current_index + 1) % len(all_pages)
                display_image(all_pages[current_index])
                time.sleep(0.5)  # Debounce delay

        else:
            print("No pages found.")
            break

except KeyboardInterrupt:
    print("Stopped by user.")
