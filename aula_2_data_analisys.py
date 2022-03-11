
"""
ESCREVER O PASSO-A-PASSO  EM PORTUGUÊS
----------------------------------------

passo 1: importar a base de dados para o python
passo 2: visualisar as informaçoes da base de dados
    objetivo 1: analisar e entender os dados existentes na base de dados
    objetivo 2: descobrir os erros (problemas) existentes na sua base de dados
passo 3: tratamento dos dados
passo 4: análise inicial / análise global (abordagem: top-down )
passo 5: análise detalhada ( buscar a causa/ a solução dos cancelamentos)

"""

# pyautogui -> automatiza o mouse, teclado e o seu tela
# pypercli
# sempre q foi trabalhar com base de dados, usar pandas
# pandas, numpy, openpyxl

# --------------------------------------------------------------------------


import os
import pdb
import time
import pyautogui
import pyperclip
import pandas as pd
import plotly.express as px
import glob

pyautogui.PAUSE = 1


def data_analisys():

    print('-'*80)
    print('\n PROJETO DE ANALISE DADOS COM PANDAS [ ongoing ] ... \n')
    print('-'*80)

    # -----------------------------------------------------------------
    # passo 1: importar a base de dados para o python
    # -----------------------------------------------------------------

    try:
        telecom_content = pd.read_csv(r'/media/ijdev/DATA/PROFISSIONAL/IntensivaoDoPython/utils/telecom_users.csv')
    except Exception as err:
        print(f'EXCEPTION: {err}')
        telecom_content = 'NO TELECOM CONTENT'

    print(telecom_content)

    # ------------------------------------------------------------
    # passo 2: visualisar as informaçoes da base de dados
    # ------------------------------------------------------------
    # Na análise de dados, o q não te ajuda, irá te atrapalhar

    # axis = 0 --> linha
    # axis = 1 --> coluna

    # -------------------------------------------------------------
    # passo 3: tratamento dos dados
    # -------------------------------------------------------------
    # analisar se o python está lendo os dados de forma correta

    telecom_content = telecom_content.drop('Unnamed: 0', axis=1)
    telecom_content = telecom_content.dropna(axis=1, how='all')
    telecom_content = telecom_content.dropna(axis=0, how='any')

    telecom_content['TotalGasto'] = pd.to_numeric(
        telecom_content['TotalGasto'], errors='coerce')


    # ----------------------------------------------------------------------
    # passo 4: análise inicial / análise global (abordagem: top-down )
    # ----------------------------------------------------------------------

    print(telecom_content['Churn'].value_counts())
    print(telecom_content['Churn'].value_counts(normalize=True).map("{:.2}%".format))


    # ----------------------------------------------------------------
    # passo 5: análise detalhada
    # (buscar a causa/ a solução dos cancelamentos)
    # ----------------------------------------------------------------
    #  por definicao, histograma aplica y --> cquantidade de clientes

    for column in telecom_content.columns:

        print(f'\n SHOWING CHART --> {column}...\n ')

        # etapa 1: criar o gráfico
        chart = px.histogram(telecom_content, x=column, color='Churn')

        # etapa 2: mostrar o gráfico no browser padrão do seu sistema operacional
        chart.show()
        time.sleep(1)


    # CONCLUSÕES:

    '''
    1 -


    '''

    print('DONE')

    return
