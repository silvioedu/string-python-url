import re

endereco = (
    "Rua das Flores, 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120"
)

padrao = re.compile("\d{5}-{0,1}\d{3}")
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)
