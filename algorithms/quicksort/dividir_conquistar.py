def divide_terreno(lado_maior, lado_menor):
    if lado_menor == 0:
        return lado_maior
    return divide_terreno(lado_menor, lado_maior % lado_menor)


print(divide_terreno(1680, 640))
