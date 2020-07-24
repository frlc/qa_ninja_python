from selenium import webdriver
from ipdb import spost_mortem
from allure_behave.hooks import allure_report

def before_all(context):
    context.driver = webdriver.Chrome("xxxx")

def before_feature(context, feature):
    #print(feature.name)
    ...

def before_scenario(context, scenario):
    #print(scenario.name)
    ...

def before_step(context, step):
    #print(step.name)
    ...

def before_tag(context, tag):
    if tag == 'registro':
        context.execute_steps('''
            Dado que acesse a pagina de registro
            Quando efetuo o cadastro
                | chave            | valor                |
                | email            | fernando_9@teste.com |
                | username         | fernando_teste_9     |
                | first_name       | fernando             |
                | last_name        | teste                |
                | password         | teste123             |
        ''')

def after_all(context):
    context.driver.quit()

def after_feature(context, feature):
    #print(feature.name)
    ...

def after_scenario(context, scenario):
    #print(scenario.name)
    ...

def after_step(context, step):
    #print(step.status)
    # if step.status == 'failed' and context.config.userdata['debug']:
    #     spost_mortem(step.exc_traceback)
    ...

def after_tag(context, tag):
    #print(tag)
    ...

