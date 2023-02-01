# Requisito 12

import sys


options = [
    "Selecione uma das opções a seguir:\n",
    " 0 - Popular o banco com notícias;\n",
    " 1 - Buscar notícias por título;\n",
    " 2 - Buscar notícias por data;\n",
    " 3 - Buscar notícias por tag;\n",
    " 4 - Buscar notícias por categoria;\n",
    " 5 - Listar top 5 notícias;\n",
    " 6 - Listar top 5 categorias;\n",
    " 7 - Sair.",
]


def switch(string):

    dict_switch = {
        "0": "Digite quantas notícias serão buscadas:",
        "1": "Digite o título:",
        "2": "Digite a data no formato aaaa-mm-dd:",
        "3": "Digite a tag:",
        "4": "Digite a categoria:",
    }

    if not string.isnumeric() or int(string) < 0 or int(string) > 7:
        print(ValueError("Opção inválida"), file=sys.stderr)

    for _ in dict_switch:
        print(dict_switch[_])


def analyzer_menu():
    """Seu código deve vir aqui"""
    menu_options = "".join(options)
    option = input(menu_options)

    switch(option)
