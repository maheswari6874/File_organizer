import os
import shutil

# Path of the folder you want to organize
path = "test_folder"

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"]
}

def list_root_files(base_path):
    files = [f for f in os.listdir(base_path) if os.path.isfile(os.path.join(base_path, f))]
    if files:
        print("Files in {}:".format(base_path))
        for f in files:
            print("  - {}".format(f))
    else:
        print("No files found in {}.".format(base_path))
    print()

print("Before organizing:")
list_root_files(path)

moved_count = 0
for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1].lower()

        for folder, extensions in file_types.items():
            if ext in extensions:
                folder_path = os.path.join(path, folder)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(file_path, os.path.join(folder_path, file))
                print("Moved {} to {}".format(file, folder))
                moved_count += 1
                break

print()
print("After organizing:")
list_root_files(path)

if moved_count == 0:
    print("No files were moved. Either the folder has no matching files or it is already organized.")
else:
    print("Done. {} file(s) moved.".format(moved_count))