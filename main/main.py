import random
from ordenacoes import BubbleSort, QuickSort


while True:

    quantidade = int(input("\nDigite a quantidade de elementos: "))

    vetor = [random.randint(1, 1000) for _ in range(quantidade)]

    bubble = BubbleSort(vetor)
    quick = QuickSort(vetor)

    bubble_comparacoes, bubble_movimentacoes = bubble.ordenar()
    quick_comparacoes, quick_movimentacoes = quick.ordenar()

    print("\nResultados:")
    print(f"Quantidade de elementos: {quantidade}")
    print(f"Bubble Sort - Comparações: {bubble_comparacoes}")
    print(f"Bubble Sort - Movimentações: {bubble_movimentacoes}")
    print(f"Quick Sort - Comparações: {quick_comparacoes}")
    print(f"Quick Sort - Movimentações: {quick_movimentacoes}")

    continuar = input("\nDeseja realizar outro teste? (s/n): ").lower()

    if continuar != "s":
        print("Programa encerrado.")
        break
