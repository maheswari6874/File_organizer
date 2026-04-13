# Python File Organizer

This project automatically organizes files in a folder (like Downloads) into categories such as Images, Videos, Documents, and Others.

## Features

- Reads all files in a specified folder
- Identifies file types by extension
- Moves files into appropriate subfolders automatically

## File Categories

- **Images**: .jpg, .jpeg, .png, .gif
- **Videos**: .mp4, .mkv, .avi
- **Documents**: .pdf, .docx, .txt
- **Audio**: .mp3, .wav

## Usage

1. Create a folder called `test_folder` in the same directory as the script.
2. Place files you want to organize inside `test_folder`.
3. Run the script:

```bash
python file_organizer.py
```

The script will move files into subfolders based on their extensions.

## Example

Before:
```
test_folder/
photo.jpg
movie.mp4
notes.pdf
song.mp3
```

After:
```
test_folder/
Images/photo.jpg
Videos/movie.mp4
Documents/notes.pdf
Audio/song.mp3
```

## Troubleshooting

- Ensure the `test_folder` exists and contains files.
- The script only processes files with extensions listed in `file_types`.
- Files without matching extensions remain in the root folder.
- Run the script from the directory containing `file_organizer.py`.