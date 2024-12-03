#Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
import os
os.system("cls")
nome_usuario = input("Digite o seu nome:")
idade_usuario = input("Digite a sua idade:")
print("Olá, ", nome_usuario, "você tem ", idade_usuario, "anos\n")