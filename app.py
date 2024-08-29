import os

# Lista global para armazenar os clientes
clientes = [
    {"nome": "Cliente 1", "tamanho": 13, "cor": "Azul", "ativo": True},
    {"nome": "Cliente 2", "tamanho": 45, "cor": "Azul", "ativo": False},
    {"nome": "Cliente 3", "tamanho": 20, "cor": "Branco", "ativo": True}
]

def exibir_nome_do_programa():
    print("""
██╗░░░██╗██╗░░░░░████████╗██████╗░░█████╗░░██████╗░░█████╗░███████╗
██║░░░██║██║░░░░░╚══██╔══╝██╔══██╗██╔══██╗██╔════╝░██╔══██╗╚════██║
██║░░░██║██║░░░░░░░░██║░░░██████╔╝███████║██║░░██╗░███████║░░███╔═╝
██║░░░██║██║░░░░░░░░██║░░░██╔══██╗██╔══██║██║░░╚██╗██╔══██║██╔══╝░░
╚██████╔╝███████╗░░░██║░░░██║░░██║██║░░██║╚██████╔╝██║░░██║███████╗
░╚═════╝░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚══════╝
""")

def mostra_escolhas():
    print("1. Cadastrar Novo Cliente")
    print("2. Listar Clientes")
    print("3. Ativar/Desativar Cliente")
    print("4. Sair")

def escolhe_opcao():

    def exibir_subtitulo(texto):
        os.system("cls" if os.name == 'nt' else 'clear')
        print(texto)
        print(" ")

    def retorna_menu():
        input("Digite uma tecla para voltar ao menu principal ")
        main()

    def cadastrar_cliente():
        exibir_subtitulo("Cadastrar Novo Cliente")
        nome_cliente = input("Digite o nome do cliente: ")
        tamanho = int(input("Digite o tamanho do cliente: "))
        cor = input("Digite a cor do cliente: ")
        ativo = input("O cliente está ativo? (Sim/Não): ").strip().lower() == 'sim'
        clientes.append({"nome": nome_cliente, "tamanho": tamanho, "cor": cor, "ativo": ativo})
        print(f"O cliente {nome_cliente} foi cadastrado com sucesso\n")
        retorna_menu()

    def listar_clientes():
        exibir_subtitulo("Lista de Clientes")
        if clientes:
            for i, cliente_item in enumerate(clientes, start=1):
                status = "Ativo" if cliente_item["ativo"] else "Inativo"
                print(f"{i}. Nome: {cliente_item['nome']} | Tamanho: {cliente_item['tamanho']} | Cor: {cliente_item['cor']} | Status: {status}")
        else:
            print("Nenhum cliente cadastrado.")
        retorna_menu()

    def ativar_desativar_cliente():
        exibir_subtitulo("Ativar/Desativar Cliente")
        listar_clientes()
        if clientes:
            try:
                escolha = int(input("Digite o número do cliente para ativar/desativar: "))
                if 1 <= escolha <= len(clientes):
                    cliente_item = clientes[escolha - 1]
                    cliente_item["ativo"] = not cliente_item["ativo"]
                    status = "Ativo" if cliente_item["ativo"] else "Inativo"
                    print(f"O cliente {cliente_item['nome']} agora está {status}.")
                else:
                    print("Número inválido. Por favor, escolha um número da lista.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
        retorna_menu()

    def finalizar_programa():
        os.system("cls" if os.name == 'nt' else 'clear')
        print("Finalizando o programa\n")

    def opcao_invalida():
        print("Opção inválida!")
        input("Aperte qualquer tecla para voltar ao menu...")
        main()

    def main():
        exibir_nome_do_programa()
        mostra_escolhas()
        try:
            opcao_escolhida = int(input("Escolha uma opção: "))
            if opcao_escolhida == 1:
                cadastrar_cliente()
            elif opcao_escolhida == 2:
                listar_clientes()
            elif opcao_escolhida == 3:
                ativar_desativar_cliente()
            elif opcao_escolhida == 4:
                finalizar_programa()
            else:
                opcao_invalida()
        except ValueError:
            opcao_invalida()

    main()

if __name__ == "__main__":
    escolhe_opcao()
