import os, sys

from globals import VERSION

def thanks():
    os.system("clear")
    input(f"Thank you for using this program The Automatic Manual Backup Creation Tool to create or append a backup.\nAMBCT for Linux v{VERSION} - by BlitzPythoner.\n\nPress any key to close the program...")
    sys.exit(0)