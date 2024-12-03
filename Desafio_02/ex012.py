#Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 
#com pesos respectivamente iguais a 1, 2, 3 e 4.

numero_um = 5*1
numero_dois = 12*2
numero_tres = 20*3
numero_quatro = 15*4

soma = numero_um + numero_dois + numero_tres + numero_quatro
soma_pesos = 1 + 2 + 3 + 4

soma_total = soma / soma_pesos

print("A média ponderada é: ", soma_total)