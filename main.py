import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


source = "/Users/muralikrishnan/Downloads"
document_destination = ""
image_destination = ""
zip_destination = ""
dmg_destination = ""

doument_extension = ['.pdf', '.docx', ',xls', '.xlsx', '.ppt', '.pptx']
image_extension = ['.jpg', '.jpeg', '.png', '.tiff', '.webp']
zip_extension = ['.zip', '.tar.gz']


with os.scandir(source) as items:
    for item in items:
        print(item.name)