#--*-- encoding: utf-8 --*--

print("Por favor diga seu nome? ")
nome = raw_input(": ")
print("Olá " + nome + " tudo bem?")

print("Vamos usar uma calculadora aqui....")
print("A única operação válida e divisão")

def divisao(v1,v2):
    return v1/v2

v1 = input("Digite o valor que quer dividir: ")
v2 = input("Digite o valor que dividirá: ")

print divisao(v1,v2)
