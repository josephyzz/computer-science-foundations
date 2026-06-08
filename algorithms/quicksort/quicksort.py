def quicksort(array):
    # Case-base
    if len(array) < 2:
        return array

    # O pivo será nosso divisor de particionamento
    # os maiores ficam no lado direto e os menores no lado esquerdo
    pivo = array[0]
    menores = [i for i in array[1:] if i <= pivo]
    maiores = [i for i in array[1:] if i > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)


print(quicksort([33, 7, 10, 6, 77, 25, 15]))
