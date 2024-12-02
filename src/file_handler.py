import csv
import json
import os
from datetime import datetime

from colorama import Fore

TASKS_JSON_FILEPATH = "data/tasks.json"
TASKS_CSV_FILEPATH = "data/tasks.csv"


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
    def save_to_csv(data, filename=TASKS_CSV_FILEPATH):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        # Nos aseguramos de que los datos tengan todas las claves necesarias
        cleaned_data = []
        for task in data:
            cleaned_task = {
                "id": task.get("id", ""),
                "title": task.get("title", ""),
                "description": task.get("description", ""),
                "status": task.get("status", "Pendiente"),
                "created_at": task.get(
                    "created_at", datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ),
                "completed_at": task.get("completed_at", ""),
            }
            cleaned_data.append(cleaned_task)
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "id",
                    "title",
                    "description",
                    "status",
                    "created_at",
                    "completed_at",
                ],
            )
            writer.writeheader()
            writer.writerows(cleaned_data)
            """Utilizamos cleaned_data en lugar de data
            para asegurarnos de que los datos
            tengan todas las claves necesarias
            y evitar errores al escribir en el archivo CSV"""

    @staticmethod
    def load_from_csv(filename=TASKS_CSV_FILEPATH):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                return list(reader)
        except FileNotFoundError:
            return []

    @staticmethod
    def convert_json_to_csv(json_file=TASKS_JSON_FILEPATH,
                            csv_file=TASKS_CSV_FILEPATH):
        """
        Convierte un archivo JSON a CSV
        """
        tasks = FileHandler.load_from_json(json_file)
        FileHandler.save_to_csv(tasks, csv_file)
        print(f"Datos convertidos de JSON a CSV en {csv_file}")

    @staticmethod
    def convert_csv_to_json(csv_file=TASKS_CSV_FILEPATH,
                            json_file=TASKS_JSON_FILEPATH):
        """
        Convierte un archivo CSV a JSON
        """
        tasks = FileHandler.load_from_csv(csv_file)
        FileHandler.save_to_json(tasks, json_file)
        print(f"Datos convertidos de CSV a JSON en {json_file}")

    @staticmethod
    def initialize_data():
        """
        Método para inicializar datos al arrancar la aplicación
        Prioriza la carga desde CSV si existe
        """
        # Primero, verificamos si existe un CSV
        if os.path.exists(TASKS_CSV_FILEPATH):
            try:
                # Si existe CSV, lo convertimos a JSON
                FileHandler.convert_csv_to_json()
                print(Fore.GREEN + "Datos cargados desde CSV")
            except Exception as e:
                print(Fore.RED + f"Error al cargar datos desde CSV: {e}")
                # Si falla la conversión, creamos un JSON vacío
                FileHandler.save_to_json([])
        else:
            # Si no existe CSV, verificamos si existe JSON
            if not os.path.exists(TASKS_JSON_FILEPATH):
                # Si no existe JSON, creamos uno vacío
                FileHandler.save_to_json([])
