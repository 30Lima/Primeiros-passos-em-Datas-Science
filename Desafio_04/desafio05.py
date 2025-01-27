#5) Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária.
#  Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. 
# Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.

import os 
os.system("cls")

numero = int(input("Digite um número: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial}.")
