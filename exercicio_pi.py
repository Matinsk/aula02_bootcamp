import math

pi = math.pi

raio_do_circulo = input("Digite o raio: ")

try:
    raio_do_circulo = float(raio_do_circulo)
    area_do_circulo =  round(pi * raio_do_circulo ** 2,2)
    print(f'A área do círculo é: {area_do_circulo}')
except ValueError:
    print("Error: Tipagem dos dados incorreta")
else:
    print("O programa funcionou perfeitamente")