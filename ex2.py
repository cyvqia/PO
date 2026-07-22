class OrdemServico:
    def __init__(self, status, dataAbertura, valorTotal):
        self.status = status
        self.dataAbetura = dataAbertura
        self.valorTotal = valorTotal

    def atualizarStatus(self):
        print(f"O status atual da OS é {self.status}.")
        print(f"A data de abertura é {self.dataAbetura}")
        print(f"O valor total é {self.valorTotal}")

info1 = OrdemServico("Em andamento", "7/7/26", 106.35)

info1.atualizarStatus()