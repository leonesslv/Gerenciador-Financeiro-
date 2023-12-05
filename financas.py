import json
import time

class Financas:
    def __init__(self):
        self.receitas = []  # Inicializa a lista de receitas como vazia
        self.despesas = []  # Inicializa a lista de despesas como vazia
        self.carregar_dados()  # Carrega dados existentes do arquivo quando uma instância da classe é criada



    def carregar_dados(self):
        try:
            with open("dados_financas.json", "r") as arquivo:
                dados = json.load(arquivo)  # Tenta carregar dados do arquivo JSON
                self.receitas = dados.get("receitas", [])  # Atualiza as receitas com dados do arquivo ou inicializa como uma lista vazia
                self.despesas = dados.get("despesas", [])  # Atualiza as despesas com dados do arquivo ou inicializa como uma lista vazia
        except FileNotFoundError:
            print("Arquivo de dados não encontrado. Iniciando com listas vazias.")  # Informa que o arquivo não foi encontrado e que as listas foram iniciadas vazias


    def salvar_dados(self):
        try:
            with open("dados_financas.json", "w") as arquivo:
                dados = {"receitas": self.receitas, "despesas": self.despesas}  # Cria um dicionário com as listas de receitas e despesas
                json.dump(dados, arquivo)  # Salva os dados no arquivo JSON
        except Exception as e:
            print(f"Erro ao salvar os dados: {e}")  # Informa se ocorrer um erro ao tentar salvar os dados
    
    
    
    def cadastrar_receita(self, descricao, valor, data=None):
        if data is None:
            data = time.strftime("%d-%m-%Y")  # Obtém a data atual no formato DD-MM-YYYY

        receita = {"Descrição": descricao, "Valor": valor, "Data": data}
        self.receitas.append(receita)  # Adiciona uma nova receita à lista de receitas
        print("Receita cadastrada com sucesso!")  # Exibe uma mensagem informando que a receita foi cadastrada com sucesso
    

    def cadastrar_despesa(self, descricao, valor, data=None):
        if data is None:
            data = time.strftime("%d-%m-%Y")  # Obtém a data atual no formato DD-MM-YYYY

        despesa = {"Descrição": descricao, "Valor": valor, "Data": data}
        self.despesas.append(despesa)  # Adiciona uma nova despesa à lista de despesas
        print("Despesa cadastrada com sucesso!")  # Exibe uma mensagem informando que a despesa foi cadastrada com sucesso


    def pesquisar_por_nome(self, lista, nome):
        resultados = [item for item in lista if nome.lower() in item["Descrição"].lower()]  # Filtra os itens da lista com base no nome fornecido, ignorando maiúsculas e minúsculas
        if resultados:
            print(f"Resultados para '{nome}':")
            for i, resultado in enumerate(resultados, start=1):  # Exibe os resultados numerados
                print(f"{i}. Descrição: {resultado['Descrição']}, Valor: {resultado['Valor']}")
        else:
            print(f"Nenhum resultado encontrado para '{nome}'.")  # Exibe uma mensagem se nenhum resultado for encontrado


    def pesquisar_receitas(self, nome):
        if not self.receitas:
            print("Nenhuma receita cadastrada.")  # Exibe uma mensagem se não houver receitas cadastradas
        else:
            self.pesquisar_por_nome(self.receitas, nome)  # Chama o método para pesquisar receitas por nome


    def pesquisar_despesas(self, nome):
        if not self.despesas:
            print("Nenhuma despesa cadastrada.")  # Exibe uma mensagem se não houver despesas cadastradas
        else:
            self.pesquisar_por_nome(self.despesas, nome)  # Chama o método para pesquisar despesas por nome


    def exibir_lista(self, lista, tipo):
        if not lista:
            print(f"Nenhuma {tipo} cadastrada.")  # Exibe uma mensagem se a lista estiver vazia
        else:
            print(f"Lista de {tipo}s:")
            for i, item in enumerate(lista, start=1):  # Exibe os itens da lista numerados
                print(f"{i}. Descrição: {item['Descrição']}, Valor: {item['Valor']}")


    def excluir_receita(self, indice):
        self.exibir_lista(self.receitas, "Receita")  # Exibe a lista de receitas antes de excluir
        try:
            del self.receitas[indice]  # Tenta excluir a receita com o índice fornecido
            print("Receita excluída com sucesso!")  # Exibe uma mensagem indicando que a receita foi excluída com sucesso
        except IndexError:
            print("Índice inválido. Não foi possível excluir a receita.")  # Exibe uma mensagem se o índice fornecido for inválido


    def excluir_despesa(self, indice):
        self.exibir_lista(self.despesas, "Despesa")  # Exibe a lista de despesas antes de excluir
        try:
            del self.despesas[indice]  # Tenta excluir a despesa com o índice fornecido
            print("Despesa excluída com sucesso!")  # Exibe uma mensagem indicando que a despesa foi excluída com sucesso
        except IndexError:
            print("Índice inválido. Não foi possível excluir a despesa.")  # Exibe uma mensagem se o índice fornecido for inválido



    def calcular_gastos(self):
        total_despesa = sum(item["Valor"] for item in self.despesas)
        return total_despesa

    def calcular_total_receita(self):
        total_receita = sum(item["Valor"] for item in self.receitas)
        return total_receita

    def listar_receitas(self):
        print("\nLista de Receitas:")
        for i, receita in enumerate(self.receitas, start=1):
            print(f"{i}. Descrição: {receita['Descrição']}, Valor: R$ {receita['Valor']:.2f}, Data: {receita['Data']}")

    def listar_despesas(self):
        print("\nLista de Despesas:")
        for i, despesa in enumerate(self.despesas, start=1):
            print(f"{i}. Descrição: {despesa['Descrição']}, Valor: R$ {despesa['Valor']:.2f}, Data: {despesa['Data']}")