# Using PyInstaller in order to package the encryption file and making it self-extractable

import PyInstaller.__main__
from pathlib import Path
import os
import shutil

def main():
    # Basically invoke PyInstaller commandline interface lmao
    # PyInstaller doesn't really have an API interface

    # Just in case, set the CWD to where the script is
    os.chdir(Path(__file__).parent.absolute())

    body_filename = input("Enter encrypted file path/filename: ")

    # We need three files/things to make the package
    # Encrypted file (BODY)
    # Encryption mode (Encryption_Mode) to store which environment parameters were used in order to encrypt the data
    # Original filename (Originak_Filename) to store the name of the decrypted file

    body_file = Path(body_filename) # Created by Encryption.py

    if not body_file.exists():
        print("Error: encrypted file does not exist, committing unalive lmao")
        print(body_file.absolute())
        exit(1)

    encryption_mode_file = Path("Encryption_Mode") # Created by Pattern_Storage.py, invoked automatically by Encryption.py
    filename_file = Path("Original_Filename") # a file to store the encrypted file's original name
    # something like storing encryption mode/environment parameters to use in Encryption_Mode file

    # The only missing piece is filename_file, this script will take care of it
    with filename_file.open("w") as fp:
        fp.write(body_file.stem)

    # Renaming whatever encrypted file to "BODY" to prepare for PyInstaller packaging
    body_file = body_file.rename("BODY")

    # BODY, Encryption_Mode, Original_Filename in place, start packaging
    PyInstaller.__main__.run([
        'PackageDecryptRoutine.py',
        '--onefile',
        '--add-data', 'BODY:.',
        '--add-data', 'Encryption_Mode:.',
        '--add-data', 'Original_Filename:.'
    ])

    print("Cleaning up...")
    shutil.rmtree("__pycache__")
    shutil.rmtree("build")
    body_file.unlink()
    encryption_mode_file.unlink()
    filename_file.unlink()    
    Path("temp.tmp").unlink()
    Path("PackageDecryptRoutine.spec").unlink()

if __name__ == "__main__":
    main()