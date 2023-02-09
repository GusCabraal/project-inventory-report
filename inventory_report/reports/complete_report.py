from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def _get_stock(cls, data: list[dict]):
        company_stock = dict()
        for product in data:
            empresa_produto = product["nome_da_empresa"]
            if empresa_produto not in company_stock:
                company_stock[empresa_produto] = 1
            else:
                company_stock[empresa_produto] += 1
        result = []
        for key in company_stock:
            result.append(f"- {key}: {company_stock[key]}")

        relatorio = "\n".join(result)
        return relatorio

    @staticmethod
    def generate(data):
        first_date = SimpleReport._get_first_manufacturing_date(data)
        last_date = SimpleReport._get_closer_expiration_date(data)
        empresa_mais_produtos = SimpleReport._get_bigger_stock(data)
        company_stock = CompleteReport._get_stock(data)
        return (
            f"Data de fabricação mais antiga: {first_date}\n"
            f"Data de validade mais próxima: {last_date}\n"
            f"Empresa com mais produtos: {empresa_mais_produtos}\n"
            f"Produtos estocados por empresa:\n"
            f"{company_stock}\n"
        )
