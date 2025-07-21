import openpyxl
import pandas as pd

def concatenar_emails_excel(caminho_arquivo_excel, nome_coluna_email):

    try:
        # Carrega o arquivo Excwel em um DataFrame
        df = pd.read_excel(caminho_arquivo_excel)

        # Verifica se a coluna de e-mail existe no DF
        if nome_coluna_email not in df.columns:
            print(f"Erro: A coluna '{nome_coluna_email}' não foi encontrada no arquivo Excel.")
            return ""

        # Seleciona a coluna de e-mails, remove valores nulos e converte para string
        emails = df[nome_coluna_email].dropna().astype(str)

        # Concatena os emails com ';'
        emails_concatenados = ";".join(emails)

        return emails_concatenados

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo_excel}' não foi encontrado.")
        return ""
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return ""

    # Define o nome do Excel e o nome da coluna de email
    caminho_excel = 'clinicas_brasil.xlsx'
    coluna = 'EMAIL'

    # Chama a função para concatenar os emails
    lista_de_emails = concatenar_emails_excel(caminho_excel, coluna)

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
