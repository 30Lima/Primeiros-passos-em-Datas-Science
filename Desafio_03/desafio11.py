#11) Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. 
# O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo,
# se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:

#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes.


import os
os.system("cls")

lado_um = float(input("Digite um número que represente o primeiro lado de um triânngulo: "))
lado_dois = float(input("Digite outro número que represente o segundo lado de um triângulo: "))
lado_tres = float(input("Digite mais um número que represente o terceiro lado de um triângulo: "))
print("")

verificacao = lado_um + lado_tres

if verificacao > lado_tres:
    print("Verificamos os números digitados e é possível realizar um triângulo com eles!")
else:
    print("Não é possível realizar um triângulo com os números digitados.")

print("")

if lado_um == lado_dois and lado_tres:
    print("O triângulo é Equilátero!")
elif lado_um == lado_dois or lado_dois == lado_tres or lado_um == lado_tres:
    print("O triângulo é Isósceles!")
elif lado_um != lado_dois and lado_dois != lado_tres:
    print("O triângulo é Escaleno.")
else:
    ("Erro.")


