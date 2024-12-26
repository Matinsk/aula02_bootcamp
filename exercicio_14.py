#Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = input("Digite uma data em dd/mm/yyyy: ")

lista_data = data.split("/")

dia = lista_data[0]
mes = lista_data[1]
ano = lista_data[2]

print(f'Dia: {dia}, Mês {mes}, Ano {ano}')
