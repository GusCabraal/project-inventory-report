from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def get_data(cls, path):
        *rest, type_path = path.split(".")
        if type_path == "json":
            with open(path) as file:
                data_list = json.load(file)
                return data_list
        else:
            raise ValueError("Arquivo inválido")

    @staticmethod
    def import_data(path: str):
        return JsonImporter.get_data(path)
