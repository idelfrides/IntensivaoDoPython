
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
import plotly.express as px

pyautogui.PAUSE = 1

from selenium import webdriver                   # controlar o navegador
from selenium.webdriver.common.keys import Keys  # contolar o teclado do seu pc
from selenium.webdriver.common.by import By      # localizar itens no navegador


GOOGLE_XPATH = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'

VALUE_XPATH = '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'

FILES_PATH = os.path.dirname(os.path.abspath(__file__))


def web_scraping_selenium():

    print('-'*80)
    print('\n WEBSCRAPING COM SELENIUM E ANALISE DA DADOS [ ongoing ] ... \n')
    print('-'*80)

    # passo 1: criar/abrir o browser
    browser = webdriver.Chrome()

    # passo 2: entrar no SITE DO GOOGLE  e pesguigar a cotação do DÓLAR
    browser.get('https://www.google.com/')

    browser.find_element(By.XPATH, GOOGLE_XPATH).send_keys('cotação do dólar')

    browser.find_element(By.XPATH, GOOGLE_XPATH).send_keys(Keys.ENTER)

    # passo 3: recuperar a cotação do dólar
    cotacao_dolar = browser.find_element(
        By.XPATH, VALUE_XPATH).get_attribute('data-value')

    # passo 4: entrar no SITE DO GOOGLE e pesguigar a cotação do EURO
    browser.get('https://www.google.com/')

    browser.find_element(By.XPATH, GOOGLE_XPATH).send_keys('cotação do euro')

    browser.find_element(By.XPATH, GOOGLE_XPATH).send_keys(Keys.ENTER)

    # passo 5: recuperar a cotação do EURO
    cotacao_euro = browser.find_element(
        By.XPATH, VALUE_XPATH).get_attribute('data-value')

    # passo 6: entrar no site da cotação do OURO, o site a seguir
    browser.get('https://www.melhorcambio.com/ouro-hoje')

    # passo 7: recuperar a cotação do OURO
    cotacao_ouro = browser.find_element(
        By.XPATH, '//*[@id="comercial"]').get_attribute('value')

    cotacao_ouro = cotacao_ouro.replace(',', '.')

    print(f'COTACAO DOLAR --> {cotacao_dolar}\n')
    print(f'COTACAO EURO --> {cotacao_euro}\n')
    print(f'COTACAO OURO --> {cotacao_ouro}\n')

    # passo 8: importar a base de dados
    try:
        real_path = '/'.join([FILES_PATH, 'utils', 'Produtos.xlsx'])
        product_content = pd.read_excel(real_path)
    except Exception as err:
        print(f'EXCEPTION: {err}')
        product_content = 'NO PRODUCT CONTENT'

    print(product_content)
    print(product_content.info())

    # passo 9: atulizar indicadores

        # a) atualizar as cotações
        # b) preco de compra = preco original * cotacao
        # c) preco de venda = preco de compra * * margem

    product_content.loc[product_content['Moeda'] == 'Dólar', 'Cotação'] = float(cotacao_dolar)

    product_content.loc[product_content['Moeda'] == 'Euro', 'Cotação'] = float(cotacao_euro)

    product_content.loc[product_content['Moeda'] == 'Ouro', 'Cotação'] = float(cotacao_ouro)

    # b) preco de compra = preco original * cotacao
    product_content['Preço de Compra'] = (
        product_content['Preço Original'] * product_content['Cotação']
    )

    # c) preco de venda = preco de compra * margem
    product_content['Preço de Venda'] = (
        product_content['Preço de Compra'] * product_content['Margem']
    )

    # passo 10: export a base de dados atualizada
    real_path = '/'.join([FILES_PATH, 'utils', 'Produtos_new.xlsx'])
    product_content.to_excel(real_path, index=False)

    print('EXPORT FILE DONE')
    print('\n DONE \n')

    return
