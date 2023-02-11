from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def get_data(cls, path):
        *rest, type_path = path.split(".")
        if type_path == "csv":
            with open(path, encoding="utf-8") as file:
                data_reader = csv.DictReader(file, delimiter=",")
                data_list = [data for data in data_reader]
                return data_list
        else:
            raise ValueError("Arquivo inválido")

    @staticmethod
    def import_data(path: str):
        return CsvImporter.get_data(path)
