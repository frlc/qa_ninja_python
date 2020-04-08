Funcionalidade: Registro


Cenario: Não deve registrar usuário já cadastrado
    Dado que acesse a pagina de registro
    Quando efetuo o cadastro
        | chave            | valor                |
        | email            | fernando_4@teste.com |
        | username         | fernando_teste_4     |
        | first_name       | fernando             |
        | last_name        | teste                |
        | password         | teste123             |
    Então a mensagem cadastro invalido deve ser exibida
    """
    Email is already in use.
    """