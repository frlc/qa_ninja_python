Funcionalidade: Registro

@registro
Cenario: Registrar usuário
    Dado que acesse a pagina de registro
    Quando efetuo o cadastro
        | chave            | valor                |
        | email            | fernando_3@teste.com |
        | username         | fernando_teste_3     |
        | first_name       | fernando             |
        | last_name        | teste                |
        | password         | teste123             |

@registro
Cenario: Não deve registrar usuário já cadastrado
    Dado que acesse a pagina de registro
    Quando efetuo o cadastro
        | chave            | valor                |
        | email            | fernando_3@teste.com |
        | username         | fernando_teste_3     |
        | first_name       | fernando             |
        | last_name        | teste                |
        | password         | teste123             |
    Então a mensagem cadastro invalido deve ser exibida
    """
    Email is already in use.
    """