import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        return url.strip() if type(url) == str else ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        if not padrao_url.match(self.url):
            raise ValueError("A URL não é válida")

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        return self.url[:indice_interrogacao]

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        return self.url[indice_interrogacao + 1 :]

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)
        return (
            self.get_url_parametros()[indice_valor:]
            if indice_e_comercial == -1
            else self.get_url_parametros()[indice_valor:indice_e_comercial]
        )

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f"{self.url}\nParâmetros: {self.get_url_parametros()}\nURL base: {self.get_url_base()}"

    def __eq__(self, value):
        return self.url == value.url


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)

# print(extrator_url)
# print(f"O tamanho da URL é : {len(extrator_url)}")
# valor_quantidade = extrator_url.get_valor_parametro("quantidade")
# print(valor_quantidade)

print(extrator_url == extrator_url_2)
