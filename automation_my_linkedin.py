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
