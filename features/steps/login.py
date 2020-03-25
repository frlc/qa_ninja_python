from behave import when, given, then
from modules.page_objects import Login
from time import sleep


@given('que acesse a pagina login')
def acessar_pagina_login(context):
    context.login = Login(context.driver)
    context.login.navigate()

@when('efetuo o login')
def efetuo_login(context):
    table = dict(context.table)
    context.login.login(table['email'], table['senha'])

@then('a mensagem deve ser exibida')
def verifica_mensagem(context):
    assert context.text == context.login.get_message_login_invalid