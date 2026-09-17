import random
from ordenacoes import BubbleSort, QuickSort, SelectionSort, InsertionSort


while True:

    quantidade = int(input("\nDigite a quantidade de elementos: "))

    vetor_aleatorio = [random.randint(1, 1000) for _ in range(quantidade)]
    vetor_ordenado = sorted(vetor_aleatorio)
    vetor_inverso = sorted(vetor_aleatorio, reverse=True)

    vetores = [
        ("Aleatório", vetor_aleatorio),
        ("Ordenado", vetor_ordenado),
        ("Inverso", vetor_inverso)
    ]

    for nome, vetor in vetores:

        bubble = BubbleSort(vetor)
        quick = QuickSort(vetor)
        selection = SelectionSort(vetor)
        insertion = InsertionSort(vetor)

        bubble_comparacoes, bubble_movimentacoes = bubble.ordenar()
        quick_comparacoes, quick_movimentacoes = quick.ordenar()
        selection_comparacoes, selection_movimentacoes = selection.ordenar()
        insertion_comparacoes, insertion_movimentacoes = insertion.ordenar()

        print(f"\nResultados - Vetor {nome}:")
        print(f"Quantidade de elementos: {quantidade}")
        print(f"Bubble Sort - Comparações: {bubble_comparacoes}")
        print(f"Bubble Sort - Movimentações: {bubble_movimentacoes}")
        print(f"Quick Sort - Comparações: {quick_comparacoes}")
        print(f"Quick Sort - Movimentações: {quick_movimentacoes}")
        print(f"Selection Sort - Comparações: {selection_comparacoes}")
        print(f"Selection Sort - Movimentações: {selection_movimentacoes}")
        print(f"Insertion Sort - Comparações: {insertion_comparacoes}")
        print(f"Insertion Sort - Movimentações: {insertion_movimentacoes}")

    continuar = input("\nDeseja realizar outro teste? (s/n): ").lower()

    if continuar != "s":
        print("Programa encerrado.")
        break
