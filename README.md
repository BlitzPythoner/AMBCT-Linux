# AMBCT – Automatic Manual Backup Creation Tool (Linux)

- **Author:** BlitzPythoner
- **Version:** v1.0
- **Platform:** Linux
- **Language:** Python

---

## Overview

AMBCT is a command-line backup tool for Linux that uses `wimlib-imagex` to create `.wim` backup images from drives or directories.

This version represents the current state of the Linux implementation. Additional functionality from the Windows version will be adapted and integrated in a Linux-compatible way.

---

## Features (current)

* Create backups of:

  * entire drives
  * custom directories
* Uses `wimlib-imagex` for `.wim` image creation
* Compression methods:

  * `NONE`
  * `XPRESS`
  * `LZX`
  * `LZMS`
* Progress output with percentage and ETA
* Optional integrity check (`--check`)
* Optional system shutdown after completion
* Pre-execution summary and validation

---

## Installation

```bash
curl -fsSL https://blitzpythoner.github.io/AMBCT-Linux-Repo/install.sh | sudo bash
```

---

## Requirements

* Linux system
* Python 3.10 or newer recommended
* Compatible with Python 3.6+
* `wimlib-imagex` must be available in PATH

---

## Usage

```bash
ambct
```

The program runs as an interactive CLI.

---

## Notes

* Performance depends on system hardware (CPU, storage speed)
* Large backups may take significant time
* Ensure sufficient free space on the target location

---

## Development Status

The Linux version is under active development.

The current release focuses on core backup functionality.
Additional features from the Windows version will be implemented step by step, adapted to Linux-specific behavior and requirements.

---

## Differences to Windows Version

* No Windows-specific features (e.g. VSS)
* No benchmarking system
* Feature set is currently reduced

---

## Dependencies

* `wimlib-imagex`
  https://wimlib.net/

---

## Author

BlitzPythoner

---

## Disclaimer

This software is provided without warranty. Use at your own risk.
