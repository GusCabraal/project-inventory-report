from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        *rest, type_path = path.split(".")
        if type_path == "json":
            with open(path) as file:
                data_list = json.load(file)
                return data_list
        else:
            raise ValueError("Arquivo inválido")
