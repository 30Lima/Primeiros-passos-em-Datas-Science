#8) Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. 
# Dica: Você pode utilizar o operador módulo %.

import os
os.system("cls")

numero = int(input("Digite um número: "))

numero_att = numero%2

if numero_att == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")