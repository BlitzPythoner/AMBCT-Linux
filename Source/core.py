import os, time, sys, subprocess, re

from globals import show_progressbar
from errors import error_handler

def create_backup(wimlib_path, backup_path, target_path, compression, backup_name, CHECK, SHUTDOWN):
    os.system("clear")

    output_file = os.path.join(target_path, f"{backup_name}.wim")
    args = [
        wimlib_path, "capture",
        backup_path,
        output_file,
        f"{backup_name}",
        f"--compress={compression.lower()}",
    ]
    if CHECK:
        args.append("--check")

    print("=== CREATING BACKUP ===\n")

    start_time = time.time()

    phase = None

    process = subprocess.Popen(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        encoding="utf-8",
        errors="ignore"
    )

    try:
        for raw_line in process.stdout:
            line = raw_line.strip()

            if "scanned" in line and "Archiving" not in line:
                if phase != "scan":
                    print(f"Scanning \"{backup_path}\"...")
                    phase = "scan"
                match = re.search(r"([\d\.]+)\s+([KMGT]i?B)\s+scanned", line)
                if match:
                    scanned_value = match.group(1)
                    scanned_unit = match.group(2)
                    sys.stdout.write(f"\rScanned: {scanned_value} {scanned_unit}... ")
                    sys.stdout.flush()
                continue

            if "Archiving file data:" in line:
                if phase != "backup":
                    print(f"\n\nSaving Backup in \"{target_path}\"... This can take a while!\n")
                    phase = "backup"

                match = re.search(r"Archiving file data:.*?\((\d+)%\)", line, re.IGNORECASE)
                if match:
                    percent = int(match.group(1))
                    show_progressbar(percent)
                continue

            if "Calculating integrity table" in line or "Verifying" in line:
                if phase != "check":
                    print("\n\nVerifying backup integrity...\n")
                    phase = "check"
                match = re.search(r"\((\d+)%\)", line)
                if match:
                    percent = int(match.group(1))
                    show_progressbar(percent)
                continue

        process.wait()
        total_time = time.time() - start_time
        mins, secs = divmod(int(total_time), 60)

        if process.returncode == 0:
            print(f"\n\nBackup completed successfully. Total time: {mins}m {secs:02d}s")
            if SHUTDOWN:
                print("System will shutdown in 10 seconds...")
                os.system("sleep 10 && shutdown -h now")

            input("\nBackup was created successfully, press Enter to continue!")
            return True
        else:
            print(f"[DEBUG]: Code: {process.returncode}\nArgs: {args}")
            error_handler(7)

    except KeyboardInterrupt:
        process.terminate()
        error_handler(-1)

    except Exception as e:
        process.terminate()
        error_handler(8)


