from collections import deque

grafo = {}
grafo['voce'] = ['alice', 'bob', 'claire']

# Nivel 1
grafo['bob'] = ['anuj', 'peggy']
grafo['alice'] = ['peggy']
grafo['claire'] = ['thom', 'jonny']

# Nivel 2
grafo['anuj'] = []
grafo['peggy'] = []
grafo['thom'] = []
grafo['jonny'] = []


def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'


def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if pessoa not in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + ' é um vendedor de manga!')
                return True
        else:
            fila_de_pesquisa += grafo[pessoa]
            verificadas.append(pessoa)
    return False


pesquisa('voce')
