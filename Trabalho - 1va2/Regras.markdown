Atividade para nota da 1VA.
==========================

Regras:
======

- Equipe: Até 3 pessoas.
- Avaliação:
	- Fluxograma dos sistemas
	- Apresentação do Sistema funcionando
	- Avaliação individual
	- Prova em grupo de até 3 pessoas sobre os projetos


Sistema-1
=========

1. Construir uma super calculadora, com as seguintes operações:
1.1. Nesta calculadora o usuário deverá se identificar com um '''apelido''';
1.2. Deverá executar: Soma, Subtração, Divisão (divizão por zero), Multiplicação;
1.2. O sistema deverá ser iniciado, ficando em '''loop''', deverá apresentar a seguinte tela:

```
	################## Super Calculadora ####################
	#							#
	# Está é a super calculadora, se ideintifique para usar	#
	# ----------------------------------------------------- #
	#							#	
	# Utilize as seguintes operações: 			#
	#	(So) Soma		(Su) Subtração		#
	#	(Di) Divisão		(Mu) Multiplicação	#
	#							#
	#	Para ver o resultado				#
	#							#
	# Para listar todas as pessoas que usaram a calculadora #
	# digite:						#
	# 	(L) Listar só as pessoas			#
	#	(LO) Lista pessoas e as operações		#
	#							#
	######################################################### 
```

1.2.1 O sistema deverá armazenar as indormações das operações em uma lista (array)
1.2.2. O sistema deverá armasenar as informações da seguinte forma: 

	pessoas = [
			['Fulano','2+2','4'],
			['Sicrano','3*2','6']
		  ]

1.2.3. O sistema deverá listar tanto as pessoas (L), quanto as operações com seus valores (LO).


Sistema-2
=========

2.1 Construa um sistema para avaliação de alunos de uma faculdade. O sistema deverá armazenar 
as seguintes informações:

	 Alunos = [['Nome Completo','nota 1','nota 2','nota 3','nota_final','status']]

	 Exemplo: Alunos = [
				['João da Espinola', 8,8,,'não precisa','não precisa','Aprovado por Média'],
				['Miguel Barnabe' 3,4,8,5 'Aprovado'],
				['Ronaldo Fenomeno',4,4,4,4,'Reprovado']
			   ]

2.2 O sistema deverá ter a seguinte tela:

	########################################### SIGA ###########
	#							   #
	# Para adcionar um aluno digite: (Add)		   	   #
	# Para Listar alunos escolha a seguinte categoria:	   #
	#	(L) Listar todos Alunos				   #
	#	(LAp) Lista alunos aprovados por média		   #
	#	(LAf) Lista alunos aprovados na final		   #
	#	(LRe) Lista alunos reprovados			   #
	#							   #
	############################################################


Sistema-3
=========

3.1. Costrua um sistema de reservas de Passagem aéreas com as seguintes funcionalidades:
3.2. O sistema deverá cadastrar a cidade - Cidades = ['Recife'.'Maceio','Terezina']
3.3. O sistema deverá cadastrar o viajante e sua cidade de origem - Viajantes_origem = [['Joao da Silva','Serra Talhada']]
3.4. O sistema deverá cadastrar o destino do passageiro - Destino_Rota = [[Viajantes[0][0],Viajantes[0][1], Cidades[0]]
3.5. O sistema deverá ter a seguinte tela:

'''
	######################################################## Viagens viajar #
	#									#
	#	Para adcionar um Cidades: (Cite)				#
	#	Para adcionar um viajante: (Viaj)				#
	#	Para adcionar uma Destino: (Dest)				#
	#	----------------------------------------------------------	#
	#									#
	#	Para imprimir a rota (Rota)					#
	#	Para imprimir as cidades: (LC)					#
	#	Para imprimir os Viajantes: (LV)				#
	#########################################################################
'''
