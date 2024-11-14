import json 
import os
import re

class Carro: 

    def __init__(self) -> None:
        self.estilo = ""
        self.marca = ""
        self.modelo = ""
        self.ano = ""
        self.cor = ""
        self.placa = ""
        self.arquivo_json_carro = self.inicializarJson()

    def inicializarJson(self) -> str: 
        caminho_json = 'crud-python\\src\\modules\\dataBase\\carro.json'

        if not os.path.exists(caminho_json):
            with open(caminho_json, 'w') as arquivo:
               json.dump({}, arquivo)

        return caminho_json

    def selecionarOpcao(self) -> int:
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

        opcao = int(input("Escolha uma das opções que deseja: "))

        return opcao

    def menuCarro(self) -> None:
        opcao = self.selecionarOpcao()
        
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
                print("")
                print("╔════════════════════════════════════════════════════╗")
                print("║                   OPCAO INVÁLIDA!                  ║")
                print("║         Por favor, selecione uma opção válida.     ║")
                print("╚════════════════════════════════════════════════════╝")
                print("Opção inválida. Tente novamente.")
        
        self.menuCarro()

    def adicionarVeiculo(self) -> None:
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
                self.estilo = input("Insira o estilo do carro: ").capitalize()
                self.marca = input("Insira a marca do carro: ").capitalize()
                self.modelo = input("Insira o modelo do carro: ").capitalize()
                self.ano = input("Insira o ano do carro: ")
                self.cor = input("Insira a cor do carro: ").capitalize()

        self.criar()

    def imprimirDados(self, veiculo: dict) -> None:
        print("")
        print("╔═══════════════════ Carro ════════════════════════╗")
        print("║ Estilo:", veiculo['estilo'])
        print("║ Marca:", veiculo['marca'])
        print("║ Modelo:", veiculo['modelo'])
        print("║ Ano:", veiculo['ano'])
        print("║ Cor:", veiculo['cor'])
        print("║ Placa:", veiculo['placa'])
        print("╚══════════════════════════════════════════════════╝")

    def exibirFrota(self) -> None:
        dados = self.lerJson(self.arquivo_json_carro)
        for placa in dados:
            self.imprimirDados(dados[placa])
        
        print("")
        print("Deseja realizar mais alguma operação no módulo de Carro?")
    
    def pesquisarVeiculo(self) -> None:
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
 
    def deletarVeiculo(self) -> None:
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

    def atualizarVeiculo(self) -> None:
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
            dados[placa]['estilo'] = input("Insira o estilo do carro: ").capitalize()
            dados[placa]['marca'] = input("Insira a marca do carro: ").capitalize()
            dados[placa]['modelo'] = input("Insira o modelo do carro: ").capitalize()
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
            
    def criar(self) -> None:
        dados = self.lerJson(self.arquivo_json_carro) 
        
        veiculo = {
            self.placa:{
                "estilo": self.estilo,
                "marca": self.marca,
                "modelo": self.modelo,
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

    def validarPlaca(self, placa: str) -> bool:

        regex_placa = r"^[A-Z]{3}\d[A-Z]\d{2}$"

        if bool(re.match(regex_placa, placa)):

            dados = self.lerJson(self.arquivo_json_carro)
            
            if placa in dados:
                print('')
                print('Placa já cadastrada no sistema!')
                print('Informe uma nova placa')
                return False
            return True
        
        else:
            print('\nPlaca inválida!')
            print('Informe uma nova placa')
            return False
        
    def lerJson(self, arquivo: dict) -> dict:
        with open(arquivo, 'r', encoding = "utf-8") as j:
            return json.load(j)
    
    def escreverJson(self, arquivo: dict, dados: dict) -> None:
        with open(arquivo, 'w', encoding = "utf-8") as j:
            json.dump(dados, j, indent=4, ensure_ascii = False)