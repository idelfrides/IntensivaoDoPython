#!src/bin/python
# encoding: utf-8


import time
from automation_my_linkedin import make_post_linkedin
from aula_1_automation import task_automation
from aula_2_data_analisys import data_analisys
from aula_3_data_science_project import web_scraping_selenium

def run_app():

    time.sleep(3)
    print(f'\n\n\n THIS IS INTENSIVAO DO PYTHON SHORT COURSE \n')
    print('-'*80)

    # task_automation()        # aula 1
    # data_analisys()          # aula 2
    web_scraping_selenium()    # aula 3

    # make_post_linkedin()

    return




if __name__ == '__main__':
    run_app()