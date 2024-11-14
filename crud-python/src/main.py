from modules.Cliente import Cliente
from modules.Aluguel import AluguelInstancer

cliente = Cliente()
carro = Carro()

cliente = Cliente()
aluguel = AluguelInstancer()
def mostrarMenu():
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
    mostrarMenu()
    opcao = int(input("Digite uma opção: "))

    match opcao:
        case 0:
            print("")
            print("╔════════════════════════════════════════════════════╗")
            print("║                 SAINDO DO SISTEMA...               ║")
            print("╚════════════════════════════════════════════════════╝")
            exit()
            return
        case 1:
            cliente.menuCliente()

        case 2:
            carro.menuCarro()

        case 3:
            aluguel.menuAluguel()
        case _:
            print('\n')
            print("╔════════════════════════════════════════════════════╗")
            print("║                 ESCOLHA INVÁLIDA! ❌               ║")
            print("║         Por favor, selecione uma opção válida.     ║")
            print("╚════════════════════════════════════════════════════╝")
            
    main()          
    
main()