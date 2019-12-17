from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time
import StringHandle

class Hello(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            File_format = StringHandle.StringHandler.extention(filename)
            Tag = StringHandle.StringHandler.tag(filename)
            if Tag != "No Tag Found":
                new_destination = tag_folders[Tag] + "/" + ext_folders[File_format] + "/" + filename
            else:
                new_destination = extensions_folders[File_format] + "/" + filename
            print(File_format)
            src = folder_to_track + "/" + filename
            print(new_destination)
            os.rename(src, new_destination)
            print(filename)

tag_folders = {
    'Math' : "/Users/Personal/Desktop/Don't Look/Documents/Matemáticas"
}
ext_folders = {
    '.pdf' : "PDF"
}
extensions_folders = {
#No name
    'noname' : "/Users/kalle/Desktop/kalle/Other/Uncategorized",
#Audio
    '.aif' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.cda' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.mid' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.midi' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.mp3' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.mpa' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.ogg' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.wav' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.wma' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.wpl' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.m3u' : "/Users/kalle/Desktop/kalle/Media/Audio",
#Video C:\Users\Personal\Desktop\Don't Look\Movies
    '.3g2': "/Users/Personal/Desktop/Don't Look/Movies",
    '.3gp': "/Users/Personal/Desktop/Don't Look/Movies",
    '.avi': "/Users/Personal/Desktop/Don't Look/Movies",
    '.flv': "/Users/Personal/Desktop/Don't Look/Movies",
    '.h264': "/Users/Personal/Desktop/Don't Look/Movies",
    '.m4v': "/Users/Personal/Desktop/Don't Look/Movies",
    '.mkv': "/Users/Personal/Desktop/Don't Look/Movies",
    '.mov': "/Users/Personal/Desktop/Don't Look/Movies",
    '.mp4': "/Users/Personal/Desktop/Don't Look/Movies",
    '.mpg': "/Users/Personal/Desktop/Don't Look/Movies",
    '.mpeg': "/Users/Personal/Desktop/Don't Look/Movies",
    '.rm': "/Users/Personal/Desktop/Don't Look/Movies",
    '.swf': "/Users/Personal/Desktop/Don't Look/Movies",
    '.vob': "/Users/Personal/Desktop/Don't Look/Movies",
    '.wmv': "/Users/Personal/Desktop/Don't Look/Movies",
#Images C:\Users\Personal\Desktop\Don't Look\Images
    '.ai': "/Users/Personal/Desktop/Don't Look/Images",
    '.bmp': "/Users/Personal/Desktop/Don't Look/Images",
    '.gif': "/Users/Personal/Desktop/Don't Look/Images",
    '.ico': "/Users/Personal/Desktop/Don't Look/Images",
    '.jpg': "/Users/Personal/Desktop/Don't Look/Images",
    '.jpeg': "/Users/Personal/Desktop/Don't Look/Images",
    '.png': "/Users/Personal/Desktop/Don't Look/Images",
    '.ps': "/Users/Personal/Desktop/Don't Look/Images",
    '.psd': "/Users/Personal/Desktop/Don't Look/Images",
    '.svg': "/Users/Personal/Desktop/Don't Look/Images",
    '.tif': "/Users/Personal/Desktop/Don't Look/Images",
    '.tiff': "/Users/Personal/Desktop/Don't Look/Images",
    '.CR2': "/Users/Personal/Desktop/Don't Look/Images",
#Internet
    '.asp': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.aspx': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.cer': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.cfm': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.cgi': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.pl': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.css': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.htm': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.js': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.jsp': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.part': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.php': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.rss': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.xhtml': "/Users/kalle/Desktop/kalle/Other/Internet",
#Compressed
    '.7z': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.arj': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.deb': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.pkg': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.rar': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.rpm': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.tar.gz': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.z': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.zip': "/Users/kalle/Desktop/kalle/Other/Compressed",
#Executables C:\Users\Personal\Desktop\Don't Look\Executables
    '.apk': "/Users/Personal/Desktop/Don't Look/Executables",
    '.bat': "/Users/Personal/Desktop/Don't Look/Executables",
    '.com': "/Users/Personal/Desktop/Don't Look/Executables",
    '.exe': "/Users/Personal/Desktop/Don't Look/Executables",
    '.gadget': "/Users/Personal/Desktop/Don't Look/Executables",
    '.jar': "/Users/Personal/Desktop/Don't Look/Executables",
    '.wsf': "/Users/Personal/Desktop/Don't Look/Executables",
    '.msi': "/Users/Personal/Desktop/Don't Look/Executables",
#Fonts C:\Users\Personal\Desktop\Don't Look\Fonts
    '.fnt': "/Users/Personal/Desktop/Don't Look/Fonts",
    '.fon': "/Users/Personal/Desktop/Don't Look/Fonts",
    '.otf': "/Users/Personal/Desktop/Don't Look/Fonts",
    '.ttf': "/Users/Personal/Desktop/Don't Look/Fonts",
#Programming C:\Users\Personal\Desktop\Don't Look\A11Pr0j3ctsF0ld3r\Workspace
    '.c': "/Users/Personal/Desktop/Don't Look/A11Pr0j3ctsF0ld3r/Workspace/C&C++",
    '.class': "/Users/Personal/Desktop/Don't Look/A11Pr0j3ctsF0ld3r/Workspace/Java",
    '.dart': "/Users/Personal/Desktop/Don't Look/A11Pr0j3ctsF0ld3r/Workspace/Dart",
    '.py': "/Users/Personal/Desktop/Don't Look/A11Pr0j3ctsF0ld3r/Workspace/Python",
    '.sh': "/Users/Personal/Desktop/Don't Look/A11Pr0j3ctsF0ld3r/Workspace/Shell",
    '.swift': "/Users/Personal/Desktop/Don't Look/A11Pr0j3ctsF0ld3r/Workspace/Swift",
    '.html': "/Users/Personal/Desktop/Don't Look/A11Pr0j3ctsF0ld3r/Workspace/HTML",
    '.h': "/Users/Personal/Desktop/Don't Look/A11Pr0j3ctsF0ld3r/Workspace/C&C++",
#Spreadsheets
    '.ods' : "/Users/kalle/Desktop/kalle/Text/Microsoft/Excel",
    '.xlr' : "/Users/kalle/Desktop/kalle/Text/Microsoft/Excel",
    '.xls' : "/Users/kalle/Desktop/kalle/Text/Microsoft/Excel",
    '.xlsx' : "/Users/kalle/Desktop/kalle/Text/Microsoft/Excel",
}
folder_to_track = "/Users/Personal/Desktop/Sorter"
folder_destination = "/Users/Personal/Desktop/TestDestination"
event_handler = Hello()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
