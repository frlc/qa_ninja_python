from behave import given, then, when 
from modules.page_objects import Home
from modules.page_objects import NavBar
from time import sleep

@given('que acesse a pagina inicial')
def acessar_pagina_inicial(context):
    context.navbar = NavBar(context.driver)

@then('o "{titulo}" deve ser visualizado')
def valida_titulo(context, titulo):
    value_temp = context.navbar.marca
    assert titulo == context.NavBa.marca

@then('o registro deve estar disponivel')
def valida_titulo(context):
    assert context.text == context.navbar.slogan

@then('o "{elemento}" deve estar disponivel na página')
def check_elemento(context, elemento):
    dic = {
        
        'Login': context.navbar.text_login,
        'Register': context.navbar.text_register,
        'Home': context.navbar.text_home
    }
    #hasattr(context.navbar, '_login')
    assert dic[elemento] == elemento

@when('clicko em "{elemento}"')
def element_click(context, elemento):
    dic = {
        'Login': context.navbar.click_login,
        'Register': context.navbar.click_register,
        'Home': context.navbar.click_home
    }
    dic[elemento]()


@then('devo ser direcionado para página login "{page}"')
def verifica_url_login(context, page):
    dic = {
        'Login': 'http://projectdreamteam.pythonanywhere.com/login',
        'Register': 'http://projectdreamteam.pythonanywhere.com/register',
        'Home': 'http://projectdreamteam.pythonanywhere.com/'
        }
    assert dic[page] == context.navbar.get_url
