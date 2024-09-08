

# UniHiker Manga Reader

![image](https://github.com/user-attachments/assets/accb8492-6219-49f9-a3c3-d6da268d77b3)


The UniHiker Manga Reader is a simple, interactive manga reading application designed to run on a UniHiker device. It allows users to read manga chapters from a USB hard drive, navigate between pages, switch between chapters, and return to the manga selection menu with ease.

## Features

- **Manga and Chapter Selection:** 
  - Browse through a list of manga titles and select the one you want to read.
  - Choose the chapter you want to start reading.

- **Page Navigation:** 
  - Use the **A** button to go to the previous page and the **B** button to go to the next page.
  - Seamlessly navigate between chapters.

- **Home Button:** 
  - Press the **Home** button at any time to return to the main manga selection screen.

- **Automatic Extraction:** 
  - The application automatically extracts manga chapters from ZIP files on the USB hard drive.

## Installation

1. **Hardware Requirements:**
   - UniHiker device
   - USB hard drive containing your manga ZIP files
   - The ZIP files should be organized as follows:
     ```
     manga_zips/
     ├── manga1.zip
     ├── manga2.zip
     └── manga3.zip
     ```

2. **Software Requirements:**
   - Ensure your UniHiker device has Python installed.
   - Install the required libraries:
     ```bash
     pip install pillow unihiker
     ```

3. **File Setup:**
   - Copy the script to your UniHiker.
   - Create directories on your USB drive:
     ```
     /mnt/usb/manga_zips/       # For your zipped manga files
     /mnt/usb/manga_unzipped/   # Where the unzipped manga chapters will be stored
     ```

## Usage

1. **Run the Script:**
   - Execute the script on your UniHiker device.

2. **Select Manga and Chapter:**
   - Use the on-screen instructions to choose a manga and chapter.

3. **Navigate Pages:**
   - Use the **A** and **B** buttons to move between pages.
   - If you reach the end or start of a chapter, the application will prompt you to move to the next or previous chapter.

4. **Return to Home:**
   - Press the **Home** button at any time to return to the main manga selection menu.

## Contributing

If you want to contribute or report issues, please feel free to open a pull request or submit an issue on the project repository.

## License

This project is licensed under the MIT License.

