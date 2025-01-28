#6) Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. 
# Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:


import os
os.system("cls")

while True:
    try: 
        numero_usuario = int(input("Digite um número inteiro: "))

    except ValueError:
        print("Por favor, digite um número inteiro.")

    break


for i in range(1,11):
    resultado = numero_usuario * i
    print(f"{numero_usuario} x {i} = {resultado}")
