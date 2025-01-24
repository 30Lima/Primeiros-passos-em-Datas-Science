#Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos 
#consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.

import os
os.system("cls")

preco_medio_um = float(input("Digite o preço do carro no primeiro ano: "))
preco_medio_dois = float(input("Digite o preço do carro no segundo ano: "))
preco_medio_tres = float(input("Digite o preço do carro no terceiro ano: "))

if preco_medio_um > preco_medio_dois and preco_medio_tres:
    print("Em comparação aos outros, no primeiro ano o carro estava com um valor mais alto.")
elif preco_medio_dois > preco_medio_um and preco_medio_tres:
    print("Em comparação aos outros, no segundo ano o carro estava com um valor mais alto.")
else:
    print("Em comparação aos outros, no terceiro ano o carro estava com um valor mais alto.")