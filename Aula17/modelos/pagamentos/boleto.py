from datetime import date
class Boleto(Pagamento):
    def __init__(self, valor, dias_para_vencimento = 0):
        self._valor = valor
        self._vencimento = date.today() + dias_para_vencimento
    def realizar_pagamento(self):
        return True
    