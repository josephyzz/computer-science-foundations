"""
Conceito de Recursividade
- Função que executa a si propria.
Usada para dividir problemas complexos.
Pode ser usadas para substituir uso de loops.
"""


def factorial(n: int):
    if n in [0, 1]:
        return 1
    if n > 0:
        return n * factorial(n - 1)


print(factorial(5))  # result = 120
