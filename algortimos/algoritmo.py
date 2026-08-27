class AlgoritmoOrdenacao:
    def __init__(self, vetor):
        self.vetor = vetor.copy()
        self.comparacoes = 0
        self.movimentacoes = 0
