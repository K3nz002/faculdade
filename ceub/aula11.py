def bubble_sort(lista):
    n = len(lista) # Obtém o número de elementos na lista

    # Loop externo: Controla o número de "passadas" pela lista
    # Precisamos de n-1 passadas no pior caso
    for i in range(n - 1):
        # Loop interno: Percorre a lista para comparar e trocar elementos adjacentes
        # A cada passada 'i', os últimos 'i' elementos já estão no lugar certo
        # então não precisamos mais compará-los
        for j in range(n - 1 - i):
            # Compara o elemento atual com o próximo
            if lista[j] > lista[j+1]:
                # Se o elemento atual for maior que o próximo, troque-os de posição
                # Essa é a parte crucial do "borbulhamento"
                lista[j], lista[j+1] = lista[j+1], lista[j] # Troca de valores em Python!

# Testando o Bubble Sort
lista_bubble = [64, 25, 12, 22, 11, 60, 14, 27]
print(f"\nLista para Bubble Sort: {lista_bubble}")
bubble_sort(lista_bubble)
print(f"Lista ordenada (Bubble Sort): {lista_bubble}")

lista_bubble_2 = [5, 1, 4, 2, 8]
print(f"\nOutra lista para Bubble Sort: {lista_bubble_2}")
bubble_sort(lista_bubble_2)
print(f"Lista ordenada (Bubble Sort): {lista_bubble_2}")
