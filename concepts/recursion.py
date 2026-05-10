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


def fibornacci(rabbits: int):
    rabbits = 1
    next = 0
    for i in range(n):
        print(next)
        next, rabbits = rabbits + next, next


print(factorial(5))  # result = 120


def fibornacci(n: int):
    if n <= 1:
        return n
    return fibornacci(n - 1) + fibornacci(n - 2)


# result [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print([fibornacci(i) for i in range(10)])
