#7) Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo.
#  Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número 
# inteiro e determine se ele é ou não um número primo.

import os
os.system("cls")

numero_usuario = int(input("Digite um número: "))

if numero_usuario <=1 :
    print("O número não é primo.")


else: 
    primo = True

    for i in range (2, numero_usuario):
        if numero_usuario % i == 0:
           primo = False
           break

    if primo:
     print("O número digitado é primo.")
    else:
        print("O número digitado não é primo.")
