#Crie um programa que solicite dois valores numéricos, um numerador e um denominador e 
#realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

valor_um = int(input("Digite um número (numerador): "))
valor_dois = int(input("Digite outro número (denominador): "))

if valor_dois == 0:
    print("O valor do denominador não pode ser zero!")
else:
    divisao = valor_um / valor_dois
    print("O valor da divisão inteira é: ", divisao)