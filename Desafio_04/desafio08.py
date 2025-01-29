#8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência.
#  Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a
#  distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.

import os
os.system("cls")

intervalo_um = 0
intervalo_dois = 0
intervalo_tres = 0
intervalo_quatro = 0

while True:
            idade_usuario = int(input("Digite a sua idade: "))

            if idade_usuario < 0:
                break

            if 0 <= idade_usuario <= 25:
                intervalo_um += 1
            elif  26 <= idade_usuario <= 50:
                intervalo_dois += 1
            elif 51 <= idade_usuario <= 75:
                intervalo_tres += 1
            elif 76 <= idade_usuario <= 100:
                intervalo_quatro += 1

            
print("\nDISTRIBUIÇÃO DE IDADES | CLASSIFICAÇÃO")
print(f"[0-25] = {intervalo_um} ")
print(f"[26-50] = {intervalo_dois} ")
print(f"[51-75] = {intervalo_tres} ")
print(f"[76-100] = {intervalo_quatro} ")