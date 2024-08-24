import os
import time
from PIL import Image
from unihiker import Display

# Initialize display
display = Display()

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

# Scrolling loop
current_index = 0

try:
    while True:
        if image_files:
            # Display the current image
            display_image(os.path.join(image_folder, image_files[current_index]))
            
            # Wait for a few seconds before showing the next image
            time.sleep(3)  # Adjust the time as needed
            
            # Move to the next image, loop back if at the end
            current_index = (current_index + 1) % len(image_files)
        else:
            print("No images found in the folder.")
            break

except KeyboardInterrupt:
    print("Stopped by user.")
