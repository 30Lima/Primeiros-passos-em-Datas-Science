#6) Escreva um programa que leia três números e os exiba em ordem decrescente.

import os
os.system("cls")

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite mais um número: "))

if n1 > n2 and n2 > n3:
    print(f"Números em ordem decrescente: {n1,n2,n3}")
elif n1 > n2 and n3 > n2:
    print(f"Números em ordem decrescente: {n1,n3,n2}")
elif n2 > n1 and n1 > n3:
    print(f"Números em ordem decrescente: {n2,n1,n3}")
elif n2> n1 and n3 > n1:
    print(f"Números em ordem descrescente: {n2,n3,n1}")
elif n3> n1 and n1 > n2:
    print(f"Números em ordem decrescente: {n3,n1,n2}")
elif n3> n2 and n2 > n1:
    print(f"Números em ordem decrescente: {n3,n2,n1}")
else:
    print("Erro")