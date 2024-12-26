#Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math

raio = input("Digite o raio do circulo: ")

try:
    raio = float(raio)
    raio_2 = raio * 2
    pi = math.pi
    area_circulo = raio_2 * pi
    print(f'A área do circulo é : {area_circulo}')
except:
    print("Error : tipagem de dado incorreta")
    