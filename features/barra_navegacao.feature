# language: pt

Funcionalidade: Barra de navegação

Contexto: Acessar página
    Dado que acesse a pagina inicial
    
    @wip
    Esquema do Cenário: "<Botão>" presente na barra de navegação e click "<Página>"
        Então o "<Botão>" deve estar disponivel na página
        Quando clicko em "<Botão>"
        Então devo ser direcionado para página login "<Botão>"

        Exemplos: Botões na NavBar
            | Botão    | Página          |
            | Login    | Página Inicial  |
            | Register | Página Registro |
            | Home     | Página Login    |