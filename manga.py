import os
import time
import zipfile
from PIL import Image
from unihiker import GUI, Button

# Initialize GUI and buttons
gui = GUI()
button_a = Button('A')  # Left button
button_b = Button('B')  # Right button
button_home = Button('Home')  # Home button

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

# Function to list all manga directories
def get_all_mangas(manga_folder):
    mangas = [folder for folder in os.listdir(manga_folder) if os.path.isdir(os.path.join(manga_folder, folder))]
    return sorted(mangas)

# Function to list all chapters and their pages
def get_all_chapters(manga_path):
    chapters = {}
    chapter_paths = sorted([os.path.join(manga_path, folder) for folder in os.listdir(manga_path) if os.path.isdir(os.path.join(manga_path, folder))])
    
    for chapter_path in chapter_paths:
        pages = sorted([os.path.join(chapter_path, page) for page in os.listdir(chapter_path)
                        if page.endswith(('.png', '.jpg', '.jpeg', '.bmp'))])
        if pages:
            chapter_name = os.path.basename(chapter_path)
            chapters[chapter_name] = pages
    return chapters

# Function to display a list of mangas
def display_manga_selection(mangas):
    gui.clear()
    text = "Select a manga:\n"
    for i, manga in enumerate(mangas):
        text += f"{i + 1}: {manga}\n"
    gui.label(text=text, x=10, y=10, font_size=20)

# Function to display a list of chapters
def display_chapter_selection(chapters):
    gui.clear()
    text = "Select a chapter:\n"
    for i, chapter in enumerate(chapters):
        text += f"{i + 1}: {chapter}\n"
    gui.label(text=text, x=10, y=10, font_size=20)

# Function to select a manga
def select_manga():
    mangas = get_all_mangas(manga_folder)
    current_selection = 0
    display_manga_selection(mangas)

    while True:
        if button_a.is_pressed():
            current_selection = (current_selection - 1) % len(mangas)
            gui.label(text=f"Selected: {mangas[current_selection]}\nA: Up  B: Down  Hold B: Confir
