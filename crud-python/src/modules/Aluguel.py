
import json 
import os
class AluguelInstancer:
    def __init__(self):
        jsonClientPath =  'crud-python\\src\\modules\\dataBase\\cliente.json',
        jsonCarPath = 'crud-python\\src\\modules\\dataBase\\carro.json'
        self.json_client = inicializarJson(jsonClientPath)
        self.jsonCar = inicializarJson(jsonCarPath) 
        
        self.client = self.getClient()
        self.car = self.getCar()
        Aluguel.newRent(self.car, self.client)
       
    def getClient(self):
       
        while True:
            cpfClient = input("Digite o CPF do cliente que vai alugar o carro: ")
            try:
                with open(self.json_client, 'r') as j:
                    dados = json.load(j)
                    client = dados[cpfClient] 
                    self.printClient(client)
                    isThisClient = input("É esse o cliente (s/n)? ")
                    if(isThisClient.upper() == "S"):
                        return client
            except:
                print("Erro! Cliente não encontrado na base de clientes. Tente novamente...")
    
    def getCar(self):
        licensePlate = input("Agora digite a placa do carro que você deseja alugar: ")
        return {
            "licensePlate": 'pgj6g22',
            "carName": 'BMW M4',
            "cor": "azul"
        }
        
    def printClient(self, cliente):
        print("")
        print("╔════════════════════════════════════════════════════╗")
        print("║ Nome:", cliente['nome'])
        print("║ CPF:", cliente['cpf']),
        print("║ Data de nascimento: ", cliente['data_nascimento']),
        print("║ E-mail : ", cliente['data_nascimento']),
        print("║ Telefone:", cliente['telefone']),
        print("║ Endereço:", cliente['endereco']),
        print("╚════════════════════════════════════════════════════╝")
class Aluguel:
    def _init_(self):
        jsonClientPath =  'crud-python\\src\\modules\\dataBase\\cliente.json',
        jsonCarPath = 'crud-python\\src\\modules\\dataBase\\carro.json'
        self.json_client = inicializarJson(jsonClientPath)
        self.jsonCar = inicializarJson(jsonCarPath) 
    def newRent(self, car, client):
        with open(self.jsonCar , 'r') as j:
            dados = json.load(j)
        newRent = {}
        newRent[f"{car['licensePlate']}-{client['cpf']}"] = {
            "rentTime": '2 years',
            "value": '22',
            "paymentForm": "credit"
        }
        dados.update(newRent)
        with open(self.jsonCar, 'w') as j:
            json.dump(dados, j, indent=4)

def inicializarJson(path): 
    normalizedPath = path[0]
    if not os.path.exists(normalizedPath):
        with open(normalizedPath, 'w') as arquivo:
            json.dump({}, arquivo)
    return normalizedPath
