import os
from datetime import datetime

class Logger:
    def __init__(self, process, user_name):
        self.process = process
        self.user_name = user_name
        self.date = datetime.now().strftime('%Y-%m-%d')
        self.log_folder = f"C:/Users/User/OneDrive/Desktop/data_science/recsys_word2vec/logs"
        self.ensure_log_directory()
        self.current_step = None
        self.log_files = {}

    def ensure_log_directory(self):
        os.makedirs(self.log_folder, exist_ok=True)

    def set_step(self, step):
        self.current_step = step
        if step not in self.log_files:
            self.log_files[step] = self.create_log_file(step)

    def create_log_file(self, step):
        filename = f"{self.process}_{self.user_name}_{step}_{self.date}.txt"
        filepath = os.path.join(self.log_folder, filename)
        open(filepath, 'a').close()
        return filepath

    def log(self, text):
        if self.current_step is None:
            raise ValueError("Step not set. Call set_step() before logging.")
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        full_text = f"{timestamp}: {text}\n"
        full_text_for_print = f"{timestamp}: {text}"
        with open(self.log_files[self.current_step], 'a') as file:
            file.write(full_text)
        print(full_text_for_print)
