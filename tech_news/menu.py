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

    if not string.isnumeric() or int(string) < 0 or int(string) > 7:
        print(ValueError("Opção inválida"), file=sys.stderr)
    elif int(string) == 0:
        print("Digite quantas notícias serão buscadas:")

    elif int(string) == 1:
        print("Digite o título:")

    elif int(string) == 2:
        print("Digite a data no formato aaaa-mm-dd:")

    elif int(string) == 3:
        print("Digite a tag:")

    elif int(string) == 4:
        print("Digite a categoria:")


def analyzer_menu():
    """Seu código deve vir aqui"""
    menu_options = "".join(options)
    option = input(menu_options)

    switch(option)
