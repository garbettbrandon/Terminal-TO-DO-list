import csv
import json
import os

from colorama import Fore

from constant.constants import TASKS_JSON_FILEPATH


class FileHandler:
    @staticmethod
    def save_to_json(data, filename=TASKS_JSON_FILEPATH):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    @staticmethod
    def load_from_json(filename=TASKS_JSON_FILEPATH):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def initialize_data():
        try:
            FileHandler.load_from_json()
        except Exception as e:
            print(f"{Fore.YELLOW}Warning: could not load JSON data - {e}")
