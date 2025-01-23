import os
import re

path = r'C:\Users\olume\Downloads'
target_path = r'C:\Users\olume\Documents\Moved Downloads'

def get_folder(ext):
    text_files = [".txt", ".pdf", ".odt", ".rtf"]
    office_files = [".pptm", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods", ".odp"]
    image_files = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"]
    audio_files = [".mp3", ".wav", ".aac", ".flac", ".ogg"]
    video_files = [".mp4", ".mkv", ".avi", ".mov", ".wmv"]
    compressed_files = [".zip", ".rar", ".7z", ".tar.gz"]
    executable_and_script_files = [".exe", ".bat", ".sh", ".py", ".jar"]
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

def folder(path, target_path):
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

            print(old_path, '>>', new_path)
            os.rename(old_path, new_path)
        
folder(path, target_path)
