
"""
PROJETO CIÊNCIA DE DADOS - PREVISÃO DE VENDAS

--

DESAFIO: Nosso desafio é conseguir prever as vendas que vamos ter em determinado período com base nos gastos em anúncios nas 3 grandes redes que a empresa Hashtag investe: TV, Jornal e Rádio
-----------------------------------------------------------

ESCREVER O PASSO-A-PASSO  EM PORTUGUÊS

Passo a Passo de um Projeto de Ciência de Dados

- Passo 1: Entendimento do Desafio
- Passo 2: Entendimento da Área/Empresa
- Passo 3: Extração/Obtenção de Dados
- Passo 4: Ajuste de Dados (Tratamento/Limpeza)
- Passo 5: Análise Exploratória
    # a) visualizar como as informações de cada item são distribuídas
    # b) ver a correlação entre cada um dos itens

- Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)

    # prapare content for training  and testing our AI

    # x -> o restante (quem vc vai usar pra treinar a AI, realizar a previsão)
    # y -> quem (parâmetro/atributo/métrica) q vc quer prever

    # TRAIN_TEST_SPLIT -> é um método q separa os dados de maneira aleatória de acordo com o tamanho informado em percentual

    # modelos de AI que iremos usar:
    # --> regressao linear
    # --> RandomForest (Árvore de decisão)

    # create models
    regression_linear_model = LinearRegression()
    random_forest_model = RandomForestRegressor()

    # train models
    regression_linear_model.fit(x_train, y_train)
    random_forest_model.fit(x_train, y_train)

    # Teste da AI e avaliação do melhor modelo

    # usar o R² (indicador) -> diz o % q o nosso modelo consegue explicar o q acontece. quanto mais proximo de 100% melhor

    # visualizar os grafico das previsões
    # resposta: o melhor modelo é o de árvore de decisão

    # realizar uma nova previsao


- Passo 7: Interpretação de Resultados

-------------------------------------------------------------------------------
"""

import os
import time
import pyautogui
import pyperclip
import pandas as pd

# python package for building charts
import matplotlib.pyplot as plt    # the main one
import seaborn as sns              # lib created using matplotbib
import plotly.express as px        #

# AI importation
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics


FILES_PATH = os.path.dirname(os.path.abspath(__file__))


def data_science_AI():

    print('-'*80)
    print('\n DATA SCIENTE AND AI PROJECT [ ongoing ] ...\n')
    print('-'*80)

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
    # Passo 5: DONE
    sns.heatmap(ads_content.corr(), cmap='Wistia', annot=True)
    # plt.show()

    # passo 6:
    x = ads_content[['TV', 'Radio', 'Jornal']]
    y = ads_content['Vendas']

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=1)

    # create models
    regression_linear_model = LinearRegression()
    random_forest_model = RandomForestRegressor()

    # train models
    regression_linear_model.fit(x_train, y_train)
    random_forest_model.fit(x_train, y_train)

    # Testing AI  models
    prevision_linear_regression = regression_linear_model.predict(x_test)
    prevision_random_forest = random_forest_model.predict(x_test)

    print('#'*80)
    print('\n\n MODELO REGRESSAO LINEAR: {}'.format(
        metrics.r2_score(y_test, prevision_linear_regression)*100))

    print('\n\n MODELO ARVORE DE DECISAO: {}\n\n'.format(
        metrics.r2_score(y_test, prevision_random_forest)*100))
    print('#'*80)

    auxiliar_table = pd.DataFrame()

    auxiliar_table['y_test'] = y_test
    auxiliar_table['Previsao Regressao Linear'] = prevision_linear_regression
    auxiliar_table['Previsoa ArvoreDecisao'] = prevision_random_forest

    plt.figure(figsize=(15, 6))
    sns.lineplot(data=auxiliar_table)
    plt.show()

    # realizar uma nova previsao
    real_path = '/'.join([FILES_PATH, 'utils', 'novos.csv'])
    new_ads_content = pd.read_csv(real_path)

    print(f'\n NEW CONTENT TO PREVISION \n\n')
    print(new_ads_content)

    prevision = random_forest_model.predict(new_ads_content)

    print(f'\n RESULT NEW PREVISION \n\n {prevision} \n\n\n')

    print('DONE')

    return