"""
Exemplos de URL válidos:
    http://www.bytebank.com.br/cambio
    https://www.bytebank.com.br/cambio
    https://www.bytebank.com/cambio

Exemplos de URL inválidos:
    https://bytebank/cambio
    http://bytebank.naoexiste/cambio
    ht:bytebank.naoexiste/cambio
"""

import re

url = "http://www.bytebank.com.br/cambio"
padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
if not padrao_url.match(url):
    raise ValueError("A URL não é válida")
print("A URL é válida")
