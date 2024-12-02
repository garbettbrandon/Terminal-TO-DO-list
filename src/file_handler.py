import json
import os

from colorama import Fore

from constant.constants import TASKS_JSON_FILEPATH


class FileHandler:
    @staticmethod
    def save_to_json(data, filename=TASKS_JSON_FILEPATH):
        """
        Saves data to a JSON file.

        Args:
            data (dict): The data to be saved (expected to be a JSON-serializable object).
            filename (str): The path to the JSON file (defaults to TASKS_JSON_FILEPATH).

        Returns:
            None
        """
        # Create the directory for the file if it doesn't exist
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        # Open the file in write mode, with UTF-8 encoding
        with open(filename, "w", encoding="utf-8") as f:
            # Serialize the data to JSON format, with indentation and non-ASCII character support
            json.dump(data, f, indent=4, ensure_ascii=False)

    @staticmethod
    def load_from_json(filename=TASKS_JSON_FILEPATH):
        """
        Loads data from a JSON file.

        Args:
            filename (str): The path to the JSON file (defaults to TASKS_JSON_FILEPATH).

        Returns:
            dict: The loaded data, or an empty list if the file is not found or the JSON is invalid.
        """
        try:
            # Open the file in read mode, with UTF-8 encoding
            with open(filename, "r", encoding="utf-8") as f:
                # Deserialize the JSON data from the file
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Return an empty list if the file is not found or the JSON is invalid
            return []

    @staticmethod
    def initialize_data():
        """
        Initializes data by attempting to load it from the JSON file.

        Returns:
            None
        """
        try:
            # Load the data from the JSON file
            FileHandler.load_from_json()
        except Exception as e:
            # Print a warning message with the error if loading fails
            print(f"{Fore.YELLOW}Warning: could not load JSON data - {e}")