from inventory_report.inventory.product import Product


def test_cria_produto():
    product_instance = Product(
        1,
        "Curso",
        "Trybe",
        "27/10/2019",
        "31/12/2100",
        "123456",
        "Qualquer lugar",
    )

    assert product_instance.id == 1
    assert product_instance.nome_da_empresa == "Trybe"
    assert product_instance.nome_do_produto == "Curso"
    assert product_instance.data_de_fabricacao == "27/10/2019"
    assert product_instance.data_de_validade == "31/12/2100"
    assert product_instance.numero_de_serie == "123456"
    assert product_instance.instrucoes_de_armazenamento == "Qualquer lugar"
