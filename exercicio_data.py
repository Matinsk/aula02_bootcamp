#faça um programa que peça o o usuário que solicite uma data no formata dd/mm/aaaa, em seguida, imprima o dia, o mÊs e o ano separadamente##

data_inserida = input("Digite a data em dd/mm/yyyy: ")

dia = data_inserida[0:2]
mes = data_inserida[3:5]
ano = data_inserida[6:10]

print(f'Dia {dia}, Mês {mes}, Ano {ano}')