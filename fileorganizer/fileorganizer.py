import os
import shutil

def rename_file(source_dir, old_name, new_name):
    """
    Renames a file in the specified directory.

    Args:
    - source_dir (str): The path of the directory containing the file to be renamed.
    - old_name (str): The current name of the file.
    - new_name (str): The new name for the file.
    """
    old_path = os.path.join(source_dir, old_name)
    new_path = os.path.join(source_dir, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"File '{old_name}' renamed to '{new_name}'")
    else:
        print(f"File '{old_name}' not found.")

def delete_item(directory, item_name):
    """
    Deletes a file or folder from the specified directory.

    Args:
    - directory (str): The path of the directory containing the item to be deleted.
    - item_name (str): The name of the item to be deleted.
    """
    item_path = os.path.join(directory, item_name)
    if os.path.exists(item_path):
        if os.path.isfile(item_path):
            os.remove(item_path)
            print(f"File '{item_name}' deleted.")
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
            print(f"Folder '{item_name}' deleted.")
    else:
        print(f"Item '{item_name}' not found.")
        

def create_folder(directory, folder_name):
    """
    Creates a new folder/directory.

    Args:
    - directory (str): The path of the directory where the new folder will be created.
    - folder_name (str): The name of the new folder.
    """
    new_folder_path = os.path.join(directory, folder_name)
    os.makedirs(new_folder_path, exist_ok=True)
    print(f"Folder '{folder_name}' created at '{directory}'")
    
def create_file(directory, file_name):
    """
    Creates a new file in the specified directory.

    Args:
    - directory (str): The path of the directory where the new file will be created.
    - file_name (str): The name of the new file.
    """
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'w') as file:
        pass  # The 'pass' statement is used as a placeholder to do nothing inside the 'with' block
    print(f"File '{file_name}' created at '{directory}'")
    

def list_all_contents(directory):
    """
    Lists all contents (files and folders) in the specified directory.

    Args:
    - directory (str): The path of the directory.
    """
    print("Contents of the directory:")
    for item in os.listdir(directory):
        print(item)
        
# Example usage
source_directory = "D:/python"
rename_file(source_directory, "rupesh.py", "hello.txt")
delete_item(source_directory, "hello.mp4")
create_folder(source_directory, "hello.py")
create_file(source_directory,"hello.mp4")
list_all_contents(source_directory)
