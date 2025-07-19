#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "click",
#     "opencc",
# ]
# ///

import os
import re

import click
import opencc

def clean_folder_names(directory, dry_run):
    pattern = r"【[^【】]*?(www\.[^【】]*?)】"  # 專門移除帶有 www. 的廣告資訊
    renamed_count = 0

    for folder_name in os.listdir(directory):
        old_path = os.path.join(directory, folder_name)
        if os.path.isdir(old_path):
            new_name = re.sub(pattern, '', folder_name).strip()
            # Convert Simplified Chinese to Traditional Chinese
            converter = opencc.OpenCC('s2t')
            new_name = converter.convert(new_name)
            new_path = os.path.join(directory, new_name)
            if old_path != new_path:
                if dry_run:
                    print(f"[Dry Run] Would rename: '{folder_name}'\n  -> '{new_name}'\n")
                else:
                    os.rename(old_path, new_path)
                    print(f"Renamed: '{folder_name}'\n  -> '{new_name}'\n")
                renamed_count += 1

    print(f"\nTotal folders renamed: {renamed_count}")


def remove_ad_files(directory, dry_run):
    """Remove files matching ad patterns and size constraints."""
    ad_patterns = [
        r"【[^【】]*?(www\.[^【】]*?)】.*",  # Matches files with 【...www...】 in the name
        r".*（www\.[^）]*?）.*",  # Matches files with （www...） in the name
        r".*www\\.[^ ]*.*",  # Matches files with www... in the name
        r"Downloaded from www\.[^ ]* ?\.txt",
        # Matches files like 'Downloaded from www.ETTV.tv .txt'
        r"\[.*\]Downloaded from [^ ]* ?\.txt",
        # Matches files like '[TGx]Downloaded from torrentgalaxy.to .txt'
        r"NEW upcoming releases by .*\.txt",
        # Matches files like 'NEW upcoming releases by Xclusive.txt'
        r"Torrent Downloaded From ExtraTorrent\.cc\.txt",
        # Matches files like 'Torrent Downloaded From ExtraTorrent.cc.txt'
    ]
    max_size = 5 * 1024 * 1024  # 5 MB in bytes
    removed_count = 0
    removed_files = []

    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if os.path.isfile(file_path) and os.path.getsize(file_path) < max_size:
                if any(re.match(pattern, file_name) for pattern in ad_patterns):
                    if dry_run:
                        print(f"[Dry Run] Would remove: '{file_path}'")
                    else:
                        os.remove(file_path)
                        print(f"Removed: '{file_path}'")
                        removed_files.append(file_path)
                    removed_count += 1

    print(f"\nTotal files removed: {removed_count}")
    if removed_files:
        print("\nList of removed files:")
        for removed_file in removed_files:
            print(removed_file)


@click.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False))
@click.option(
    '--dry-run', is_flag=True, help="Perform a dry run without renaming folders or removing files."
)
def cli(directory, dry_run):
    """CLI tool to clean folder names and remove ad files in the specified directory."""
    clean_folder_names(directory, dry_run)
    print("\n" + "=" * 40 + "\n")  # Separator between rename and remove
    remove_ad_files(directory, dry_run)


if __name__ == '__main__':
    cli()
