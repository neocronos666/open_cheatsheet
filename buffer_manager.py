# buffer_manager.py
import os
import json
import time
import logging

class BufferManager:
    def __init__(self, root_dir, buffer_file, settings_file):
        self.root_dir = root_dir
        self.buffer_file = buffer_file
        self.settings_file = settings_file
        self.buffer_data = {}
        self.settings = self.load_settings()

    def load_settings(self):
        """Load settings from the configuration file."""
        try:
            with open(self.settings_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error("Settings file not found.")
            return {}

    def should_refresh(self):
        """Determine if the buffer should be refreshed based on settings."""
        return self.settings.get("autorefresh", False)

    def refresh_buffer(self):
        """Refresh the buffer by scanning the cheatsheets directory."""
        for root, dirs, files in os.walk(self.root_dir):
            for file in files:
                if file.endswith('.chsheet'):
                    file_path = os.path.join(root, file)
                    self.buffer_data[file_path] = self.parse_chsheet(file_path)
        self.save_buffer()

    def parse_chsheet(self, file_path):
        """Parse the .chsheet file and return a dictionary with its contents."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                data['file_name'] = os.path.basename(file_path)
                data['title'] = self.extract_title(data['file_name'])
                data['last_modified'] = time.ctime(os.path.getmtime(file_path))
                return data
        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON in {file_path}")
            return {}

    def extract_title(self, file_name):
        """Extract the title from the file name."""
        base_name = os.path.splitext(file_name)[0]
        title = ''.join(e for e in base_name if e.isalnum()).capitalize()
        return title

    def save_buffer(self):
        """Save the buffer data to the buffer file."""
        try:
            with open(self.buffer_file, 'w') as f:
                json.dump(self.buffer_data, f, indent=4)
        except IOError as e:
            logging.error(f"Error saving buffer: {e}")

    def load_buffer(self):
        """Load buffer data from the buffer file."""
        try:
            with open(self.buffer_file, 'r') as f:
                self.buffer_data = json.load(f)
        except FileNotFoundError:
            logging.warning("Buffer file not found. Creating a new one.")
            self.refresh_buffer()

    def manual_refresh(self):
        """Manually trigger a buffer refresh."""
        self.refresh_buffer()

# Ejemplo de uso
if __name__ == "__main__":
    logging.basicConfig(filename='log/buffer_manager.log', level=logging.INFO)
    
    buffer_manager = BufferManager(
        root_dir='cheatsheets/',
        buffer_file='cfg/.buffer',
        settings_file='cfg/settings.cfg'
    )
    
    if buffer_manager.should_refresh():
        buffer_manager.refresh_buffer()
    else:
        buffer_manager.load_buffer()

