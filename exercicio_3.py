#Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

num1 = input("Digite o primeiro número: ") 
num2 = input("Digite o segundo número: ")


try:
    num1 = float(num1)
    num2 = float(num2)
    mult = num1 * num2
    print(f' a multiplicação do número {num1} por {num2} é {mult}')
except:
    print("Error: tipagem de dados incorreta")