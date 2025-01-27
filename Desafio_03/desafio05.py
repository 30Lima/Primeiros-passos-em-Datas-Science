#5) Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.

import os
os.system("cls")

produto_um = float(input("Digite o preço do primeiro produto: "))
produto_dois = float(input("Digite o preço do segundo produto: "))
produto_tres = float(input("Digite o preço do terceiro produto: "))

if produto_um > produto_dois or produto_tres:
    print("O produto um é mais barato para comprar!")
elif produto_dois > produto_um or produto_tres:
    print("O produto dois é mais barato para comprar!")
else:
    print("O produto três é mais barato para comprar!")