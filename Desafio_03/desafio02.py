#2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe 
#se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

import os 
os.system("cls")

porcentagem_empresa = float(input("Digite o percentual de crescimento de produção da sua empresa: "))

if porcentagem_empresa > 0:
    print("Sua porcentagem está positiva!")
else:
    print("Sua porcentagem está em descrescimento (negativa)!")