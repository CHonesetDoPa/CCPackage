# Basically a rewrite of Decryption.Py
# Use in packaged executables only
# Basically rewriting get_info.py and Decryption.py

# Proof of concept
# Environment rewritten, decryption logic stays the same
# Reworked code structure to create a single extraction script in order to be packaged in PyInstaller

import uuid
import os
import platform
import socket
import hashlib
import sys
from datetime import datetime
from dateutil.tz import tzlocal
from pathlib import Path
from Crypto.Cipher import AES

DEBUG = True
SEPARATOR = "X"

class Environment():
    """Retrieves environment data on the user's PC, such as Operating System, hostname, current time or date, etc.
    """
    def __init__(self):
        # environment_variables = [(parameter1, cli_letter1, value1), (parameter2, cli_letter2, value2), ...]
        # Priority is already determined by this ordered list
        self._environment_variables = []

        # For parameter priority refer to: https://github.com/CHonesetDoPa/CCPackage/blob/main/README.md
        # 1: Operating system type
        self._environment_variables.append(("os_type", 'o', platform.system()))

        # 2: User time zone
        self._environment_variables.append(("current_timezone", 'z', datetime.now(tzlocal()).strftime('%z')))

        # 3: Current date
        self._environment_variables.append(("current_date", 'd', datetime.now().strftime('%Y-%m-%d')))

        # 4: Current time
        self._environment_variables.append(("current_time", 't', datetime.now().strftime('%H:%M')))

        # 5: Hostname
        self._environment_variables.append(("hostname", 'h', socket.gethostname()))

        # 6: MAC Address
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        mac_address = ":".join([mac[i:i+2] for i in range(0, 12, 2)])
        self._environment_variables.append(("mac_address", 'm', mac_address))

        # 7: Current working directory name
        current_dir = Path(os.getcwd())
        folder_name = current_dir.name
        self._environment_variables.append(("folder_name", 'n', folder_name))

        # 8: If specific file exists under current working directory
        file = current_dir / "default"
        if file.exists() and file.is_file():
            file_exists = "File_Exists"
        else:
            file_exists = "File_NotExists"

        self._environment_variables.append(("file_exists", 'f', file_exists))

    def generate_password(self, mode : str) -> bytes:
        """Generates a password based on which environment parameters is specified in parameter `mode`

        Args:
            mode (str): environment parameters
            refer to: https://github.com/CHonesetDoPa/CCPackage/blob/main/README.md
            Must be one or more of the following characters: o, z, d, t, h, m, n, f

        Returns:
            bytes: key used for AES256 encryption
        """
        # The actual password (environment parameter values, concatenated and separated by "X")
        # This will then be hashed twice to be the AES key
        plaintext = ""
        
        # Sanity check for mode
        for i in mode:
            if i not in "ozdthmnf":
                raise Exception(f"Invalid environment parameter: {i}, in {mode}")

        # Iterate through every environment parameters (with list order)
        for env_parameter, cli_letter, value in self._environment_variables:
            if cli_letter in mode:
                plaintext += value + SEPARATOR
                if DEBUG: print(f"|{env_parameter}: {value}")
        
        # Add environment values to plaintext
        plaintext = plaintext[:-1] # Strip out the last separator
        plaintext_bytes = plaintext.encode("UTF-8")

        if DEBUG: print(plaintext)
        
        # Encode and hash the plaintext (environment parameter values)
        sha256_hasher = hashlib.sha256()
        sha256_hasher.update(plaintext_bytes)
        hash1 = sha256_hasher.hexdigest()
        hash1_bytes = hash1.encode()
        if DEBUG: print("hash1 (plaintext hash):", hash1)

        sha256_hasher = hashlib.sha256()
        sha256_hasher.update(hash1_bytes)
        hash2 = sha256_hasher.digest() # Yes, we're hashing the same thing twice, this is what Decryption/Encryption.py implemented
        if DEBUG: print("hash2 (AES Key, hash1 SHA256 hash):", sha256_hasher.hexdigest()); print(hash2)
        return hash2
    
ENV = Environment()

def IsPackaged() -> bool:
    """Determines if this decryption routine is running in a PyInstaller routine or from source

    Returns:
        bool: True for PyInstaller, False for source
    """
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return True
    else:
        #return False
        print("WARNING: This script is currently running in source mode")
        #raise Exception("This code can only be run in a PyInstaller one-file bundle")

def decrypt_file(file_path : Path, save_path : Path, mode : str):
    # Assuming that the nonce, tag and ciphertext are stored in the same file
    # Assuming nonce: 16 bytes, tag: 16 bytes
    with file_path.open("rb") as encrypted_file:
        # Note, read head offset: 16 bytes (nonce), 32 bytes (tag), the rest after 32 bytes is ciphertext
        nonce, tag, ciphertext = [ encrypted_file.read(x) for x in (16, 16, -1) ]
        key = ENV.generate_password(mode)
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        #data = cipher.decrypt_and_verify(ciphertext, tag)
        data = cipher.decrypt(ciphertext) # This is intentional, if the key is incorrect, write invalid data to it
        # Note: decrypt doesn't remove padding? This might be a dealbreaker

    # Assuming we're writing to user's current working directory
    with save_path.open("wb") as d:
        d.write(data)

    if DEBUG:
        # Checking for authenticity, DEBUG USE ONLY
        try:
            cipher.verify(tag)
            print("Message decryption success")
        except:
            print("Message decryption failed")
            dbg_in = input("Remove garbage file? [Y/n]: ").strip().lower()
            if dbg_in == "y":
                save_path.unlink()
                print("File removed")

def main():
    # Encrypted data
    encrypted_file = Path(__file__).resolve().with_name("BODY")
    # Mode file MEI/Encryption_Mode, contains what environment parameters to use in the AES's key generation
    mode_file = Path(__file__).resolve().with_name("Encryption_Mode")
    # Original filename
    filename_file = Path(__file__).resolve().with_name("Original_Filename") # A file containing the encrypted body's filename
    # since the data is named "BODY", we need another way to put filename into it. I botched this thing in.
    
    # Read encryption mode (environment parameters to use)
    with mode_file.open("r") as em:
        encryption_mode = em.read().strip()

    # Read filename, set save path to Current working directory
    with filename_file.open() as fn:
        filename = fn.read().strip()
        save_file_path = Path.cwd() / filename

    # Decrypt the files
    decrypt_file(encrypted_file, save_file_path, encryption_mode)

if __name__ == "__main__":
    if DEBUG:
        print(os.getcwd())
        input("Press [Enter] to start extraction process...")
        print("Warning: debug code enabled")
    main()