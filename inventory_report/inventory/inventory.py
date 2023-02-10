from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def get_data(cls, path):
        *rest, type_path = path.split(".")
        if type_path == "csv":
            with open(path, encoding="utf-8") as file:
                data_reader = csv.DictReader(file, delimiter=",")
                data_list = [data for data in data_reader]
                return data_list
        if type_path == "json":
            with open(path) as file:
                data_list = json.load(file)
                return data_list
        if type_path == "xml":
            with open(path) as fd:
                data_list = xmltodict.parse(fd.read())
                return data_list["dataset"]["record"]

    @classmethod
    def generate_report(cls, data: list[dict], report_type: str):
        if report_type == "simples":
            report = SimpleReport.generate(data)
        else:
            report = CompleteReport.generate(data)
        return report

    @staticmethod
    def import_data(path: str, report_type: str):
        data = Inventory.get_data(path)
        report = Inventory.generate_report(data, report_type)
        return report
