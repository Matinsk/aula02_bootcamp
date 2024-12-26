#Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

base = input("Digite a base: ")
exponte = input("Digite o exponete: ")

try:
    base = float(base)
    exponte = float(exponte)
    potencia = base ** exponte
    print(f'A potencia de {base} pelo expoente {exponte} é : {potencia}')
except:
    print("Error : tipagem de dados incorreta")
