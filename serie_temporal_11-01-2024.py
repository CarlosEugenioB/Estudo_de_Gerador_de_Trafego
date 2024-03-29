# -*- coding: utf-8 -*-
"""Serie_Temporal_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YeNISyGchDlVOF807HF30y9oVkywToIF
"""

import pandas as pd
# Importa a biblioteca pandas para manipulação e análise de dados.

import matplotlib.pyplot as plt
# Importa a biblioteca matplotlib.pyplot para criação de gráficos.

import io
# Importa o módulo io para manipulação de streams de bytes (como arquivos).

from google.colab import files
# Importa a função de manipulação de arquivos do Google Colab.

# Solicita o upload do arquivo
print("Por favor, faça o upload de um arquivo .xlsx ou .csv")
uploaded = files.upload()
# Exibe uma mensagem solicitando o upload de um arquivo .xlsx ou .csv e usa a função upload do Colab para carregar o arquivo.

# Verifica se algum arquivo foi carregado
if uploaded:
    nome_do_arquivo = next(iter(uploaded))
    # Pega o nome do primeiro arquivo carregado.
    extensao = nome_do_arquivo.split('.')[-1]
    # Determina a extensão do arquivo.

    # Lê o conteúdo do arquivo usando o Pandas
    if extensao == 'xlsx':
        dados = pd.read_excel(io.BytesIO(uploaded[nome_do_arquivo]), engine='openpyxl')
    elif extensao == 'csv':
        dados = pd.read_csv(io.BytesIO(uploaded[nome_do_arquivo]))
    else:
        print("Formato de arquivo não suportado.")
        exit()
    # Lê o arquivo usando pandas. io.BytesIO é usado para ler o conteúdo binário do arquivo.
    # 'openpyxl' é a engine para ler arquivos .xlsx e 'pd.read_csv' para arquivos .csv.

    # Verifica se as colunas necessárias existem
    if 'DL_bitrate' in dados.columns and 'UL_bitrate' in dados.columns and 'Time' in dados.columns:
        # Plota o gráfico para DL_bitrate
        plt.figure(figsize=(10, 5))
        plt.plot(dados['Time'], dados['DL_bitrate'], color='blue', label='DL_bitrate')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Taxa de Transmissão DL (Mbps)')
        plt.title('Taxa de Transmissão de Download ao Longo do Tempo')
        # Cria um gráfico de linha para a taxa de transmissão de download (DL_bitrate) ao longo do tempo.

        # Plota o gráfico para UL_bitrate
        plt.figure(figsize=(10, 5))
        plt.plot(dados['Time'], dados['UL_bitrate'], color='red', label='UL_bitrate')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Taxa de Transmissão UL (Mbps)')
        plt.title('Taxa de Transmissão de Upload ao Longo do Tempo')
        # Cria um gráfico de linha para a taxa de transmissão de upload (UL_bitrate) ao longo do tempo.

        # Plota um terceiro gráfico combinando DL e UL
        plt.figure(figsize=(10, 5))
        plt.scatter(dados['Time'], dados['DL_bitrate'], color='blue', label='DL_bitrate', s=10)
        plt.scatter(dados['Time'], dados['UL_bitrate'], color='red', label='UL_bitrate', s=10)
        plt.xlabel('Tempo (s)')
        plt.ylabel('Taxa de Transmissão (Mbps)')
        plt.title('Taxa de Transmissão de Download e Upload ao Longo do Tempo')
        plt.legend()
        plt.show()
        # Cria um gráfico de dispersão combinando as taxas de transmissão de download e upload ao longo do tempo.
    else:
        print("As colunas necessárias (DL_bitrate, UL_bitrate, Time) não foram encontradas no arquivo.")
        # Imprime uma

