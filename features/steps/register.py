from behave import when, given, then
from modules.page_objects import Registro
from time import sleep


@given('que acesse a pagina de registro')
def acessar_pagina_registro(context):
    context.registro = Registro(context.driver)
    context.registro.navigate()

@when('efetuo o cadastro')
def efetuo_cadastro(context):
    table = dict(context.table)
    context.registro.register(table['email'], table['username'], table['first_name'], table['last_name'], table['password'])

@then('a mensagem cadastro invalido deve ser exibida')
def verifica_mensagem(context):
    assert context.text == context.registro.get_message_cadastro_invalid