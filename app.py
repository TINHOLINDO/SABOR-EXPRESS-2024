import os

clientes = [{"nome": "João", "email": "joao@example.com", "ativo": True},
            {"nome": "Maria", "email": "maria@example.com", "ativo": False},
            {"nome": "Pedro", "email": "pedro@example.com", "ativo": True}]

def mostra_titulo():
    print("""
    

██╗░░░██╗██╗░░░░░████████╗██████╗░░█████╗░  ██████╗░██████╗░██╗███╗░░░███╗███████╗
██║░░░██║██║░░░░░╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██║████╗░████║██╔════╝
██║░░░██║██║░░░░░░░░██║░░░██████╔╝███████║  ██████╔╝██████╔╝██║██╔████╔██║█████╗░░
██║░░░██║██║░░░░░░░░██║░░░██╔══██╗██╔══██║  ██╔═══╝░██╔══██╗██║██║╚██╔╝██║██╔══╝░░
╚██████╔╝███████╗░░░██║░░░██║░░██║██║░░██║  ██║░░░░░██║░░██║██║██║░╚═╝░██║███████╗
░╚═════╝░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝╚══════╝2
        """)

def mostra_escolhas():
    print("1. Cadastrar Clientes")
    print("2. Listar Clientes")
    print("3. Ativar/Desativar Cliente")
    print("4. Sair")

def escolhe_opcao():

    def exibir_subtitulo(texto):
        os.system("cls")
        linha = "_" * 65
        print(linha)
        print(texto)
        print(linha)
        print(" ")

    def retorna_menu():
        input("Digite uma tecla para voltar ao menu principal ")
        main()

    def cadastra_clientes():
        exibir_subtitulo("Cadastrar Clientes")

        nome_cliente = input("Digite o nome do cliente que deseja cadastrar: ")
        email_cliente = input(f"Digite o email do {nome_cliente} para cadastrar: ")
        dados_do_cliente = {"nome": nome_cliente, "email": email_cliente, "ativo": True}
        clientes.append(dados_do_cliente)
        print(f"O cliente {nome_cliente} foi cadastrado com sucesso\n")

        retorna_menu()

    def listar_clientes():
        exibir_subtitulo("Lista de Clientes Cadastrados")
        for cliente in clientes:
            nome_cliente = cliente["nome"]
            email_cliente = cliente["email"]
            ativo = "Ativo" if cliente["ativo"] else "Inativo"
            print(f" - {nome_cliente.ljust(20)} | {email_cliente.ljust(30)} | {ativo}")
        retorna_menu()

    def ativar_cliente():
        exibir_subtitulo("Ativar/Desativar Cliente")
        nome_cliente = input("Digite o nome do cliente que deseja ativar/desativar: ")
        cliente_encontrado = False

        for cliente in clientes:
            if nome_cliente == cliente["nome"]:
                cliente_encontrado = True
                cliente["ativo"] = not cliente["ativo"]
                mensagem = f"{nome_cliente} foi ativado com sucesso" if cliente["ativo"] else f"{nome_cliente} foi desativado"
                print(mensagem)
        if not cliente_encontrado:
            print("Cliente não encontrado")
        retorna_menu()

    def finalizar_programa():
        os.system("cls")
        print("Finalizando o programa\n")

    def opcao_invalida():
        print("Essa opção não é válida")
        input("Aperte qualquer tecla para voltar")
        main()

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastra_clientes()
        elif opcao_escolhida == 2:
            listar_clientes()
        elif opcao_escolhida == 3:
            ativar_cliente()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == "__main__":
    main()
