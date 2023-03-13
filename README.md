# ViaCEP-python
## Modulo simples para fazer requisições à API do ViaCEP em Python

Necessita de:
ou, CEP;
ou, Unidade Federativa(Estado), Localidade(Cidade) e Logradouro(Nome da rua, avenida, etc.).

Os formatos aceitos são "json" e "xml".

Ao não definir um formato será retornado:
ou uma lista vazia;
ou uma lista com dicionários;
ou um dicionário.

Se for definido um formato, será retornado uma string contendo o valor no formato requisitado.
