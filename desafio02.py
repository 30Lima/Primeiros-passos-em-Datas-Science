'''
Coleta e amostragem de dados
Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.
Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem
 [idade] anos e mede [altura] metros!”.
'''
import os
os.system("cls")
nome_usuario = input("Digite o seu nome:")
print("Olá, ", nome_usuario, "\n")

nome_usuario = input("Digite o seu nome:")
idade_usuario = input("Digite a sua idade:")
print("Olá, ", nome_usuario, "você tem ", idade_usuario, "anos\n")
nome_usuario = input("Digite o seu nome:")
idade_usuario = input("Digite a sua idade:")
altura_usuario = input("Digite a sua altura")
print("Olá, ", nome_usuario, "você tem ", idade_usuario, "anos e mede ", altura_usuario, 
      "metros\n")

os.system("cls")
