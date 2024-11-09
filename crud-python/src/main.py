from modules.Cliente import Cliente

cliente = Cliente()

def showMenu():
    print("")
    print("╔════════════════════════════════════════════════════╗")
    print("║            BEM-VINDO AO SISTEMA DE GESTÃO          ║")
    print("║                     LOCADORA                       ║")
    print("╠════════════════════════════════════════════════════╣")
    print("║                                                    ║")
    print("║   Neste sistema, você pode gerenciar as seguintes  ║")
    print("║   opções:                                          ║")
    print("║                                                    ║")
    print("║   1. Cliente - Gerencie os clientes da locadora    ║")
    print("║   2. Carro - Gerencie a frota de carros            ║")
    print("║   3. Aluguel - Gerencie os contratos de aluguel    ║")
    print("║   0. Sair - Saia do sistema                        ║")
    print("║                                                    ║")
    print("╚════════════════════════════════════════════════════╝")

    
def main():
        showMenu()
        opcao = int(input("Digite uma opção: "))
        
        while True:
            match opcao:
                case 0:
                    print("")
                    print("╔════════════════════════════════════════════════════╗")
                    print("║                 SAINDO DO SISTEMA...               ║")
                    print("╚════════════════════════════════════════════════════╝")
                    exit()
                    break
                case 1:
                    cliente.mainCliente()
                    main()
                case 2:
                    print("╔════════════════════════════════════════════════════╗")
                    print("║                   MÓDULO CARRO                     ║")
                    print("╚════════════════════════════════════════════════════╝")
                case 3:
                    print("╔════════════════════════════════════════════════════╗")
                    print("║                   MÓDULO ALUGUEL                   ║")
                    print("╚════════════════════════════════════════════════════╝")
                case _:
                    print('\n')
                    print("╔════════════════════════════════════════════════════╗")
                    print("║                   ESCOLHA INVÁLIDA!                ║")
                    print("║         Por favor, selecione uma opção válida.     ║")
                    print("╚════════════════════════════════════════════════════╝")
                    opcao = int(input("Digite uma opção válida: "))
                    
main()