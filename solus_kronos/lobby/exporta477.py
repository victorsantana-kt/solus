import os
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from datetime import datetime
def exporta477():
    
    
    print("----------> INICIANDO EXPORTAÇÃO 477")
    # Configurando o pandas para exibir mais linhas
    pd.set_option('display.max_rows', 100)

    # Definindo a pasta de origem dos arquivos Excel
    pasta = 'C:/477'

    # Função para listar e filtrar arquivos .xlsx que começam com '477'
    def filtrar_arquivos(diretorio):
        for arquivo in os.listdir(diretorio):
            if arquivo.startswith('477') and arquivo.lower().endswith('.xlsx'):
                yield os.path.join(diretorio, arquivo)

    # Inicializando um DataFrame vazio para o resultado final
    df_final = pd.DataFrame()

    # Processando cada arquivo na pasta especificada
    for caminho_arquivo in filtrar_arquivos(pasta):
        df_temp = pd.read_excel(caminho_arquivo, header=1)
        df_final = pd.concat([df_final, df_temp], ignore_index=True)

    # Função para converter com segurança os valores para o tipo desejado
    def converter_com_seguranca(valor, tipo):
        try:
            if pd.isna(valor):
                return np.nan
            elif tipo == 'Int64':
                return pd.to_numeric(valor, errors='coerce', downcast='integer')
            elif tipo == 'datetime64[ns]':
                return pd.to_datetime(valor, errors='coerce')
            elif tipo == 'float':
                return float(valor)
            elif tipo == 'object':
                return str(valor)
            else:
                return valor
        except (ValueError, TypeError):
            return np.nan

    # Mudando os tipos de dados das colunas especificadas
    tipos = {
        "3": 'Int64', 
        "NUMLANCTO": 'object', 
        "PARCELA": 'object', 
        "EVENTO": 'object', 
        "DESCR EVENTO": 'object', 
        "HISTORICO DA DESPESA": 'object', 
        "CNPJ FORNECEDOR": 'object', 
        "NOME FORNECEDOR": 'object', 
        "MUNICIPIO FORNECEDOR": 'object', 
        "UF FORNECEDOR": 'object', 
        "BCO/AGENCIA/CONTA FORNECEDOR": 'object', 
        "CNPJ FAVORECIDO": 'object', 
        "NOME FAVORECIDO": 'object', 
        "ESPECIALIDADE": 'object', 
        "RNTRC": 'object', 
        "CTA CTB DEB": 'Int64', 
        "CTA CTB CRED": 'Int64', 
        "NFISCAL": 'Int64', 
        "CHAVE NFISCAL": 'float', 
        "VALOR TOTAL PRODUTOS": 'float', 
        "VLR NOTA": 'float', 
        "VLR PARCELA": 'float', 
        "JUROS": 'Int64', 
        "DESCONTOS": 'float', 
        "VLR FINAL": 'float', 
        "INCLUSAO": 'datetime64', 
        "LOGIN": 'object', 
        "VENCIMEN": 'datetime64', 
        "EMISSAO": 'datetime64', 
        "DATA PGTO": 'datetime64', 
        "APROVACAO": 'object', 
        "CONTABIL": 'datetime64', 
        "UNI": 'object', 
        "SIT DES": 'object', 
        "ARQ REMESSA": 'object', 
        "ARQ": 'object', 
        "COD BAR BLOQUETO": 'Int64', 
        "CFOP": 'Int64', 
        "GRUPO EVENTO": 'object', 
        "MES COMPETENCIA": 'datetime64'
    }
    for coluna, tipo_str in tipos.items():
        if coluna in df_final.columns:
            df_final[coluna] = df_final[coluna].apply(lambda x: converter_com_seguranca(x, tipo_str))

    # Filtrando as linhas onde a coluna 'NUMLANCTO' é diferente de 'NUMLANCTO'
    df_final = df_final[df_final['NUMLANCTO'] != "NUMLANCTO"]

    # Aplicando filtros adicionais
    df_final = df_final[(df_final['EVENTO'] != 5442) & 
                        (df_final['SIT DES'] != "CANC") & 
                        (df_final[3] == 5) &
                        (df_final['PARCELA'] == "1")]

    # Renomeando as colunas do DataFrame
    df_final.rename(columns={
        'NUMLANCTO': 'NUMLANCTO',
        'PARCELA': 'PARCELA',
        'EVENTO': 'EVENTO',
        'DESCR EVENTO': 'DESCR_EVENTO',
        'HISTORICO DA DESPESA': 'HISTORICO_DA_DESPESA',
        'CNPJ FORNECEDOR': 'CNPJ_FORNECEDOR',
        'NOME FORNECEDOR': 'NOME_FORNECEDOR',
        'MUNICIPIO FORNECEDOR': 'MUNICIPIO_FORNECEDOR',
        'UF FORNECEDOR': 'UF_FORNECEDOR',
        'BCO/AGENCIA/CONTA FORNECEDOR': 'BCO_AGENCIA_CONTA_FORNECEDOR',
        'CNPJ FAVORECIDO': 'CNPJ_FAVORECIDO',
        'NOME FAVORECIDO': 'NOME_FAVORECIDO',
        'ESPECIALIDADE': 'ESPECIALIDADE',
        'RNTRC': 'RNTRC',
        'CTA CTB DEB': 'CTA_CTB_DEB',
        'CTA CTB CRED': 'CTA_CTB_CRED',
        'NFISCAL': 'NFISCAL',
        'CHAVE NFISCAL': 'CHAVE_NFISCAL',
        'VALOR TOTAL PRODUTOS': 'VALOR_TOTAL_PRODUTOS',
        'VLR NOTA': 'VLR_NOTA',
        'VLR PARCELA': 'VLR_PARCELA',
        'JUROS': 'JUROS',
        'DESCONTOS': 'DESCONTOS',
        'VLR FINAL': 'VLR_FINAL',
        'INCLUSAO': 'INCLUSAO',
        'LOGIN': 'LOGIN',
        'VENCIMEN': 'VENCIMEN',
        'EMISSAO': 'EMISSAO',
        'DATA PGTO': 'DATA_PGTO',
        'APROVACAO': 'APROVACAO',
        'CONTABIL': 'CONTABIL',
        'UNI': 'UNI',
        'SIT DES': 'SIT_DES',
        'ARQ REMESSA': 'ARQ_REMESSA',
        'ARQ': 'ARQ',
        'COD BAR BLOQUETO': 'COD_BAR_BLOQUETO',
        'CFOP': 'CFOP',
        'GRUPO EVENTO': 'GRUPO_EVENTO',
        'MES COMPETENCIA': 'MES_COMPETENCIA'
    }, inplace=True)

    # Convertendo NFISCAL para inteiro antes da concatenação
    df_final['NFISCAL'] = df_final['NFISCAL'].fillna(0).astype(int)

    # Usando str.strip() e str.replace() para remover espaços do início, meio e fim dos valores
    df_final['cod'] = (df_final['NFISCAL'].astype(str).str.strip().str.replace(' ', '') + '_' + df_final['CNPJ_FORNECEDOR'].astype(str).str.strip().str.replace(' ', ''))

    data_hora_inclusao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df_final['DataHoraInclusao'] = data_hora_inclusao

    # Parâmetros de conexão ao banco de dados MySQL
    usuario = 'root'
    senha = 'auto.sup'
    host = 'localhost'
    banco_de_dados = 'solus_db'
    nome_tabela = 'app477_bd477'

    # Criando uma conexão com o banco de dados
    engine = create_engine(f'mysql+mysqlconnector://{usuario}:{senha}@{host}/{banco_de_dados}')

    # Criando a tabela no banco de dados e inserindo os dados
    df_final.to_sql(nome_tabela, con=engine, if_exists='replace', index=False)

    print("Dados inseridos com sucesso na tabela MySQL.")

    # Exibindo as primeiras linhas do DataFrame final para verificação
    print(df_final.head())
