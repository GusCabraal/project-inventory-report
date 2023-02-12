from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def get_data(self, path):
        new_data = self.importer.import_data(path)
        for item in new_data:
            self.data.append(item)
        return self.data

    @classmethod
    def generate_report(cls, data: list[dict], report_type: str):
        if report_type == "simples":
            report = SimpleReport.generate(data)
        else:
            report = CompleteReport.generate(data)
        return report

    def import_data(self, path: str, report_type: str):
        self.get_data(path)
        report = InventoryRefactor.generate_report(self.data, report_type)
        return report
