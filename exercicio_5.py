#Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

num = input("Digite um número: ")

try:
    num = float(num)
    quadrado = num * num
    print(f'O quadrado do número {num} é {quadrado}')
except:
    print("Error : tipagem de dados incorerta")