# Main Code for AMBCT

import os, time, webbrowser

from load import load
from globals import VERSION, normalize_path
from errors import error_handler
from drive import select_backup_drive, select_save_drive
from storage import check_storage
from options import c_select_options
from pre_create import c_pre_create_backup
from core import create_backup
from thanks import thanks

def main():
    os.system("clear")
    print(f"=== Automatic Manual Backup Creation Tool for Linux v{VERSION} === \n")
    print("Welcome to AMBCT. What do you want to do?\n")
    print("[1] Create a new backup")
    print("[/] More will be soon!\n")
    if update == 1:
        print("[U] Visit website for update\n")
        print(f"A newer version of AMBCT is available. Current version: {VERSION}, Latest version: v{version}\n")
    if update == 2:
        print("You are using the newest version.\n")
    if update == 3:
        print("This version is currently under development.\n")
    if update == 4:
        print("It was not possible to check for updates.\n")
    print("[X] Exit AMBCT\n")

    while True:
        choice = input("Choose an option for what you'd like to do: ").lower()

        if choice == "1":
            # Create backup
            backup_path, backup_size, DRIVE = select_backup_drive()
            target_path, target_available_space = select_save_drive()
            storage_index = check_storage(backup_size, target_available_space, backup_path[0])
            compression, backup_name, CHECK, SHUTDOWN = c_select_options(storage_index)
            c_pre_create_backup(backup_path, backup_size, DRIVE, target_path, target_available_space, compression, backup_name, CHECK, SHUTDOWN)
            create_backup(wimlib_path, normalize_path(backup_path), normalize_path(target_path), compression, backup_name, CHECK, SHUTDOWN)
            thanks()

        elif choice == "u" and update == 1:
            webbrowser.open("https://github.com/BlitzPythoner/AMBCT/releases/latest")
            return main()
        
        elif choice == "x":
            error_handler(-1)
        else:
            print("Please select one of the options listed above.\n")
            time.sleep(2)
            continue

update, wimlib_path, version = load()
main()