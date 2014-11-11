
def divide(valor_1,valor_2):
	if valor_2 == 0:
		return "Erro, nao divide por ZERO!"
	else:
		return float(valor_1) / float(valor_2)


def testa_tipo(variavel):
	return type(variavel)



print(testa_tipo(print))