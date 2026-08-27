from algoritmo import AlgoritmoOrdenacao


class BubbleSort(AlgoritmoOrdenacao):
    def ordenar(self):
        for i in range(len(self.vetor)):
            for j in range(len(self.vetor) - 1 - i):
                self.comparacoes += 1

                if self.vetor[j] > self.vetor[j + 1]:
                    self.vetor[j], self.vetor[j + 1] = self.vetor[j + 1], self.vetor[j]
                    self.movimentacoes += 1

        return self.comparacoes, self.movimentacoes


class QuickSort(AlgoritmoOrdenacao):
    def ordenar(self):

        def ordenar_particao(inicio, fim):
            if inicio >= fim:
                return

            pivo = self.vetor[fim]
            i = inicio - 1

            for j in range(inicio, fim):
                self.comparacoes += 1

                if self.vetor[j] <= pivo:
                    i += 1

                    if i != j:
                        self.vetor[i], self.vetor[j] = self.vetor[j], self.vetor[i]
                        self.movimentacoes += 1

            if i + 1 != fim:
                self.vetor[i + 1], self.vetor[fim] = self.vetor[fim], self.vetor[i + 1]
                self.movimentacoes += 1

            posicao_pivo = i + 1

            ordenar_particao(inicio, posicao_pivo - 1)
            ordenar_particao(posicao_pivo + 1, fim)

        ordenar_particao(0, len(self.vetor) - 1)

        return self.comparacoes, self.movimentacoes
