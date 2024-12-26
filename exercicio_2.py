#Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

num = input("Digite um número: ")

try:
    num = float(num)
    resto_5 = num // 5
    print(f'o resto da divisão do número {num} dividido por 5 é {resto_5}')
except:
    print("Error : Tipagem dos dados incorreta")
