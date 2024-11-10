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

    def showMenuCars(self):
        print("")
        print("╔════════════════════════════════════════════════════╗")
        print("║                  MÓDULO CARRO                      ║")
        print("╠════════════════════════════════════════════════════╣")
        print("║  1. Adicionar veículo                              ║")
        print("║  2. Exibir frota                                   ║")
        print("║  3. Atualizar veículo                              ║")
        print("║  4. Excluir veículo                                ║")
        print("║  5. Deletar Cliente                                ║")
        print("║  0. Voltar                                         ║")
        print("╚════════════════════════════════════════════════════╝")


    # Menu de opções
    def mainCars(self):
        while True:
            self.showMenuCars()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.adicionarVeiculo()
            
            elif opcao == "2":
                self.exibirFrota()
            
            elif opcao == "3":
                Carro.atualizarVeiculo()
            
            elif opcao == "4":
                Carro.deletarVeiculo()

            elif opcao == "5":
                print("Saindo do programa...")
                break
            
            else:
                print("Opção inválida. Tente novamente.")

    def adicionarVeiculo(self):
        print("")
        print("╔════════════════════════════════════════════════════╗")
        print("║                   CADASTRO CARRO   📝              ║")
        print("╚════════════════════════════════════════════════════╝")
        print("")
        print("════════════ Informe os dados do veículo ════")
        self.modelo = input("Insira o modelo do carro: ").capitalize()
        self.marca = input("Insira a marca do carro: ").capitalize()
        self.nome = input("Insira o nome do carro: ").capitalize()
        self.ano = input("Insira o ano do carro: ")
        self.cor = input("Insira a cor do carro: ").capitalize()
        self.placa = input("Insira a placa do carro: ").upper()
        print("Carro adicionado com sucesso.")

        self.create()

    def imprimirDados(self, veiculo):
        print(f"Modelo: {veiculo["modelo"]}")
        print(f"Marca: {veiculo["marca"]}")
        print(f"Nome: {veiculo["nome"]}")
        print(f"Ano: {veiculo["ano"]}")
        print(f"Cor: {veiculo["cor"]}")
        print(f"Placa: {veiculo["placa"]}")


    def exibirFrota(self):
        dados = self.lerJson(self.arquivo_json_carro)
        for placa in dados:

            self.imprimirDados(dados[placa])  
            print()
    
#     @classmethod
#     def pesquisarVeiculo(cls):
#         placa = input("Insira a placa do carro: ").upper()
#         for carro in cls.frota:
#             if carro.placa == placa:
#                 carro.imprimirDados()  # Corrigido para chamar o método corretamente
#                 return
#         print("Carro não encontrado.")

#     @classmethod
#     def atualizarVeiculo(cls):
#         placa = input("Insira a placa do carro que deseja atualizar: ").upper()
#         for carro in cls.frota:
#             if carro.placa == placa:
#                 carro.modelo = input("Insira o novo modelo: ").capitalize()
#                 carro.marca = input("Insira a nova marca: ").capitalize()
#                 carro.nome = input("Insira o novo nome: ").capitalize()
#                 carro.ano = input("Insira o novo ano: ")
#                 carro.cor = input("Insira a nova cor: ").capitalize()
#                 carro.placa = input("Insira a nova placa: ").upper()
#                 print("Carro atualizado com sucesso.")
#                 cls.salvarFrota("veiculos.json")
#                 return
#         print("Carro não encontrado.")
    
#     @classmethod
#     def deletarVeiculo(cls):
#         placa = input("Insira a placa do carro que deseja deletar: ").upper()
#         for carro in cls.frota:
#             if carro.placa == placa:
#                 cls.frota.remove(carro)
#                 print("Carro deletado com sucesso.")
#                 cls.salvarFrota("veiculos.json")
#                 return
#         print("Carro não encontrado.")
    
    

# # Carregar os dados do arquivo JSON
# try:
#     with open("veiculos.json", "r", encoding="utf-8") as arquivo:
#         carros = json.load(arquivo)
#     for data in carros:
#         Carro(
#             modelo=data["modelo"],
#             marca=data["marca"],
#             nome=data["nome"],
#             ano=data["ano"],
#             cor=data["cor"],
#             placa=data["placa"]
#         )
# except FileNotFoundError:
#     print("Arquivo 'veiculos.json' não encontrado. Nenhum dado foi carregado.")

    def create(self):
        dados = self.lerJson(self.arquivo_json_carro) 
        veiculo = {}
        veiculo[self.placa] = {
                "id": self.id,
                "modelo": self.modelo,
                "marca": self.marca,
                "nome": self.nome,
                "ano": self.ano,
                "cor": self.cor,
                "placa": self.placa
            } 
        
        dados.update(veiculo)
        self.escreverJson(self.arquivo_json_carro, dados)
        
        print("")
        print("╔════════════════════════════════════════════════════╗")
        print("║        CADASTRO REALIZADO COM SUCESSO  ✅          ║")
        print("╚════════════════════════════════════════════════════╝")
        print("")
        print("Deseja realizar mais alguma operação em Cliente?")
        self.mainCars()

    def lerJson(self, arquivo):
        with open(arquivo, 'r', encoding = "utf-8") as j:
            return json.load(j)
    
    def escreverJson(self, arquivo, dados):
        with open(arquivo, 'w', encoding = "utf-8") as j:
            json.dump(dados, j, indent=4, ensure_ascii = False)

    