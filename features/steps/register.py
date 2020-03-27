from behave import when, given, then
from modules.page_objects import Registro
from time import sleep


@given('que acesse a pagina de registro')
def acessar_pagina_registro(context):
    context.registro = Registro(context.driver)
    context.registro.navigate()