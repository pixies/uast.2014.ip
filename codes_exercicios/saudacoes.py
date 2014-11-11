# --*-- encoding: utf-8 --*--

#Comentario de uma linha
def saudacao(nomePessoa,hora):
	return "{} Bom dia, São {}".format(nomePessoa,hora)

	"""
	Este codigo vai saudar uma pessoa
	Sempre que perguntado ele vai responder
	com uma saudacao de : bom dia, boa tarde 
	boa Noite
	"""



print(saudacao('joao','11horas'))