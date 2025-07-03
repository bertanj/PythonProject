import openpyxl
import pandas as pd

def concatenar_emails_excel(caminho_arquivo_excel, nome_coluna_email):
    """
    Lê e-mails de um arquivo Excel e os concatena com um ponto e vírgula como separador.

    Args:
        caminho_arquivo_excel (str): O caminho completo para o arquivo Excel.
        nome_coluna_email (str): O nome da coluna que contém os endereços de e-mail.

    Returns:
        str: Uma string contendo todos os e-mails concatenados, separados por ponto e vírgula.
             Retorna uma string vazia se nenhum e-mail for encontrado ou se o arquivo/coluna for inválido.
    """
    try:
        # Carrega o arquivo Excel em um DataFrame do pandas
        # Use a variável caminho_arquivo_excel aqui
        df = pd.read_excel(caminho_arquivo_excel)

        # Verifica se a coluna de e-mail existe no DataFrame
        # Use a variável nome_coluna_email aqui
        if nome_coluna_email not in df.columns:
            print(f"Erro: A coluna '{nome_coluna_email}' não foi encontrada no arquivo Excel.")
            return ""

        # Seleciona a coluna de e-mails, remove valores nulos e converte para string
        # Use a variável nome_coluna_email aqui
        emails = df[nome_coluna_email].dropna().astype(str)

        # Concatena os e-mails com ';'
        emails_concatenados = ";".join(emails)

        return emails_concatenados

    except FileNotFoundError:
        # Use a variável caminho_arquivo_excel aqui
        print(f"Erro: O arquivo '{caminho_arquivo_excel}' não foi encontrado.")
        return ""
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return ""

    # Define o nome do seu arquivo Excel e o nome da coluna de e-mails
    # Como o arquivo está na mesma pasta, basta o nome do arquivo.
    caminho_do_seu_excel = 'clinicas_brasil.xlsx'
    nome_da_coluna_de_email = 'EMAIL'

    # Chama a função para concatenar os e-mails
    lista_de_emails = concatenar_emails_excel(caminho_do_seu_excel, nome_da_coluna_de_email)

    # Imprime o resultado
    if lista_de_emails:
        print("\nE-mails concatenados:")
        print(lista_de_emails)

        nome_arquivo_txt = 'emails_concatenados.txt'
        with open(nome_arquivo_txt, 'w', encoding='utf-8') as f:
            f.write(lista_de_emails)
        print(f"E-mails salvos em '{nome_arquivo_txt}' com sucesso!")

    else:
        print("\nNão foi possível obter os e-mails ou nenhum e-mail foi encontrado.")