import os

# Prompt for the password
pasw = input("Enter the password used in write.py: ")

# Set up the base directory where the folder was initially created
base_dir = r"C:\Users\devan\OneDrive\Desktop\safe"  # Adjust this if necessary

# Reconstruct the path based on the password
final_path = base_dir
for char in pasw:
    final_path = os.path.join(final_path, char)

# Print the constructed path for debugging
print(f"Final directory path based on password: {final_path}")

# Check if the path exists and list the contents if it does
if os.path.exists(final_path):
    print(f"Folder found at: {final_path}")
    print("\nContents:")
    for root, dirs, files in os.walk(final_path):
        level = root.replace(final_path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{sub_indent}{f}")
else:
    print("Error: The specified path does not exist. Please check the password and try again.")
