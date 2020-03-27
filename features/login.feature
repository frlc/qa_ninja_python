Funcionalidade: Login


Cenario: Efetuar login sem sucesso
    Dado que acesse a pagina login
    Quando efetuo o login
        | chave | valor              |
        | email | fernando@teste.com |
        | senha | teste              |
    Então a mensagem deve ser exibida
        """
        Invalid email or password.
        """