from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

products_list = [
    {
        "nome_da_empresa": "Farinini",
        "data_de_fabricacao": "2021-10-10",
        "data_de_validade": "2023-06-03",
    }
]


def test_decorar_relatorio():
    report_instance = ColoredReport(SimpleReport)
    colored_report = report_instance.generate(products_list)
    bi = "\033[36m"
    bf = "\033[0m"
    gi = "\033[32m"
    gf = "\033[0m"
    ri = "\033[31m"
    rf = "\033[0m"
    assert colored_report == (
        f"{gi}Data de fabricação mais antiga:{gf} {bi}2021-10-10{bf}\n"
        f"{gi}Data de validade mais próxima:{gf} {bi}2023-06-03{bf}\n"
        f"{gi}Empresa com mais produtos:{gf} {ri}Farinini{rf}"
    )
