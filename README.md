# Toolbox

A collection of utility scripts for various tasks. This repository contains scripts written in Fish shell and Python to automate and simplify common operations.

## Scripts Overview

### 1. `rename_ani_gamer_episodes.fish`

**Description:**
Renames `.mp4` files in a specified directory by extracting episode numbers from filenames and formatting them as `eXXX.mp4` (e.g., `e001.mp4`).

**Usage:**
```fish
./rename_ani_gamer_episodes.fish [folder]
```
If no folder is specified, the current directory is used.

---

### 2. `clean_ads_and_convert_zh.py`

**Description:**
- Cleans folder names by removing advertisement patterns and converting Simplified Chinese to Traditional Chinese.
- Removes ad-related files smaller than 5 MB based on specific patterns.

**Dependencies:**
- Python 3.13+
- `click`
- `opencc`

**Usage:**
```bash
python clean_ads_and_convert_zh.py <directory> [--dry-run]
```
- `<directory>`: The target directory to process.
- `--dry-run`: Simulates the operations without making changes.

---

### 3. `link-to-bin.fish`

**Description:**
Creates symlinks for all `.sh`, `.bash`, `.fish`, and `.py` scripts in the current directory to `~/bin`, removing their extensions.

**Usage:**
```fish
./link-to-bin.fish
```

---

## Setup

### Adding `~/bin` to PATH
Ensure `~/bin` is in your PATH to use the symlinked scripts:
```bash
echo 'set PATH ~/bin $PATH' >> ~/.config/fish/config.fish
source ~/.config/fish/config.fish
```

---

## License
This project is licensed under the MIT License.
