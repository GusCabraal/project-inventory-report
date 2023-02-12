from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    try:
        file_path = sys.argv[1]
        report_type = sys.argv[2]
        *rest, type_path = file_path.split(".")
        if type_path == "csv":
            inventory_instance = InventoryRefactor(CsvImporter)
            sys.stdout.write(
                inventory_instance.import_data(file_path, report_type)
            )
        if type_path == "json":
            inventory_instance = InventoryRefactor(JsonImporter)
            sys.stdout.write(
                inventory_instance.import_data(file_path, report_type)
            )
        if type_path == "xml":
            inventory_instance = InventoryRefactor(XmlImporter)
            sys.stdout.write(
                inventory_instance.import_data(file_path, report_type)
            )
    except IndexError:
        sys.stderr.write("Verifique os argumentos\n")


main()
