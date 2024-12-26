#Faça um programa que converta a temperatura de Celsius para Fahrenheit.

temperatura_celsius = input("Digite a temperatura Celsius: ")

try:
    temperatura_celsius = float(temperatura_celsius)
    # Fórmula (temperatura_celsius × 9/5) + 32
    temperatura_fahrenheit = (temperatura_celsius * (9/5)) + 32
    print(f'A conversão da temperatura Celsius: {temperatura_celsius} em Fahrenheit é: {temperatura_fahrenheit}')
except:
    print("Error : tipo de tipagem incorreta")

