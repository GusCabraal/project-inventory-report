from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def get_data(cls, path):
        *rest, type_path = path.split(".")
        if type_path == "xml":
            with open(path) as fd:
                data_list = xmltodict.parse(fd.read())
                return data_list["dataset"]["record"]
        else:
            raise ValueError("Arquivo inválido")

    @staticmethod
    def import_data(path: str):
        return XmlImporter.get_data(path)
