import json 
import os

class Carro: 

    def __init__(self):
        self.modelo = ""
        self.marca = ""
        self.nome = ""
        self.ano = ""
        self.cor = ""
        self.placa = ""
        self.arquivo_json_carro = self.inicializarJson()

    def inicializarJson(self): 
        caminho_json = 'crud-python\\src\\modules\\dataBase\\carro.json'
        if not os.path.exists(caminho_json):
            with open(caminho_json, 'w') as arquivo:
               json.dump({}, arquivo)

        return caminho_json

    def mostrarMenuCarros(self):
        print("")
        print("╔════════════════════════════════════════════════════╗")
        print("║                  MÓDULO CARRO                      ║")
        print("╠════════════════════════════════════════════════════╣")
        print("║  1. Adicionar veículo  📝                          ║")
        print("║  2. Exibir frota       📋                          ║")
        print("║  3. Pesquisar veículo  🔍                          ║")
        print("║  4. Atualizar veículo  🔄                          ║")
        print("║  5. Deletar veículo    ❌                          ║")
        print("║  0. Voltar                                         ║")
        print("╚════════════════════════════════════════════════════╝")

    def menuCarro(self):
        self.mostrarMenuCarros()
        opcao = int(input("Escolha uma das opções que deseja: "))
        
        match opcao:
            case 1:
                self.adicionarVeiculo()
            case 2:
                self.exibirFrota()
            case 3:
                self.pesquisarVeiculo()
            case 4:
                self.atualizarVeiculo()
            case 5:
                self.deletarVeiculo()
            case 0:
                return
            case _:
                print("╔════════════════════════════════════════════════════╗")
                print("║                   OPCAO INVÁLIDA!                  ║")
                print("║         Por favor, selecione uma opção válida.     ║")
                print("╚════════════════════════════════════════════════════╝")
                print("Opção inválida. Tente novamente.")
                opcao = int(input("Escolha uma das opções que deseja: "))
        
        self.menuCarro()

    def adicionarVeiculo(self):
        placaValidada = False
        
        while not placaValidada:
            print("")
            print("╔════════════════════════════════════════════════════╗")
            print("║                   CADASTRO CARRO   📝              ║")
            print("╚════════════════════════════════════════════════════╝")
            print("")
            print("════════════ Informe os dados do veículo ════")
            self.placa = input("Insira a placa do carro: ").upper()
            placaValidada = self.validarPlaca(self.placa)
            
            if placaValidada:
                self.modelo = input("Insira o modelo do carro: ").capitalize()
                self.marca = input("Insira a marca do carro: ").capitalize()
                self.nome = input("Insira o nome do carro: ").capitalize()
                self.ano = input("Insira o ano do carro: ")
                self.cor = input("Insira a cor do carro: ").capitalize()
        
        self.criar()

    def imprimirDados(self, veiculo):
        print("")
        print("╔═══════════════════ Carro ════════════════════════╗")
        print("║ Modelo:", veiculo['modelo'])
        print("║ Marca:", veiculo['marca'])
        print("║ Nome:", veiculo['nome'])
        print("║ Ano:", veiculo['ano'])
        print("║ Cor:", veiculo['cor'])
        print("║ Placa:", veiculo['placa'])
        print("╚══════════════════════════════════════════════════╝")

    def exibirFrota(self):
        dados = self.lerJson(self.arquivo_json_carro)
        for placa in dados:
            self.imprimirDados(dados[placa])
        
        print("")
        print("Deseja realizar mais alguma operação no módulo de Carro?")
    
    def pesquisarVeiculo(self):
        dados = self.lerJson(self.arquivo_json_carro)
        placa = input("Insira a placa do carro: ").upper()
        if placa in dados:
            carro = dados[placa]
            self.imprimirDados(carro)
        else:
            print("")
            print("╔════════════════════════════════════════════════════╗")
            print("║              CARRO NÃO ENCONTRADO                  ║")
            print("╚════════════════════════════════════════════════════╝")
            print("")
        
        print("")
        print("Deseja realizar mais alguma operação no módulo de Carro?")
 
    def deletarVeiculo(self):
        placaPesquisa = input("Insira a placa do carro que deseja deletar: ").upper()
        dados = self.lerJson(self.arquivo_json_carro)
        
        if placaPesquisa in dados:
            print("Carro encontrado.")
            del dados[placaPesquisa]
            self.escreverJson(self.arquivo_json_carro, dados)
            print("")
            print("╔════════════════════════════════════════════════════╗")
            print("║          CARRO ATUALIZADO COM SUCESSO  ✅          ║")
            print("╚════════════════════════════════════════════════════╝")
            print("")
        else:
            print("")
            print("╔════════════════════════════════════════════════════╗")
            print("║              CARRO NÃO ENCONTRADO!                 ║")
            print("╚════════════════════════════════════════════════════╝")
            print("")

    def atualizarVeiculo(self):
        print("")
        print("╔════════════════════════════════════════════════════╗")
        print("║                ATUALIZAR CARRO   🔄                ║")
        print("╚════════════════════════════════════════════════════╝")
        
        placa = input("Informe a placa do carro que deseja atualizar: ").upper()
        dados = self.lerJson(self.arquivo_json_carro)
        
        if placa in dados:
            self.imprimirDados(dados[placa])
            print("Carro encontrado!")
            
            print("")
            dados[placa]['modelo'] = input("Insira o modelo do carro: ").capitalize()
            dados[placa]['marca'] = input("Insira a marca do carro: ").capitalize()
            dados[placa]['nome'] = input("Insira o nome do carro: ").capitalize()
            dados[placa]['ano'] = input("Insira o ano do carro: ")
            dados[placa]['cor'] = input("Insira a cor do carro: ").capitalize()
            
            self.escreverJson(self.arquivo_json_carro, dados)
            print("")
            print("╔════════════════════════════════════════════════════╗")
            print("║          CARRO ATUALIZADO COM SUCESSO  ✅          ║")
            print("╚════════════════════════════════════════════════════╝")
            print("")
        else:
            print("")
            print("╔════════════════════════════════════════════════════╗")
            print("║              CARRO NÃO ENCONTRADO!                 ║")
            print("╚════════════════════════════════════════════════════╝")
            print("")
            print("Carro não cadastrado em sistema.")
            print("")
            
    def criar(self):
        dados = self.lerJson(self.arquivo_json_carro) 
        
        veiculo = {
            self.placa:{
                "modelo": self.modelo,
                "marca": self.marca,
                "nome": self.nome,
                "ano": self.ano,
                "cor": self.cor,
                "placa": self.placa
            } 
        }
        dados.update(veiculo)
        self.escreverJson(self.arquivo_json_carro, dados)
        
        print("")
        print("╔════════════════════════════════════════════════════╗")
        print("║        CARRO ADICIONADO COM SUCESSO!  ✅           ║")
        print("╚════════════════════════════════════════════════════╝")
        print("")
        print("Deseja realizar mais alguma operação em módulo Carro?")

    def validarPlaca(self, placa):
        dados = self.lerJson(self.arquivo_json_carro)
        
        if placa in dados:
            print('')
            print('Placa já cadastrada no sistema!')
            print('Informe uma nova placa')
            return False
        return True
        
    def lerJson(self, arquivo):
        with open(arquivo, 'r', encoding = "utf-8") as j:
            return json.load(j)
    
    def escreverJson(self, arquivo, dados):
        with open(arquivo, 'w', encoding = "utf-8") as j:
            json.dump(dados, j, indent=4, ensure_ascii = False)