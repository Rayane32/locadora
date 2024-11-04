
import json 
import os
class Cliente:
    def __init__(self):
        self.nome = ''
        self.cpf = ''
        self.data_nascimento = ''
        self.email = ''
        self.telefone = ''
        self.endereco =''
        self.opcao = ''
        self.arquivo_json_cliente = self.inicializarJson()
    
    def inicializarJson(self): 
        caminho_json = 'crud-python\\src\\modules\\dataBase\\cliente.json'
        
        if not os.path.exists(caminho_json):
            with open(caminho_json, 'w') as arquivo:
               json.dump({}, arquivo)

        return caminho_json
        
    def showMenuCliente(self):
        print("")
        print("╔════════════════════════════════════════════════════╗")
        print("║                  MÓDULO CLIENTE                    ║")
        print("╠════════════════════════════════════════════════════╣")
        print("║  1. Cadastrar Cliente       📝                     ║")
        print("║  2. Listar Clientes         📋                     ║")
        print("║  3. Buscar Cliente          🔍                     ║")
        print("║  4. Deletar Cliente         ❌                     ║")
        print("║  0. Voltar                                         ║")
        print("╚════════════════════════════════════════════════════╝")
    
    def mainCliente(self):
        self.showMenuCliente()
        self.opcao = int(input("Escolha uma das opções que deseja: "))
        
        while True:
            match self.opcao:
                case 0:
                    print('ok')
                case 1:
                    self.criarDadosCliente()
                case 2:
                    self.listarClientes()
                case _:
                    print('\n')
                    print("╔════════════════════════════════════════════════════╗")
                    print("║                   ESCOLHA INVÁLIDA!                ║")
                    print("║         Por favor, selecione uma opção válida.     ║")
                    print("╚════════════════════════════════════════════════════╝")
                    self.opcao = int(input("Digite uma opção válida: "))
            

    def criarDadosCliente(self):
        print("")
        print("╔════════════════════════════════════════════════════╗")
        print("║                   CADASTRO CLIENTE  📝             ║")
        print("╚════════════════════════════════════════════════════╝")
        print("")
        print("════════════ Informe os dados pessoais do cliente ════")
        self.cpf = input("CPF: ")
        self.validarCPF(self.cpf)
        self.nome = input("Nome completo: ")
        self.data_nascimento = input("Data de nascimento(dd/mm/yy): ")
        self.email = input("E-mail: ")
        self.telefone = input("Telefone: ")
        self.endereco = input("Endereço: ")
       
        self.create()
           
    def create(self):
        dados = self.lerJson(self.arquivo_json_cliente)
        
        cliente = {}
        cliente[self.cpf] = {
            'nome': self.nome,
            'cpf': self.cpf,
            'email': self.email,
            'telefone': self.telefone,
            'data_nascimento': self.data_nascimento,
            'endereco': self.endereco
        }
        dados.update(cliente)
        self.escreverJson(self.arquivo_json_cliente, dados)
        
        print("")
        print("╔════════════════════════════════════════════════════╗")
        print("║        CADASTRO REALIZADO COM SUCESSO  ✅          ║")
        print("╚════════════════════════════════════════════════════╝")
        print("Deseja realizar mais alguma operação em Cliente?")
        self.mainCliente()
    
    def listarClientes(self):
        print("╔════════════════════════════════════════════════════╗")
        print("║              LISTAGEM DE CLIENTES  📋              ║")
        print("╚════════════════════════════════════════════════════╝")
                       
        dados = self.lerJson(self.arquivo_json_cliente)
        for chave in dados:
            cliente = dados[chave]
            
            print("")
            print("╔════════════════════════════════════════════════════╗")
            print("║ Nome:", cliente['nome'])
            print("║ CPF:", cliente['cpf']),
            print("║ Data de nascimento: ", cliente['data_nascimento']),
            print("║ E-mail : ", cliente['email']),
            print("║ Telefone:", cliente['telefone']),
            print("║ Endereço:", cliente['endereco']),
            print("╚════════════════════════════════════════════════════╝")
        
        print("Deseja realizar mais alguma operação em Cliente?")
        self.mainCliente()
    
    def validarCPF(self, cpf):
        dados = self.lerJson(self.arquivo_json_cliente)
        
        if cpf in dados:
            print('')
            print('Esse cpf já pertence a um cliente no sistema!')
            print('Informe um novo cpf')
            self.criarDadosCliente()


    def lerJson(self, arquivo):
        with open(arquivo, 'r', encoding = "utf-8") as j:
            return json.load(j)
    
    def escreverJson(self, arquivo, dados):
        with open(arquivo, 'w', encoding = "utf-8") as j:
            json.dump(dados, j, indent=4, ensure_ascii = False)