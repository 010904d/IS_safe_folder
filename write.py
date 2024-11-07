import os
import shutil

def is_hidden(filepath):
    # Check if the file is hidden (including system files like .git)
    return filepath.startswith('.') or os.path.basename(filepath).startswith('.')

from_dir = input('ENTER the dir of folder to protect: ')
fname = input('Enter folder name to create: ')
pasw = input('Enter the password: ')

todir = r"C:\Users\devan\OneDrive\Desktop"
todir = os.path.join(todir, fname)

# Create the base folder
if not os.path.exists(todir):
    os.mkdir(todir)

# Loop through the password and create nested folders
for i in pasw:
    # Create folders from 1 to 20 within each character directory
    for j in range(1, 21):
        path = os.path.join(todir, str(j))
        os.makedirs(path, exist_ok=True)
        for k in range(1, 21):
            path2 = os.path.join(path, str(k))
            os.makedirs(path2, exist_ok=True)
    
    # Append each password character as a subdirectory in the main folder
    todir = os.path.join(todir, i)
    os.makedirs(todir, exist_ok=True)  # Ensure the subdirectory is created for each password character

# Move the original folder to the final directory path, excluding hidden files
def move_files(src, dest):
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if not is_hidden(os.path.join(root, d))]  # Skip hidden directories
        for file in files:
            file_path = os.path.join(root, file)
            if not is_hidden(file_path):  # Skip hidden files
                try:
                    shutil.move(file_path, os.path.join(dest, file))
                except Exception as e:
                    print(f"Error moving {file_path}: {e}")

# Call the function to move the files and directories
try:
    move_files(from_dir, todir)
    print(f"Moved the folder to {todir}")
except Exception as e:
    print(f"Error: {e}")
