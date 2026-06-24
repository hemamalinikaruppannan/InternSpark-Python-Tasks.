import os
import shutil
import logging
from datetime import datetime

# 1. Setup Logging Configuration

log_filename = f"file_management_{datetime.now().strftime('%Y%m%d')}.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_filename, encoding='utf-8'), # Added encoding here
        logging.StreamHandler()
    ]
)

# Define file types and their corresponding folder names
EXTENSION_MAPPING = {
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css', '.sh']
}

def organize_directory(target_dir):
    """
    Sorts files in the target directory into specific category folders 
    based on their extensions.
    """
    # Exception Handling: Check if the path exists
    if not os.path.exists(target_dir):
        logging.error(f"The path '{target_dir}' does not exist.")
        print("❌ Error: The specified directory path does not exist.")
        return

    # Exception Handling: Check if it's actually a directory
    if not os.path.isdir(target_dir):
        logging.error(f"The path '{target_dir}' is not a valid directory.")
        print("❌ Error: The path provided is a file, not a directory.")
        return

    logging.info(f"Starting file organization in: {target_dir}")
    print(f"\n📂 Organizing: {target_dir}...\n")

    try:
        # List all items in the directory
        items = os.listdir(target_dir)
        files_moved = 0

        for item in items:
            item_path = os.path.join(target_dir, item)

            # Skip directories, we only want to process files
            if os.path.isdir(item_path):
                continue

            # Extract file extension
            
            _, extension = os.path.splitext(item)
            extension = extension.lower()
            
            # Determine destination folder category
            moved = False
            for category, extensions in EXTENSION_MAPPING.items():
                if extension in extensions:
                    category_dir = os.path.join(target_dir, category)
                    
                    # Create the category directory if it doesn't exist
                    if not os.path.exists(category_dir):
                        os.makedirs(category_dir)
                        logging.info(f"Created new folder: {category_dir}")

                    # Move file
                    dest_path = os.path.join(category_dir, item)
                    shutil.move(item_path, dest_path)
                    logging.info(f"Moved: {item} -> {category}/")
                    files_moved += 1
                    moved = True
                    break

            # If extension doesn't match any category, move to 'Others'
            if not moved and extension:  # ensuring it's not a file without an extension
                others_dir = os.path.join(target_dir, 'Others')
                if not os.path.exists(others_dir):
                    os.makedirs(others_dir)
                
                dest_path = os.path.join(others_dir, item)
                shutil.move(item_path, dest_path)
                logging.info(f"Moved: {item} -> Others/")
                files_moved += 1

        logging.info(f"Organization complete. Total files moved: {files_moved}")
        print(f"✅ Success! Organized {files_moved} files. Details saved to '{log_filename}'.")

    except PermissionError:
        logging.error(f"Permission denied while accessing '{target_dir}'.")
        print("❌ Error: Permission denied. Run the script with administrator privileges.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("--- 🛠️ Python File Automation & Sorting Tool ---")
    # User Input Support
    user_directory = input("Enter the absolute path of the directory to clean/organize: ").strip()
    organize_directory(user_directory)  # 👈 Double-check: No "r" after organize!