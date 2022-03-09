# encoding: utf-8

"""
ESCREVER O PASSO-A-PASSO  EM PORTUGUÊS
----------------------------------------

passo 1: entrar no sistema da emprresa (um diretorio no drive)
passo 2: navegar no sistema ate encontar a base de dados
passo 3: exprovar a base de vendas
passo 4: calcular os indicadores (faturamento e quantidade de produtos vendidos )
passo 5: enviar um email pra a diretoria com os indicadores

"""

# pyautogui -> automatiza o mouse, teclado e o seu tela
# pypercli
# sempre q foi trabalhar com base de dados, usar pandas
# pandas, numpy, openpyxl

# --------------------------------------------------------------------------


import os
import time
from datetime import datetime
import pyautogui
import pyperclip
import pandas as pd
import glob

pyautogui.PAUSE = 1

CONTENT = u"""
HELLO, my people, tudo bem com vcs ?

Ontem, Terca-feira ( 2022-03-08 ) continuamos no INTENSIVÃO DO PYTHON com muita energia e muito conhecimento.
Está sendo espetacular. Bom demais.

CONTEÚDO:

#2 | DAY 2: Análise de dados com python.
Aplicação do dia trabalha/aplica os seguintes conhecimentos:

    - Extração de dados a partir de uma fonte
    - Importação para o ambiente de programação de python usando pandas
    - Tratamento de dados no ambiente de python com pandas
    - Apresentar os resultados em um gráficos utilizando o package PLOTLY

Proferido por Lira da #HASTAG Programacao

----
Postagem feita pela automacao do python.
DATE:  {}
----

#python #pandas #nalisededados #dataanalisys #automatização #plotly #dev #developer #works #learning


"""


def make_post_linkedin():

    # remove_data_files()
    # time.sleep(5)

    # -----------------------------------------------------------------
    # PASSO 1: entrar no sistema da emprresa (um diretorio no drive)
    # -----------------------------------------------------------------
    pyautogui.hotkey('Ctrl', 't')  #atalho abre uma nov aba

    pyperclip.copy('https://www.linkedin.com/feed/')

    pyautogui.hotkey('Ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(15)

    # ------------------------------------------------------------
    # PASSO 2: navegar no sistema ate encontar a base de dados
    # ------------------------------------------------------------

    # abrir diretorio exportar
    pyautogui.click(x=904, y=164, clicks=1)
    time.sleep(4)

    # print(pyautogui.position())

    # criar publicação
    pyautogui.click(x=837, y=264)
    time.sleep(3)

    current_date = str(datetime.today())[:10]
    full_content = CONTENT.format(current_date)
    pyautogui.write(full_content)
    time.sleep(3)

    print(pyautogui.position())

    # pyautogui.click(x=1207, y=657, clicks=1)

    # print(pyautogui.position())

    #time.sleep(5)

    # print(pyautogui.position())

    # --------------------------------------------------------
    # passo 3: exprovar a base de vendas
    # --------------------------------------------------------

    '''
    # 1 click no arquivo
    pyautogui.click(x=448, y=344, clicks=1)
    time.sleep(1)

    # 1 click no MENU
    pyautogui.click(x=1686, y=243)
    time.sleep(2)

    # 1 click para download do arquivo ( base de dados de vendas )
    pyautogui.click(x=1454, y=643)
    time.sleep(5)

    # click em ok para confirmar
    pyautogui.click(x=1108, y=668)
    time.sleep(10)

    # ------------------------------------------------------------
    # PASSO 4: calcular os indicadores
    #   (faturamento e quantidade de produtos vendidos)
    # ------------------------------------------------------------


    try:
        sell_content = pd.read_excel(r'/home/ijdev/Downloads/Vendas - Dez.xlsx')
    except Exception as err:
        print(f'EXCEPTION: {err}')
        sell_content = 'NO SELL CONTENT'


    # r'' -> raw string ( path string )

    print(sell_content)

    faturamento = sell_content['Valor Final'].sum()
    product_total_sell = sell_content['Quantidade'].sum()

    print(f'\n\n TOTAL DE PRODUTOS VENDIDOS:  {product_total_sell}')
    print(f'\n\n TOTAL DE FATURAMENTO: {faturamento}\n\n')

    # ----------------------------------------------------------------
    # passo 5: enviar um email pra a diretoria com os indicadores
    # ----------------------------------------------------------------

    print('\n\n ENVIANDO EMAIL...')

    pyautogui.hotkey('ctrl', 't')
    pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')

    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(15)

    pyautogui.click(x=177, y=251)
    time.sleep(5)

    pyautogui.write('welcome2ijmedia@gmail.com')
    pyautogui.press('enter')
    time.sleep(3)

    pyautogui.click(x=922, y=521)
    pyautogui.write(u'[ TESTE ] | Enviando relatorio de analise de dados')
    time.sleep(3)

    pyautogui.click(x=990, y=630)
    pyautogui.write('     Enviando email para o diretor OBAMA . ')
    time.sleep(7)

    # print(pyautogui.position())
    pyautogui.click(x=917, y=1044)

    print('\n\n EMAIL ENVIADO COM SUCESSO \n\n')
    '''


def remove_data_files():
    print('\n\n REMOVING FILES...')

    os.chdir('/home/ijdev/Downloads')

    for file_ in glob.glob('*.xlsx'):
        if 'Vendas - Dez' in file_:
            os.remove(file_)

    return
