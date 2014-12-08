Atividade para nota da 1VA.
==========================

Regras:
======

- Equipe: Até 3 pessoas.
- Avaliação:
-- Apresentação do Sistema funcionando
-- 


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

