#9) Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.

import os
os.system("cls")

numero_usuario = float(input("Digite um número: "))

if numero_usuario % 1 == 0:
    print("O número é inteiro")
else:
    print("O número é decimal.")
