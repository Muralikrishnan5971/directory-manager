import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


source = "/Users/muralikrishnan/Downloads"
document = "/Users/muralikrishnan/Downloads/document/"
image = "/Users/muralikrishnan/Downloads/image/"
archive = "/Users/muralikrishnan/Downloads/archive/"

extension = {
"document":['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'py'],
"image":['jpg', 'jpeg', 'png', 'tiff', 'webp', 'gif'],
"archive":['zip', 'tar', 'gz', 'pkg', 'dmg', 'app']
}

# assign destination location based on the destination type
def select_destination_folder(dest_type):
    
    if dest_type == "document":
        dest_type = document
    elif dest_type == "image":
        dest_type = image
    elif dest_type == "archive":
        dest_type = archive
    else:
        pass
    return dest_type

def move_file(source, dest):
    if dest == None:
        pass
    else:
        try:
            print("Moving: ", source, "to ", dest)
            # shutil.move(source, dest)
        except FileNotFoundError: 
            print ('File Not Found') 
        
# find destination folder based on file extension
def find_dest_folder(file_ext):
    for key in list(extension.keys()):
        for ext in extension[key]:
            if ext == file_ext:
                return key
        

# # class MoveHandler(FileSystemEventHandler):
    
def on_modified():
    with os.scandir(source) as files:
        for file in files:
            filename = file.name.split(".")
            file_ext = filename[-1].lower()
            dest_type = find_dest_folder(file_ext)
            source_filepath = source + "/" + file.name
            dest_filepath = select_destination_folder(dest_type)

            # print("Moving: ", source_filepath, "to ", dest_filepath)
            move_file(source_filepath, dest_filepath)
  
on_modified()
