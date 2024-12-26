#Escreva um programa que soma dois números inteiros inseridos pelo usuário.

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

try:
    num1 = float(num1)
    num2 = float(num2)
    soma = num1 + num2
    print(f'o resultado da soma é {soma}')
except:
    print("Tipagem dos dados incorreta")

