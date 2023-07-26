# FileOrganizerPy

FileOrganizerPy is a Python script that helps you organize your files by moving or copying them from a source folder to a destination folder based on their file extensions. It categorizes files into predefined categories like Documents, Images, Videos, and Music. If the file extension doesn't match any predefined categories, it will be placed in the "Others" category.

## Prerequisites

Before running the script, ensure you have the following:

- Python installed on your system (Python 3.x recommended).
- Basic familiarity with using the command line (Terminal or Command Prompt).

## How to Use

1. Clone this repository to your local machine or download the `file_organizer.py` script directly.

2. Open your terminal or command prompt and navigate to the folder containing the `file_organizer.py` script.

3. Run the script by executing the following command:

```bash
python file_organizer.py
```

4. The script will prompt you for the source folder, destination folder, and some other preferences to organize your files.

5. Enter the paths for the source and destination folders when prompted. For example:

   ```
   Example Paths:
   Windows Source folder: C:\Users\Username\Documents\source_folder
   Windows Destination folder: D:\Backup\destination_folder
   Linux Source folder: /home/username/source_folder
   Linux Destination folder: /mnt/backup/destination_folder
   Note: Please replace the example paths with your desired paths.
   ```

6. Choose whether you want to copy the files instead of moving them by typing `yes` or `no`.

7. Choose whether you want to sort the files by categories by typing `yes` or `no`.

8. The script will start organizing the files and display the progress on the console. Files will be moved or copied to the appropriate subfolders within the destination folder.

9. At the end of the process, the script will show a summary of the files organized and any errors encountered.

10. Optionally, the script will ask if you want to save the summary in a `.log` file.

## GUI Edition

A graphical user interface (GUI) edition of FileOrganizerPy is available, allowing users to interact with the application through an easy-to-use interface. To use the GUI edition, run the `file_organizer_gui.py` script instead of the command-line version. The GUI version offers the same functionality as the command-line version but provides a more user-friendly experience.

## File Categories

The script automatically categorizes files into the following categories based on their extensions:

- **Documents**: txt, pdf, doc, docx, xls, xlsx, ppt, pptx
- **Images**: jpg, jpeg, png, gif, bmp
- **Videos**: mp4, avi, mkv, mov, wmv
- **Music**: mp3, ogg, wav, flac

If a file's extension does not match any of the above categories, it will be placed in the "Others" category.

## Notes

- Please make sure to replace the example paths with your desired paths.
- Take a backup of your files before running the script, especially if you're using the move option. The script will move files from the source folder, and there is no undo option.
- Always run the script in the folder where the `file_organizer.py` or `file_organizer_gui.py` script is located.
- Use the script responsibly and verify the results after organization.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE) (GPL-3.0). Feel free to modify and distribute it as per the terms of the license.

---

Happy organizing! If you have any questions or encounter any issues, please feel free to [create an issue](https://github.com/PawiX25/FileOrganizerPy/issues) in the repository.
