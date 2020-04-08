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
        
@registro
Cenario: Efetuar login com sucesso
    Dado que acesse a pagina login
    Quando efetuo o login
        | chave | valor                |
        | email | fernando_9@teste.com |
        | senha | teste123             |
    Então o nome de usuário deve ser exibido
        """
        Hi, fernando_teste_9!
        """