numero = input("Digite qualquer coisa: ")

try:
    numero = float(numero)
    if isinstance(numero, float or int):
        print("A variável digita é um número")
except:
     print("A variável digita é um caracter")

