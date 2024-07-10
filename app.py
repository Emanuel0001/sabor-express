import os

restaurantes = [
    {'nome': 'BurgerKing', 'categoria': 'fastfood', 'ativo': False},
    {'nome': 'pizzaSup', 'categoria': 'italiana', 'ativo': True},
    {'nome': 'dell', 'categoria': 'lanchonete', 'ativo': False}
]
def imprimir_titulo_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar Status do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_titulo('Encerrando App')

def voltar_ao_menu_principal():
    input('\n Digite uma tecla para voltar ao menu principal ou tecle ENTER: ')
    main()

def exibir_titulo(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    print('opcao invalida')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    pass
    exibir_titulo('cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante: ')
    Categoria_resturante = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': Categoria_resturante, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_restaurante} cadastrado com sucess!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_titulo('Lista de restaurantes:')
   
    print(f'{("Nome".ljust(30))} | {("Categoria".ljust(20))} | Status')
    for item in restaurantes:
        nome_restaurante = item['nome']
        categoria = item['categoria']
        ativos = 'ativado' if item['ativo'] else 'desativado'
        print(f'| Nome: {nome_restaurante.ljust(20)} | Categoria: {categoria.ljust(20)} | Status: {ativos.ljust(20)}')
    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    exibir_titulo('Alternando o estado do restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'o restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'o restaurante {nome_do_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante nao encontrado')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        # opcao_escolhida = int(opcao_escolhida)
        print(f'Você escolheu a opção {opcao_escolhida}')
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
            print('cadastrar restaurante')
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('clear')
    imprimir_titulo_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__' :
    main()