#3) Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.

import os
os.system("cls")

letra_usuario = str(input("Digite uma letra do afabeto: "))

if letra_usuario == "A" or "E" or "I" or "o" or "u":
    print("A letra digitada é uma vogal!")
else: 
    print("A letra digitada é uma consoante!")