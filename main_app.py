#!src/bin/python
# encoding: utf-8


import time

from automation_my_linkedin import make_post_linkedin
from aula_1_automation import task_automation
from aula_2_data_analisys import data_analisys
from aula_3_data_science_project import web_scraping_selenium


def run_app(choice):

    time.sleep(3)

    if choice == 1:
        task_automation()           # aula 1
    elif choice == 2:
        data_analisys()             # aula 2
    elif choice == 3:
        web_scraping_selenium()     # aula 3
    else:
        make_post_linkedin()        # make post in my linkedin

    return



def menu():

    while True:
        print(""""
        -----------------------------------------
                        MENU
        -----------------------------------------
        """)

        print('''
            1 --> AUTOMACAO COM PYAUTOGUI ( envio de email eutometico)
            2 --> PROJETO DE ANALISE DADOS COM PANDAS ( resultados em graficos)
            3 --> WEBSCRAPING COM SELENIUM E ANALISE DA DADOS
            4 --> MAKE POST IN MY LINKEDIN ACCCOUNT
            0 --> QUIT APP
        ''')

        try:
            response_ = int(input('INFORME UMA OPCAO:   '))
        except Exception as err:
            print(f'AVISO: OPCAO INVALIDA')
            response_ = 'BAD'

        if response_ in (0, 1, 2, 3, 4):
            break

    return response_




if __name__ == '__main__':

    sleep_minutes = 1

    while True:
        response_ = menu()
        if response_ == 0:
            print('\n\n THE APP WILL BE QUIT\n\n')
            exit(0)

        run_app(response_)

        print('-'*80)
        print(f'\n THE APP GOING TO SLEEP {sleep_minutes} minute(s)\n')
        print('-'*80)

        time.sleep(sleep_minutes * 60)
