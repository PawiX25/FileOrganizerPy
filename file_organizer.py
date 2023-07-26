import os
import shutil

def organize_files(source_folder, destination_folder, move_files=True):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for root, _, files in os.walk(source_folder):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1][1:]  # Get the file extension without the dot
                destination_path = os.path.join(destination_folder, file_extension)

                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)

                try:
                    if move_files:
                        shutil.move(file_path, os.path.join(destination_path, filename))
                        print(f"Moved '{filename}' to '{destination_path}'")
                    else:
                        shutil.copy2(file_path, os.path.join(destination_path, filename))
                        print(f"Copied '{filename}' to '{destination_path}'")
                except shutil.Error:
                    print(f"Error processing '{filename}'")

if __name__ == "__main__":
    print("Example Paths:")
    print("Windows Source folder: C:\\Users\\Username\\Documents\\source_folder")
    print("Windows Destination folder: D:\\Backup\\destination_folder")
    print("Linux Source folder: /home/username/source_folder")
    print("Linux Destination folder: /mnt/backup/destination_folder")
    print("Note: Please replace the example paths with your desired paths.")

    use_current_directory = input("Do you want to use the current directory as the source folder? (yes/no): ").lower()
    if use_current_directory == "yes":
        source_folder = os.getcwd()  # Set the current working directory as the source folder
    else:
        source_folder = input("Enter the source folder path: ")

    destination_folder = input("Enter the destination folder path: ")
    
    copy_files = input("Do you want to copy the files instead of moving them? (yes/no): ").lower()

    if copy_files == "yes":
        move_files = False
    else:
        move_files = True

    organize_files(source_folder, destination_folder, move_files)
