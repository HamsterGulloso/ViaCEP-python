class BadRequest(Exception):
    """
    Esta exceção é levantada quando os parametros da consulta não adequam ao formato da requisição.
    """
    ...

class NoConnection(Exception):
    """
    Essa exceção é levantada quando não há uma conexão estável com a internet. 
    """
    pass

def consultar_via_cep(
    cep: int | str = None,
    uf: str = None,
    localidade: str = None,
    logradouro: str = None,
    formato: str = None
)-> list[dict] | dict | str :
    """
    Realiza uma consulta ao serviço ViaCep.\n
    Necessita de: ou, CEP;
    ou, Unidade Federativa(Estado), Localidade(Cidade) e Logradouro(Nome da rua, avenida, etc).\n
    Os formatos aceitos são "json" e "xml". Ao não definir um formato será retornado:
    ou uma lista vazia;
    ou uma lista com dicionários;
    ou um dicionário.
    """
    ...
