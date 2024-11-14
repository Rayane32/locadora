import json
import os
import time


class AluguelInstancer:
    def __init__(self):
        self.caminhoJsonCliente = 'crud-python\\src\\modules\\dataBase\\cliente.json'
        self.caminhoJsonCarro = 'crud-python\\src\\modules\\dataBase\\carro.json'
        self.caminhoJsonAluguel = 'crud-python\\src\\modules\\dataBase\\aluguel.json'
        
        self.json_cliente = self.inicializarJson(self.caminhoJsonCliente)
        self.json_carro = self.inicializarJson(self.caminhoJsonCarro)
        self.json_aluguel = self.inicializarJson(self.caminhoJsonAluguel)

    def inicializarJson(self, path):
        if not os.path.exists(path):
            with open(path, 'w') as arquivo:
                json.dump({}, arquivo)
        return path

    def mostrarMenuAluguel(self):
        print("")
        print("╔════════════════════════════════════════════════════╗")
        print("║                 MÓDULO ALUGUEL                    ║")
        print("╠════════════════════════════════════════════════════╣")
        print("║  1. Iniciar Novo Aluguel      🚗                   ║")
        print("║  2. Listar Aluguéis           📋                   ║")
        print("║  3. Buscar Aluguel por CPF e Placa 🔍             ║")
        print("║  4. Editar Aluguel            ✏️                   ║")
        print("║  5. Apagar Aluguel            ❌                   ║")
        print("║  0. Voltar                                         ║")
        print("╚════════════════════════════════════════════════════╝")

    def menuAluguel(self):
        while True:
            self.mostrarMenuAluguel()
            opcao = int(input("Escolha uma das opções que deseja: "))

            match opcao:
                case 0:
                    break
                case 1:
                    self.iniciarNovoAluguel()
                case 2:
                    self.listarAlugueis()
                case 3:
                    self.buscarAluguel()
                case 4:
                    self.editarAluguel()
                case 5:
                    self.apagarAluguel()
                case _:
                    print("Opção inválida, por favor escolha uma opção válida.")

    def fingirCarregamento(self):
            print(".", )
            time.sleep(0.5)
            print("..", )
            time.sleep(0.5)
            print("...", )

    def iniciarNovoAluguel(self):
        client = self.getClient()
        carro = self.getCar(None)
        
        if client and carro:
            aluguel = Aluguel()
            aluguel.newRent(carro, client)
        else:
            print("Erro ao iniciar novo aluguel.")

    def listarAlugueis(self):
        with open(self.json_aluguel, 'r', encoding="utf-8") as arquivo:
            alugueis = json.load(arquivo)

        print("Lista de Aluguéis:")
        for key, aluguel in alugueis.items():
            print(f"\nPlaca: {str(key).split('-')[0]}")
            print(f"Tempo de aluguel: {aluguel['tempoAluguel']}")
            print(f"Valor: R${aluguel['valorDoAluguel']}")
            print(f"Forma de pagamento: {aluguel['formaDePagamento']}")
            time.sleep(0.5)
        print("\nFim da lista de aluguéis.")

    def buscarAluguel(self):
        cpf = input("Informe o CPF do cliente: ")
        placa = input("Informe a placa do carro: ").replace("-", "")
        id_aluguel = f"{placa}-{cpf}"

        with open(self.json_aluguel, 'r', encoding="utf-8") as arquivo:
            alugueis = json.load(arquivo)

        if id_aluguel in alugueis:
            aluguel = alugueis[id_aluguel]
            print(f"\nAluguel encontrado: {id_aluguel}")
            print(f"Tempo de aluguel: {aluguel['tempoAluguel']}")
            print(f"Valor: R${aluguel['valorDoAluguel']}")
            print(f"Forma de pagamento: {aluguel['formaDePagamento']}")
        else:
            self.fingirCarregamento()
            print("Aluguel não encontrado.")

    def editarAluguel(self):
        print("\n--- Edição de Aluguel ---")
        client = self.getClient()
        carro = self.getCar(None)
        placaNormalizada = str(carro['placa']).replace("-", "")
        id_aluguel = f"{placaNormalizada}-{client['cpf']}"

        with open(self.json_aluguel, 'r', encoding="utf-8") as arquivo:
            alugueis = json.load(arquivo)

        if id_aluguel in alugueis:
            aluguel = alugueis[id_aluguel]
            print(f"\nAluguel encontrado: {id_aluguel}")
            print("Campos atuais do aluguel:")
            print(f"1. Tempo de aluguel: {aluguel['tempoAluguel']}")
            print(f"2. Valor: R${aluguel['valorDoAluguel']}")
            print(f"3. Forma de pagamento: {aluguel['formaDePagamento']}")
            
            campo = int(input("Digite o número do campo que deseja editar (1 - Tempo, 2 - Valor, 3 - Forma de pagamento): "))
            
            if campo == 1:
                aluguel['tempoAluguel'] = input("Digite o novo prazo do aluguel: ")
            elif campo == 2:
                aluguel['valorDoAluguel'] = float(input("Digite o novo valor do aluguel: "))
            elif campo == 3:
                aluguel['formaDePagamento'] = input("Digite a nova forma de pagamento: ")
            else:
                print("Opção inválida. Nenhuma alteração foi feita.")
                return

            alugueis[id_aluguel] = aluguel
            with open(self.json_aluguel, 'w', encoding="utf-8") as arquivo:
                json.dump(alugueis, arquivo, indent=4, ensure_ascii=False)
            print("Aluguel atualizado com sucesso.")
        else:
            print("Aluguel não encontrado.")

    def apagarAluguel(self):
        print("\n--- Apagar Aluguel ---")
        cpf = input("Digite o CPF do cliente: ")

        with open(self.json_aluguel, 'r', encoding="utf-8") as arquivo:
            alugueis = json.load(arquivo)

        alugueis_do_cpf = {key: aluguel for key, aluguel in alugueis.items() if key.endswith(cpf)}

        if alugueis_do_cpf:
            print(f"\nAluguéis encontrados para o CPF {cpf}:")
            for id_aluguel, aluguel in alugueis_do_cpf.items():
                print(f"\nPlaca: {str(id_aluguel).split('-')[0]}")
                print(f"Tempo de aluguel: {aluguel['tempoAluguel']}")
                print(f"Valor: R${aluguel['valorDoAluguel']}")
                print(f"Forma de pagamento: {aluguel['formaDePagamento']}")

            id_para_apagar = input("\nDigite a placa do carro que deseja apagar o aluguel: ")
            id_para_apagar = f"{id_para_apagar}-{cpf}"
            if id_para_apagar in alugueis_do_cpf:
                confirm = input(f"Tem certeza que deseja apagar o aluguel {id_para_apagar}? (s/n): ")
                if confirm.lower() == 's':
                    del alugueis[id_para_apagar]
                    with open(self.json_aluguel, 'w', encoding="utf-8") as arquivo:
                        json.dump(alugueis, arquivo, indent=4, ensure_ascii=False)
                    print("Aluguel apagado com sucesso.")
                else:
                    print("Operação cancelada.")
            else:
                time.sleep(0.2)
                print("ID de aluguel inválido. Abortando operação...")
                time.sleep(0.2)
        else:
            self.fingirCarregamento()
            print("Nenhum aluguel encontrado para o CPF fornecido. Abortando operação...")

    def getClient(self):
        cpfClient = input("Digite o CPF do cliente que vai alugar o carro: ")
        with open(self.json_cliente, 'r') as j:
            dados = json.load(j)
            client = dados.get(cpfClient)
            if client:
                self.printClient(client)
                confirm = input("É esse o cliente (s/n)? ")
                if confirm.lower() == "s":
                    return client
        print("Cliente não encontrado...\nTente novamente")
        return self.getClient()

    def getCar(self, placaCarro):
        if placaCarro != None:
            licensePlate = placaCarro
        else:
            licensePlate = input("Digite a placa do carro que deseja alugar: ")
        with open(self.json_carro, 'r') as j:
            dados = json.load(j)
            car = dados.get(licensePlate)
            if car:
                self.printCar(car)
                confirm = input("É esse o carro (s/n)? ")
                if confirm.lower() == "s":
                    return car
        print("Carro não encontrado...\nTente novamente")
        if placaCarro != None:
            return None
        else:
            return self.getCar(placaCarro)

    def printClient(self, cliente):
        print("\n╔════════ Cliente ═════════╗")
        print(" Nome:", cliente['nome'])
        print(" CPF:", cliente['cpf'])
        print(" Data de nascimento:", cliente['data_nascimento'])
        print(" E-mail:", cliente['email'])
        print(" Telefone:", cliente['telefone'])
        print(" Endereço:", cliente['endereco'])
        print("╚══════════════════════════╝")

    def printCar(self, car):
        print("\n╔════════ Carro ═════════╗")
        print(" Placa:", car['placa'])
        print(f" Marca e Nome: {car['marca']} {car['nome']}")
        print(f" Modelo: {car['modelo']}")
        print(" Ano:", car['ano'])
        print(" Cor:", car['cor'])
        print("╚════════════════════════╝")

class Aluguel:
    def __init__(self):
        self.json_aluguel = 'crud-python\\src\\modules\\dataBase\\aluguel.json'

    def newRent(self, car, client):
        with open(self.json_aluguel, 'r') as arquivo:
            dados = json.load(arquivo)

        id_aluguel = f"{str(car['placa']).replace('-', '')}-{client['cpf']}"
        prazo = input("Digite o prazo do aluguel: ")
        valor = float(input("Digite o valor do aluguel: "))
        formaDePagamento = input("Digite a forma de pagamento usada: ")
        dados[id_aluguel] = {
            "tempoAluguel": prazo,
            "valorDoAluguel": valor,
            "formaDePagamento": formaDePagamento
        }

        with open(self.json_aluguel, 'w', encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print("Aluguel registrado com sucesso.")
