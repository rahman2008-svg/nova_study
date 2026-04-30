import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    def __init__(self, callback):
        self.callback = callback

    def run(self):
        event_handler = Handler(self.callback)
        observer = Observer()
        observer.schedule(event_handler, "data", recursive=False)
        observer.start()

        print("👀 Live watcher started")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()

        observer.join()


class Handler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback

    def on_modified(self, event):
        print("🔄 Reloading AI...")
        self.callback()
