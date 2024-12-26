idade = input("Digite sua idade: ")

try:
    idade = int(idade)
    
    if idade >= 18:
        print("OK. Você está permitido a tirar habilitação")
    else:
        print("Você não pode tirar habilitação sem atingir a maioridade +18")

except ValueError:
    print("Digite um número ao invés de um caracter")