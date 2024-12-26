#Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

num1 = input("Digite o primeiro número inteiro: ")
num2 = input("Digite o segundo número inteiro: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    if num1 == 0 or num2 == 0:
        divisao = 0
    else:    
        divisao = num1 / num2
    print(f'A divisão do número {num1} pelo número {num2} é: {divisao}')
except:
    print("Error: tipagem de dados incorreta")