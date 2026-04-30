import sys

def error_handler(code):
    if code == -1: # User-initiated program closure
        sys.exit(-1)
    if code == 1: # Serious error
        input("\nError 1: The architecture of this program does not match that of your processor. Please download the correct version of this program.\nPlease press any key to exit this program...")
        sys.exit(1)
    elif code == 2: # Serious error
        input("\nError 2: The files required for this program were not found. Please reinstall this program.\nPlease press any key to exit this program...")
        sys.exit(2)
    elif code == 3: # Minor error
        input("\nError 3: An internet connection could not be established to check for updates.\nPress any key continue anyway...")
        return
    elif code == 4: # Moderate error
        input("\nError 4: No drives were detected. Please connect a drive and restart the program. \nPress any key to close the program...")
        sys.exit(4)
    elif code == 5: # Special case: The error message is displayed in `check_storage()` for illustrative purposes.
        sys.exit(5)
    elif code == 6: # Minor error
        input("\nError 6: An error occurred while measuring the speed of your target drive. \nPress any key to skip this measurement...")
        return
    elif code == 7: # Moderate error
        input("\nError 7: The backup failed. Please restart the program, and if you encounter any further issues, please report them on my GitHub page. \nPress any key to close this program...")
        sys.exit(7)
    elif code == 8: # Moderate error
        input("\nError 8: An unexpected error occurred while creating or appending the backup. See the log for more information. \nPress any key to exit the program...")
        sys.exit(8)


        