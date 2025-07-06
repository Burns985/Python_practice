import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def move_to_videos_folder(source_folder, target_folder):
    for filename in os.listdir(source_folder):
        src_path = os.path.join(source_folder, filename)
        if os.path.isfile(src_path):
            dest_path = os.path.join(target_folder, filename)
            shutil.move(src_path, dest_path)
            print(f"Moved '{filename}' to the Videos folder.")


class ChromeDownloadsHandler(FileSystemEventHandler):
    def __init__(self, source_folder, target_folder):
        self.source_folder = source_folder
        self.target_folder = target_folder

    def on_created(self, event):
        time.sleep(1)  # Wait for the file to be fully downloaded
        move_to_videos_folder(self.source_folder, self.target_folder)


def main():
    chrome_downloads_folder = "C:/Users/muhai/OneDrive/Documents"  # Replace with your Chrome downloads folder path
    videos_folder = "C:/Users/muhai/OneDrive/Music"  # Replace with your Videos folder path

    event_handler = ChromeDownloadsHandler(chrome_downloads_folder, videos_folder)
    observer = Observer()
    observer.schedule(event_handler, path=chrome_downloads_folder, recursive=False)
    observer.start()

    try:
        print("Chrome Downloads Monitor is running. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
