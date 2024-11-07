from cryptography.fernet import Fernet

# Opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

# Using the key
fernet = Fernet(key)

# Get the file path to decrypt
from_dir = input('ENTER the path and file name to decrypt ').strip()

# Open the encrypted file
try:
    with open(from_dir, 'rb') as enc_file:
        encrypted = enc_file.read()
    
    # Decrypt the file
    decrypted = fernet.decrypt(encrypted)
    
    # Write the decrypted data back to the file
    with open(from_dir, 'wb') as dec_file:
        dec_file.write(decrypted)
    
    print("File decrypted successfully.")
except FileNotFoundError:
    print("Error: The specified file was not found.")
except OSError as e:
    print(f"Error: {e}")
