
"""

DESAFIO: recuperar as cotações atualizadas de Dólar, do Euro e do Ouro e atualizar os valores de compra e vendas de produtos.

-----------------------------------------------------------

ESCREVER O PASSO-A-PASSO  EM PORTUGUÊS

passo 1: criar/abrir o browser
passo 2: entrar no SITE DO GOOGLE  e pesguigar a cotação do DÓLAR
passo 3: recuperar a cotação do dólar

passo 4: entrar no SITE DO GOOGLE e pesguigar a cotação do EURO
passo 5: recuperar a cotação do EURO

passo 6: entrar no navegador e pesguigar a cotação do OURO no site a seguir

--> https://www.melhorcambio.com/ouro-hoje

passo 7: recuperar a cotação do OURO

passo 8: import a base de dados

passo 9: atulizar indicadores
    a) atualizar as cotações
    b) preco de compra = preco original * cotacao
    c) preco de venda = preco de compra * * margem

passo 10: export a base de dados atualizada


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
import matplotlib.pyplot as plt
import seaborn as sns   # lib created using matplotbib
import plotly.express as px

pyautogui.PAUSE = 1

from selenium import webdriver                   # controlar o navegador
from selenium.webdriver.common.keys import Keys  # contolar o teclado do seu pc
from selenium.webdriver.common.by import By      # localizar itens no navegador


FILES_PATH = os.path.dirname(os.path.abspath(__file__))


def data_science_AI():
    print('\n\n DATA SCIENTE AND ARTIFICIAL INTELIGENCE PROJECT [ ongoing ] ...')

    # passo 1: importar a base de dados
    try:
        real_path = '/'.join([FILES_PATH, 'utils', 'advertising.csv'])
        ads_content = pd.read_csv(real_path)
    except Exception as err:
        print(f'EXCEPTION: {err}')
        ads_content = 'NO ADVERTISING CONTENT'

    print(ads_content)
    print(ads_content.info())

    # passo 9: atulizar indicadores

        # a) atualizar as cotações
        # b) preco de compra = preco original * cotacao
        # c) preco de venda = preco de compra * * margem

    # product_content.loc[linhas, colunas] = valor_atualizado
    '''
    product_content.loc[product_content['Moeda'] == 'Dólar', 'Cotação'] = float(cotacao_dolar)

    product_content.loc[product_content['Moeda'] == 'Euro', 'Cotação'] = float(cotacao_euro)

    product_content.loc[product_content['Moeda'] == 'Ouro', 'Cotação'] = float(cotacao_ouro)

    # b) preco de compra = preco original * cotacao
    product_content['Preço de Compra'] = (
        product_content['Preço Original'] * product_content['Cotação']
    )

    # c) preco de venda = preco de compra * margem
    product_content['Preço de Venda'] = (
        product_content['Preço de Compra'] * product_content['Mrgem']
    )

    # print(product_content)

    # passo 10: export a base de dados atualizada
    real_path = '/'.join([FILES_PATH, 'utils', 'Produtos_new.xlsx'])
    product_content.to_excel(real_path, index=False)

    print('EXPORT FILE DONE')
    print('\n DONE \n')
    '''