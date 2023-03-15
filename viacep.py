from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from json import loads

class BadRequest(Exception):
    pass

class NoConnection(Exception):
    pass

def consultar_via_cep(
    cep = None,
    uf = None,
    localidade = None,
    logradouro = None,
    formato = None
):   
    if not formato:
        formato = 'dict'
        urlformat = "json"
    elif formato not in ["json", "xml"]:
        raise ValueError("\n\nFormatos Aceitos: 'json' e 'xml'")
    else:
        urlformat = formato

    if cep:
        url =  f"https://viacep.com.br/ws/{cep}/{urlformat}/"
    elif uf and localidade and logradouro:
        url = f"https://viacep.com.br/ws/{uf}/{localidade}/{logradouro}/{urlformat}/"
    else:
        raise ValueError("\n\nInforme ou:\nCEP;\nUnidade Federativa, localidade e logradouro")

    url = url.replace(" ", "%20")
    try:
        text = urlopen(url).read().decode("utf-8")
        return text if formato != 'dict' else loads(text)
    except HTTPError:
        raise BadRequest
    except URLError:
        raise NoConnection
