# Prepare files, set paths

import platform, urllib.request, ssl
from globals import VERSION, ARCH
from errors import error_handler

def update(current_version):
    version_url = "https://raw.githubusercontent.com/BlitzPythoner/AMBCT-Linux/main/version.txt"

    try:
        with urllib.request.urlopen(version_url, timeout=5) as response:
            online_version = response.read().decode().strip()
    except Exception:
        try:
            context = ssl._create_unverified_context()
            with urllib.request.urlopen(version_url, context=context, timeout=5) as response:
                online_version = response.read().decode().strip()
        except Exception:
            error_handler(3)
            return 4, None

    local = current_version
    remote = float(online_version.strip())

    if local < remote:
        return 1, online_version
    elif local > remote:
        return 3, None
    else:
        return 2, None  

def load():
    print("\nChecking Architecture...\n")
    arch = platform.machine()
    if not str(ARCH) in arch:
        error_handler(1)

    wimlib_path = "wimlib-imagex"
    print("Files were successfully loaded!\n")
    
    print("Checking for updates...\n")
    upd_code, version = update(VERSION)

    return upd_code, wimlib_path, version
