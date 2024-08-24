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
    chapter_paths = sorted([os.path.join(manga_folder, folder) for folder in os.listdir(manga_folder)])
    
    for chapter_path in chapter_paths:
        if os.path.isdir(chapter_path):
            for page in sorted(os.listdir(chapter_path)):
                if page.endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                    pages.append(os.path.join(chapter_path, page))
    return pages, chapter_paths

# Get a list of all pages across all chapters
all_pages, chapter_paths = get_all_pages(manga_folder)

# Function to display an image on the UniHiker screen
def display_image(image_path):
    image = Image.open(image_path)
    display.show_image(image)

# Function to display a prompt
def display_prompt():
    display.show_text("Continue to next chapter?\nA: Yes  B: No", font_size=24)

# Indexes for current page and chapter
current_page_index = 0
current_chapter_index = 0

# Display the first page initially
if all_pages:
    display_image(all_pages[current_page_index])

try:
    while True:
        if all_pages:
            # Check if the left button is pressed (previous page)
            if button_a.is_pressed():
                current_page_index = (current_page_index - 1) % len(all_pages)
                display_image(all_pages[current_page_index])
                time.sleep(0.5)  # Debounce delay

            # Check if the right button is pressed (next page)
            if button_b.is_pressed():
                # If at the last page of the current chapter, ask to continue
                if current_page_index == len(all_pages) - 1:
                    display_prompt()
                    time.sleep(0.5)  # Delay for prompt

                    while True:
                        if button_a.is_pressed():  # Continue to next chapter
                            current_chapter_index += 1
                            # Load the next chapter
                            chapter_pages, _ = get_all_pages(chapter_paths[current_chapter_index])
                            all_pages.extend(chapter_pages)
                            current_page_index += 1
                            display_image(all_pages[current_page_index])
                            time.sleep(0.5)  # Debounce delay
                            break

                        elif button_b.is_pressed():  # Stay on last page
                            display_image(all_pages[current_page_index])
                            time.sleep(0.5)  # Debounce delay
                            break

                else:
                    current_page_index = (current_page_index + 1) % len(all_pages)
                    display_image(all_pages[current_page_index])
                    time.sleep(0.5)  # Debounce delay

        else:
            print("No pages found.")
            break

except KeyboardInterrupt:
    print("Stopped by user.")
