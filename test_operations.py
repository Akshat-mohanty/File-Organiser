import os
from file_organizer.operations import organize_files, rename_files

# Setup files
os.makedirs("test_dir", exist_ok=True)
open("test_dir/pic1.jpg", "w").close()
open("test_dir/pic2.png", "w").close()
open("test_dir/doc1.pdf", "w").close()
open("test_dir/script.py", "w").close()

print("Initial files in test_dir:", os.listdir("test_dir"))

print("\n--- Testing organize_files ---")
organize_files("test_dir")
print("Folders created:", os.listdir("test_dir"))
if os.path.exists("test_dir/Images"):
    print("Files in Images:", os.listdir("test_dir/Images"))

print("\n--- Testing rename_files ---")
# create test file to rename
open("test_dir/old_pattern_file.txt", "w").close()
rename_files("test_dir", "old_pattern", "new_pattern")
print("Files in test_dir:", os.listdir("test_dir"))

