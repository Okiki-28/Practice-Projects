import os
import re
from pathlib import Path

path = Path.home() / "Documents"
target_path = r'C:\Users\olume\Documents\Moved Downloads'

def get_folder(ext):
    
    text_files = [".txt", ".pdf", ".odt", ".rtf"]
    office_files = [".pptm", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods", ".odp"]
    image_files = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"]
    audio_files = [".mp3", ".wav", ".aac", ".flac", ".ogg"]
    video_files = [".mp4", ".mkv", ".avi", ".mov", ".wmv"]
    compressed_files = [".zip", ".rar", ".7z", ".tar.gz"]
    executable_and_script_files = [".bat", ".sh", ".py", ".jar"]
    web_files = [".html", ".htm", ".css", ".js", ".php", ".json"]
    database_files = [".sql", ".db", ".sqlite", ".csv", ".xls", ".xlsx"]
    application_files = [".exe", ".msi", ".bat", ".sh", ".jar", ".apk", ".app", ".dmg", ".iso", ".deb", ".rpm"]


    if ext in text_files:
        return "Text Documents"
    elif ext in office_files:
        return "Office files"
    elif ext in image_files:
        return "Image"
    elif ext in audio_files:
        return "Audio"
    elif ext in video_files:
        return "Video"
    elif ext in compressed_files:
        return "Compressed files"
    elif ext in executable_and_script_files:
        return "Scripts"
    elif ext in web_files:
        return "Web docs"
    elif ext in database_files:
        return "Database_files"
    elif ext in application_files:
        return "Applications"
    else:
        return False

def folder():
    arr = ["Desktop", "Documents", "Downloads"]
    #Choosing Path
    for a in range(len(arr)):
        print(a+1, arr[a])
    i = input("Choose folder you wish to sort files [1-3]: ")
    while True:
        if not i.isdigit():
            print("Invalid")
            i = input("Choose again: ")
            continue
        elif not 1 <= int(i) <= len(arr):
            print("Invalid")
            i = input("Choose again: ")
            continue
        break
    i = int(i)-1
    path = Path.home() / arr[i]
    print(f"Initial path: {path}")

    #Choosing Destination
    home= input("Enter name of folder to store document files: ")
    i1 = input("Choose home folder from list above to store this [1-3]: ")
    while True:
        if not i1.isdigit():
            print("Invalid")
            i1 = input("Choose again: ")
            continue
        elif not 1 <= int(i1) <= len(arr):
            print("Invalid")
            i1 = input("Choose again: ")
            continue
        break
    i1 = int(i1)-1
    target_path = os.path.join(Path.home(), arr[i1], home)
    print(f"Target Path: {target_path}")

    files = os.listdir(path)

    for file in files:
        match = re.search(r'\.([a-zA-Z0-9]{1,10})$', file)
        if match:
            i = match.span()
            ext = file[i[0]:i[1]]
            folder_name = get_folder(ext)
            if not folder_name:
                print('>>', ext, file)
                print()
                continue

            old_path = os.path.join(path, file)
            new_folder = os.path.join(target_path, folder_name)
            new_path = os.path.join(new_folder, file)

            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
                print("New folder created!\n")
            else:
                print("Folder exists!\n")

            print(old_path, '>>', new_path)
            os.rename(old_path, new_path)
        
folder()
