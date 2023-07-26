import os
import shutil

def organize_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for root, _, files in os.walk(source_folder):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1][1:]  # File extension without the dot
                destination_path = os.path.join(destination_folder, file_extension)

                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)

                try:
                    shutil.move(file_path, os.path.join(destination_path, filename))
                    print(f"Moved '{filename}' to '{destination_path}'")
                except shutil.Error:
                    print(f"Error moving '{filename}' to '{destination_path}'")

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

    organize_files(source_folder, destination_folder)
