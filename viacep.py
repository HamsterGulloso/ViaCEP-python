from urllib.request import urlopen
from json import loads

def consultar_via_cep(
    cep = None,
    uf = None,
    localidade = None,
    logradouro = None,
    formato = None
):   
    if not formato or formato == 'dict':
        formato = 'dict'
        urlformat = "json"
    elif formato not in ["json", "xml", "dict"]:
        raise ValueError("\n\nFormatos Aceitos: 'json', 'xml' e 'dict'")
    else:
        urlformat = formato

    if cep:
        url =  f"https://viacep.com.br/ws/{cep}/{urlformat}/"
    elif uf and localidade and logradouro:
        url = f"https://viacep.com.br/ws/{uf}/{localidade}/{logradouro}/{urlformat}/"
    else:
        raise ValueError("\n\nInforme ou:\nCEP;\nUnidade Federativa, localidade e logradouro")

    url = url.replace(" ", "%20")

    text = urlopen(url).read().decode("utf-8")
    return text if formato != 'dict' else loads(text)