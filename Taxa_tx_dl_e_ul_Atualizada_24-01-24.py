# -*- coding: utf-8 -*-
"""Calculando_Taxa_Tx_Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z1GPdouPoQryIjGoClPLwmL7NVAoIVHJ
"""

# Importa as bibliotecas necessárias
import pandas as pd                 # Importa a biblioteca Pandas para manipulação de dados (Planilha Excel)
import matplotlib.pyplot as plt     # Importa a biblioteca Matplotlib para plotagem de gráficos
import io                           # Importa o módulo io para manipulação de fluxos de dados
from google.colab import files     # Importa a biblioteca para carregar arquivos no ambiente Colab (https://colab.research.google.com/drive)

# Solicita o upload do arquivo
print("Por favor, faça o upload de um arquivo .xlsx")
uploaded = files.upload()  # Solicita ao usuário que faça o upload de um arquivo .xlsx

# Verifica se algum arquivo foi carregado
if uploaded:
    nome_do_arquivo = next(iter(uploaded))  # Obtém o nome do arquivo carregado
    extensao = nome_do_arquivo.split('.')[-1]  # Obtém a extensão do arquivo

    # Lê o conteúdo do arquivo usando o Pandas
    if extensao == 'xlsx':  # Verifica se a extensão do arquivo é .xlsx
        dados = pd.read_excel(io.BytesIO(uploaded[nome_do_arquivo]))  # Lê o arquivo .xlsx usando Pandas

        # Ajusta a opção de exibição do Pandas para mostrar todas as linhas
        pd.set_option('display.max_rows', None)  # Configura o Pandas para exibir todas as linhas do DataFrame

        # Verifica se as colunas necessárias existem
        if 'DL_bitrate' in dados.columns and 'UL_bitrate' in dados.columns and 'Time' in dados.columns:
            # Calcula as taxas de transmissão para DL e UL
            dados['DL_bitrate'] = dados['DL_bitrate'] * 8 / 1e6  # Converte os valores de DL para Mbps
            dados['UL_bitrate'] = dados['UL_bitrate'] * 8 / 1e6  # Converte os valores de UL para Mbps

            # Converte a coluna 'Time' para o formato de datetime
            dados['Time'] = pd.to_datetime(dados['Time'])

            # Calcula o número de segundos desde o início do tempo
            dados['Seconds'] = dados['Time'].sub(dados['Time'].iloc[0]).dt.total_seconds()

            # Cria a coluna 'Frame/s' usando os segundos e ajusta a vírgula
            dados['Frame/s'] = (dados['Seconds'] * 1000).round(3)  # Multiplica por 1000 e arredonda para 3 casas decimais
            dados['Frame/s'] = (dados['Frame/s'] * 10).round(2)

            # Plota o gráfico para DL_bitrate como pontos
            plt.figure(figsize=(10, 5))  # Define o tamanho da figura
            plt.scatter(dados['Time'], dados['DL_bitrate'], color='blue', label='DL_bitrate', s=10)  # Plota os pontos DL_bitrate
            plt.xlabel('Tempo (s)')  # Define o rótulo do eixo x
            plt.ylabel('Taxa de Transmissão DL (Mbps)')  # Define o rótulo do eixo y
            plt.title('Taxa de Transmissão de Download ao Longo do Tempo')  # Define o título do gráfico

            # Plota o gráfico para UL_bitrate como pontos
            plt.figure(figsize=(10, 5))  # Define o tamanho da figura
            plt.scatter(dados['Time'], dados['UL_bitrate'], color='red', label='UL_bitrate', s=10)  # Plota os pontos UL_bitrate
            plt.xlabel('Tempo (s)')  # Define o rótulo do eixo x
            plt.ylabel('Taxa de Transmissão UL (Mbps)')  # Define o rótulo do eixo y
            plt.title('Taxa de Transmissão de Upload ao Longo do Tempo')  # Define o título do gráfico

            # Plota um terceiro gráfico combinando DL e UL como pontos
            plt.figure(figsize=(10, 5))  # Define o tamanho da figura
            plt.scatter(dados['Time'], dados['DL_bitrate'], color='blue', label='DL_bitrate', s=10)  # Plota os pontos DL_bitrate
            plt.scatter(dados['Time'], dados['UL_bitrate'], color='red', label='UL_bitrate', s=10)  # Plota os pontos UL_bitrate
            plt.xlabel('Tempo (s)')  # Define o rótulo do eixo x
            plt.ylabel('Taxa de Transmissão (Mbps)')  # Define o rótulo do eixo y
            plt.title('Taxa de Transmissão de Download e Upload ao Longo do Tempo')  # Define o título do gráfico
            plt.legend()  # Adiciona a legenda ao gráfico

            # Calcula a taxa de transmissão total (DL + UL)
            dados['Total_bitrate'] = dados['DL_bitrate'] + dados['UL_bitrate']

            # Plota um quarto gráfico com a taxa de transmissão total
            plt.figure(figsize=(10, 5))  # Define o tamanho da figura
            plt.scatter(dados['Time'], dados['Total_bitrate'], color='purple', label='Total_bitrate', s=10)  # Plota os pontos Total_bitrate
            plt.xlabel('Tempo (s)')  # Define o rótulo do eixo x
            plt.ylabel('Taxa de Transmissão Total (Mbps)')  # Define o rótulo do eixo y
            plt.title('Taxa de Transmissão Total (DL + UL) ao Longo do Tempo')  # Define o título do gráfico
            plt.legend()  # Adiciona a legenda ao gráfico

            # Exibe a tabela com os valores de taxa de transmissão e Frame/s
            print("\nTabela de Taxa de Transmissão:")
            print(dados[['Time', 'Frame/s', 'DL_bitrate', 'UL_bitrate', 'Total_bitrate']])  # Imprime a tabela de dados
        else:
            print("As colunas necessárias (DL_bitrate, UL_bitrate, Time) não foram encontradas no arquivo.")
    else:
        print("Formato de arquivo não suportado.")
else:
    print("Nenhum arquivo foi carregado.")