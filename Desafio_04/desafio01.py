#1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

n1 = int(input("Digite um número inteiro :"))
n2 = int(input("Digite outro número inteiro :"))

for num in range(n1 + 1, n2):
    print(num)