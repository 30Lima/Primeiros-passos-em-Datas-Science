#Crie um programa que solicite dois valores numéricos, um numerador 
#e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

valor_um = float(input("Digite um valor (numerador): "))
valor_dois = float(input("Digite outro valor numérico (denominador): "))

if valor_dois == 0:
    print("Por favor, digite um número que não seja 0.")

else:
    divisao = valor_um / valor_dois
    print("A divisão desses números é: ", divisao)