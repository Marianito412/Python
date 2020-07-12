from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from StringStuff import *
import os
import time

class Watcher:
    folder_to_track = "/Users/Mariano/Desktop/Sorter"

    def __init__(self):
        self.observer = Observer()

    def run(self):   
        event_handler = Handler()
        self.observer.schedule(event_handler, self.folder_to_track, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Interrupted by keyboard")
        self.observer.join()

class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        folder_to_track = "/Users/Mariano/Desktop/Sorter"
        for filename in os.listdir(folder_to_track):
            src = f"{folder_to_track}/{filename}"
            destination = get_destination(filename)
            ensure_dir(destination)
            os.rename(src, f"{destination}/{filename}")

if __name__ == "__main__":
    w = Watcher()
    w.run()