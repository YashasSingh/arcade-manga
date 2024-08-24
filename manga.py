import os
import time
from PIL import Image
from unihiker import Display, Button

# Initialize display and buttons
display = Display()
button_a = Button('A')  # Left button
button_b = Button('B')  # Right button

# Path to the folder with images (assuming the USB drive is mounted at /mnt/usb)
image_folder = "/mnt/usb/images/"

# List all image files in the folder (you can add more extensions if needed)
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
