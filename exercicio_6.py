#Escreva um programa que receba dois números flutuantes e realize sua adição

num1 = input("Digite um número decimal: ")
num2 = input("Digite um número decimal: ")

try:
    num1 = float(num1)
    num2 = float(num2)
    soma = num1 + num2
    print(f'A soma dos números {num1} e {num2} é {soma}')
except:
    print("Error : tipagem de dados incorreta")
    