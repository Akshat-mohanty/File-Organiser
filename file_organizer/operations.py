import os
import shutil
from pathlib import Path
from typing import Dict, List

# Define a mapping from categories to file extensions
CATEGORY_MAP: Dict[str, List[str]] = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".csv", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Code": [".py", ".java", ".cpp", ".c", ".js", ".html", ".css", ".json", ".xml"],
}

def get_category(extension: str) -> str:
    """Return the appropriate category for a given file extension."""
    extension = extension.lower()
    for category, extensions in CATEGORY_MAP.items():
        if extension in extensions:
            return category
    return "Others"

def organize_files(directory: str) -> None:
    """Organize files in the specified directory into subfolders based on extension."""
    target_dir = Path(directory)
    if not target_dir.is_dir():
        raise ValueError(f"'{directory}' is not a valid directory.")

    moved_files_count = 0

    for file_path in target_dir.iterdir():
        # Only process files, skip directories
        if file_path.is_file():
            category = get_category(file_path.suffix)
            category_dir = target_dir / category

            # Create category directory if it doesn't exist
            category_dir.mkdir(exist_ok=True)

            # Move the file
            destination = category_dir / file_path.name
            shutil.move(str(file_path), str(destination))
            moved_files_count += 1
            print(f"Moved: {file_path.name} -> {category}/")
            
    print(f"\nSuccessfully organized {moved_files_count} files in '{directory}'.")

def rename_files(directory: str, pattern: str, replacement: str) -> None:
    """Rename files in the specified directory by replacing pattern with replacement."""
    target_dir = Path(directory)
    if not target_dir.is_dir():
        raise ValueError(f"'{directory}' is not a valid directory.")

    renamed_files_count = 0

    for file_path in target_dir.iterdir():
        if file_path.is_file() and pattern in file_path.name:
            new_name = file_path.name.replace(pattern, replacement)
            new_file_path = target_dir / new_name
            
            # Avoid overwriting if a file with the new name already exists
            if new_file_path.exists():
                print(f"Warning: Cannot rename {file_path.name} to {new_name} (file exists). Skipping.")
                continue

            file_path.rename(new_file_path)
            renamed_files_count += 1
            print(f"Renamed: {file_path.name} -> {new_name}")

    print(f"\nSuccessfully renamed {renamed_files_count} files in '{directory}'.")
