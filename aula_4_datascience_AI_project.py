
"""

DESAFIO: recuperar as cotações atualizadas de Dólar, do Euro e do Ouro e atualizar os valores de compra e vendas de produtos.

-----------------------------------------------------------

ESCREVER O PASSO-A-PASSO  EM PORTUGUÊS

Passo a Passo de um Projeto de Ciência de Dados

- Passo 1: Entendimento do Desafio
- Passo 2: Entendimento da Área/Empresa
- Passo 3: Extração/Obtenção de Dados
- Passo 4: Ajuste de Dados (Tratamento/Limpeza)
- Passo 5: Análise Exploratória
- Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)
- Passo 7: Interpretação de Resultados


SELENIUM

- funciona em segundo plano, enquanto vc está realizando outras tarefas
- funciona independente de mudança de posionamento de elementos na sua tela
- funciona independente da resolução da tela do seu laptop
-

-------------------------------------------------------------------------------
"""

import os
import time
import pyautogui
import pyperclip
import pandas as pd

# python package for building chart

import matplotlib.pyplot as plt    # the main one
import seaborn as sns              # lib created using matplotbib
import plotly.express as px        #

pyautogui.PAUSE = 1

from selenium import webdriver                   # controlar o navegador
from selenium.webdriver.common.keys import Keys  # contolar o teclado do seu pc
from selenium.webdriver.common.by import By      # localizar itens no navegador


FILES_PATH = os.path.dirname(os.path.abspath(__file__))


def data_science_AI():
    print('\n\n DATA SCIENTE AND AI PROJECT [ ongoing ] ...')

    # passo 1 | passo 2: all done
    # passo 3: done

    try:
        real_path = '/'.join([FILES_PATH, 'utils', 'advertising.csv'])
        ads_content = pd.read_csv(real_path)
    except Exception as err:
        print(f'EXCEPTION: {err}')
        ads_content = 'NO ADVERTISING CONTENT'

    print(ads_content)
    print(ads_content.info())

    # Passo 4: Ajuste de Dados (Tratamento/Limpeza)  done

    # Passo 5: Análise Exploratória

        # a) visualizar como as informações de cada item são distribuídas
        # b) ver a correlação entre cada um dos itens

    sns.heatmap(ads_content.corr(), cmap='Wistia', annot=True)
    plt.show()

    # passo 6:Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)

    # prapare content for training  and testing our AI

    

    print('DONE')
