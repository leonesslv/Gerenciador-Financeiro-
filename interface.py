import PySimpleGUI as sg
from financas import Financas
import time
sg.theme('LightBlue')

def main():
    financas = Financas()

    button_size = (50, 2)  # Define o tamanho dos botões

    layout = [
    [sg.Text("Menu", size=(15, 1), justification='', font=('Arial', 20))],
    [sg.Column([
        [sg.Button("Cadastrar Receita", key="cad_receita", size=button_size)],
        [sg.Button("Cadastrar Despesa", key="cad_despesa", size=button_size)],
        [sg.Button("Pesquisar Receitas", key="pesq_receitas", size=button_size)],
        [sg.Button("Pesquisar Despesas", key="pesq_despesas", size=button_size)],
        [sg.Button("Excluir Receita", key="excluir_receita", size=button_size)],
        [sg.Button("Excluir Despesa", key="excluir_despesa", size=button_size)],
        [sg.Button("Listar Receitas", key="listar_receitas", size=button_size)],
        [sg.Button("Listar Despesas", key="listar_despesas", size=button_size)],
        [sg.Button("Calcular Gastos", key="calcular_gastos", size=button_size)],
        [sg.Button("Calcular Receita Total", key="calcular_receita_total", size=button_size)],
        [sg.Text("", size=(50, 1), key="resultado", justification='center', font=('Arial', 12))],
        [sg.Button("Salvar e Sair", key="salvar_sair", size=button_size)],
    ], element_justification='center')]
]
    window = sg.Window("Gerenciador Financeiro", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "salvar_sair":
            financas.salvar_dados()
            print("Dados salvos. Encerrando o programa.")
            break

        if event == "cad_receita":
         descricao = sg.popup_get_text("Digite a descrição da receita:")
         if descricao is not None:  # Verifica se o usuário pressionou "Cancelar"
             valor_texto = sg.popup_get_text("Digite o valor da receita:")
             data_texto_receita = sg.popup_get_text("Digite a data da receita:")
             if valor_texto is not None:  # Verifica se o usuário pressionou "Cancelar"
                    try:
                        valor = float(valor_texto)
                        financas.cadastrar_receita(descricao, valor, data_texto_receita)
                    except ValueError:
                        sg.popup_error("Valor inválido. Digite um número válido.")
                        
        elif event == "cad_despesa":
            descricao = sg.popup_get_text("Digite a descrição da despesa:")
            if descricao is not None:  # Verifica se o usuário pressionou "Cancelar"
                valor_texto = sg.popup_get_text("Digite o valor da despesa:")
                data_texto_despesa = sg.popup_get_text("Digite a data da despesa:")
                if valor_texto is not None:  # Verifica se o usuário pressionou "Cancelar"
                    try:
                        valor = float(valor_texto)
                        financas.cadastrar_despesa(descricao, valor, data_texto_despesa)
                    except ValueError:
                        sg.popup_error("Valor inválido. Digite um número válido.")
                
        elif event == "pesq_receitas":
            nome_pesquisa = sg.popup_get_text("Digite o nome para pesquisa de receitas:")
            if nome_pesquisa is not None: # Verifica se o usuário pressionou "Cancelar"
                financas.pesquisar_receitas(nome_pesquisa)

        elif event == "pesq_despesas":
            nome_pesquisa = sg.popup_get_text("Digite o nome para pesquisa de despesas:")
            if nome_pesquisa is not None: # Verifica se o usuário pressionou "Cancelar"
                financas.pesquisar_despesas(nome_pesquisa)

        elif event == "excluir_receita":
            financas.exibir_lista(financas.receitas, "Receita")
    
            if financas.receitas:  # Verifica se a lista de receitas não está vazia
             indice_texto = sg.popup_get_text("Digite o índice da receita a ser excluída:")
        
            if indice_texto is not None:  # Verifica se o usuário pressionou "Cancelar"
                try:
                    indice = int(indice_texto)
                    
                    # Verifica se o índice é válido
                    if 1 <= indice <= len(financas.receitas):
                        confirmacao = sg.popup_yes_no(f"Tem certeza que deseja excluir a receita {indice}?")

                        if confirmacao == "Yes":
                            financas.excluir_receita(indice - 1)
                    else:
                        sg.popup_error("Índice inválido. Digite um índice válido.")
                except ValueError:
                    sg.popup_error("Índice inválido. Digite um número inteiro válido.")
    

        elif event == "excluir_despesa":
            financas.exibir_lista(financas.despesas, "Despesa")

            if financas.despesas:  # Verifica se a lista de despesas não está vazia
                indice_texto = sg.popup_get_text("Digite o índice da despesa a ser excluída:")

                if indice_texto is not None:  # Verifica se o usuário pressionou "Cancelar"
                    try:
                        indice = int(indice_texto)

                        # Verifica se o índice é válido
                        if 1 <= indice <= len(financas.despesas):
                            confirmacao = sg.popup_yes_no(f"Tem certeza que deseja excluir a despesa {indice}?")

                            if confirmacao == "Yes":
                                financas.excluir_despesa(indice - 1)
                        else:
                            sg.popup_error("Índice inválido. Digite um índice válido.")
                    except ValueError:
                        sg.popup_error("Índice inválido. Digite um número inteiro válido.")



        elif event == "listar_receitas":
            lista_receitas = financas.listar_receitas()

        elif event == "listar_despesas":
            lista_despesas = financas.listar_despesas()

        elif event == "calcular_gastos":
            total_despesa = financas.calcular_gastos()
            window["resultado"].update(f'Total de Despesas: R$ {total_despesa:.2f}')

        elif event == "calcular_receita_total":
            total_receita = financas.calcular_total_receita()
            window["resultado"].update(f'Total de Receita: R$ {total_receita:.2f}')

    window.close()

if __name__ == "__main__":
    main()
