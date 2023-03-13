def consultar_via_cep(
    cep: int | str = None,
    uf: str = None,
    localidade: str = None,
    logradouro: str = None,
    formato: str = None
)-> list[dict] | dict | str :
    """Realiza uma consulta ao serviço ViaCep.\n
    Necessita de: ou, CEP;
    ou, Unidade Federativa(Estado), Localidade(Cidade) e Logradouro(Nome da rua, avenida, etc).\n
    Os formatos aceitos são "json", "xml" e "dict"(padrão)"""
    ...