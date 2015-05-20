

"""
Construa um contador de caracteres, que informe
quantas letras 'i' tem na string 
'asasasasasiiiasasasiiasasi'
"""
def conta_caracter(string):
	cont = 0
	for caracter in string:
		if caracter == 'i':
			cont += 1
	return cont


"""
Construa um programa que criptografe qualquer palavra,
 a regra de criptografia é, substitua as vogaes por 
 números: [a,e,i,o,u] por [1,2,3,4,5] se forem em 
 MAIUSCULO substitua por [@,#,$,%,*].
"""
def cript_palavra(palavra):
	npalavra = palavra
	for caracter in palavra:
		if caracter == 'a':
			palavra = palavra.replace(caracter, '1')
		elif caracter == 'e':
			palavra = palavra.replace(caracter, '2')
		elif caracter == 'i':
			palavra = palavra.replace(caracter, '3')
		elif caracter == 'o':
			palavra = palavra.replace(caracter, '4')
		elif caracter == 'u':
			palavra = palavra.replace(caracter, '5')
		elif caracter == 'A':
			palavra = palavra.replace(caracter, '@')
		elif caracter == 'E':
			palavra = palavra.replace(caracter, '#')
		elif caracter == 'I':
			palavra = palavra.replace(caracter, '$')
		elif caracter == 'O':
			palavra = palavra.replace(caracter, '%')
		elif caracter == 'U':
			palavra = palavra.replace(caracter, '*')
	return palavra


"""
Faça uma função que concatene números, onde toda 
sequencia numerica digitada (0,0,1,2,3,4,5) seja 
impresso no formato 0012345.
"""
def concatena_valores(n1,n2,n3,n4,n5,n6,n7):
	return str(n1) + str(n2) + str(n3) + str(n4) + str(n5) + str(n6) + str(n7)

"""
Para infinitos valores
"""
def concatene_varios_valores(*lista_de_valores):
	string = ''
	for caracter in lista_de_valores:
		string += str(caracter)
	return string


"""
Executando as funções
"""
print(concatena_valores(3,6,8,0,0,0,0))
print(concatene_varios_valores(0,0,0,0,2,0,0,1,0,1,1))
print(cript_palavra('CAMALEAO'))
print(conta_caracter('asasasasasiiiasasasiiasasi'))










