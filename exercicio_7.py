#Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

num1 = input("Digite um número: ")
num2 = input("Digite um número: ")

try:
    num1 = float(num1)
    num2 = float(num2)
    media = (num1 + num2) / 2
    print(f'A média dos números {num1} e {num2} é: {media}') 
except:
    print("Error : tipagem de dados incorreta")
    