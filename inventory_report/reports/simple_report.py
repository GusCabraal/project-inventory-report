from datetime import date


class SimpleReport:
    @classmethod
    def __get_first_manufacturing_date(cls, data: list[dict]):
        data_fabricacao = date.fromisoformat(data[0]["data_de_fabricacao"])
        for product in data:
            data_fab_item = date.fromisoformat(product["data_de_fabricacao"])
            if data_fabricacao > data_fab_item:
                data_fabricacao = data_fab_item
        return data_fabricacao

    @classmethod
    def __get_closer_expiration_date(cls, data: list[dict]):
        hoje = date.today()
        diferenca_date = date.fromisoformat(data[0]["data_de_validade"]) - hoje
        data_validade = date.fromisoformat(data[0]["data_de_validade"])
        for product in data:
            data_val_item = date.fromisoformat(product["data_de_validade"])
            diferenca_val_item = data_val_item - hoje
            if diferenca_date > diferenca_val_item:
                data_validade = data_val_item
                diferenca_date = data_val_item - hoje
        return data_validade

    @classmethod
    def __get_bigger_stock(cls, data: list[dict]):
        company_stock = dict()
        for product in data:
            nome_empresa = product["nome_da_empresa"]
            if nome_empresa not in company_stock:
                company_stock[nome_empresa] = 0
            else:
                company_stock[nome_empresa] += 1

        empresa_mais_produtos = max(company_stock, key=company_stock.get)
        return empresa_mais_produtos

    @staticmethod
    def generate(data):

        first_date = SimpleReport.__get_first_manufacturing_date(data)
        last_date = SimpleReport.__get_closer_expiration_date(data)
        empresa_mais_produtos = SimpleReport.__get_bigger_stock(data)
        return (
            f"Data de fabricação mais antiga: {first_date}\n"
            f"Data de validade mais próxima: {last_date}\n"
            f"Empresa com mais produtos: {empresa_mais_produtos}"
        )
