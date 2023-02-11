from inventory_report.inventory.product import Product


def test_cria_produto():
    product_instance = Product(
        1,
        "farinha",
        "Farinini",
        "01-05-2021",
        "02-06-2023",
        "123456",
        "ao abrigo de luz",
    )

    assert product_instance.id == 1
    assert product_instance.nome_da_empresa == "Farinini"
    assert product_instance.nome_do_produto == "farinha"
    assert product_instance.data_de_fabricacao == "01-05-2021"
    assert product_instance.data_de_validade == "02-06-2023"
    assert product_instance.numero_de_serie == "123456"
    assert product_instance.instrucoes_de_armazenamento == "ao abrigo de luz"
