#Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.

import os 
os.system("cls")

numero_um = int(input("Digite um número: "))
numero_dois = int(input("Digite outro número: "))
print("")

if numero_um > numero_dois:
    print("O número um é maior!")
else:
    print("O número dois é maior!")