#10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar.
#O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

import os 
os.system("cls")

def par_impar (a,b):
    verificador1 = a % 2
    if verificador1 == 0:
        print("O primeiro número digitado é par.")
    else:
        print("O primeiro número digitado é impar.")

    verificador2 = b % 2
    if verificador2 == 2:
        print("O segundo número digitado é par.")
    else:
        print("O segundo número digitado é impar.")

def positivo_negativo (a,b):
    if a > 0:
        print("O primeiro número é positivo.")
    else:
        print("O primeiro número é negativo.")
    
    if b > 0:
        print("O segundo número é positivo.")
    else:
        print("O segundo número é negativo.")
    

def inteiro_decimal (a,b):
    if a % 1 == 0:
        print("O primeiro número é inteiro.")
    else:
        print("O primeiro número número é decimal.")

    if b % 1 == 0:
        print("O segundo número é inteiro.")
    else:
        print("O segundo número é decimal.")
    
    

numero_um = float(input("Digite o primeiro número: "))
numero_dois = float(input("Digite o segundo número: "))
print("")

opcao_usuario = int(input("MENU DE OPERAÇÕES\n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n\n Digite a operação desejada: "))

if opcao_usuario == 1:
    resultado_soma = numero_um + numero_dois
    print(f"A soma dos números é: {resultado_soma}")
    par_impar(numero_um,numero_dois)
    positivo_negativo(numero_um,numero_dois)
    inteiro_decimal(numero_um,numero_dois)

elif opcao_usuario == 2:
    resultado_subtracao = numero_um - numero_dois
    print(f"A subtração dos números é: {resultado_subtracao}")
    par_impar(numero_um,numero_dois)
    positivo_negativo(numero_um,numero_dois)
    inteiro_decimal(numero_um,numero_dois)


elif opcao_usuario == 3:
    resultado_divisao = numero_um / numero_dois
    print(f"O resultado da divisão é: {resultado_divisao}")
    par_impar(numero_um,numero_dois)
    positivo_negativo(numero_um,numero_dois)
    inteiro_decimal(numero_um,numero_dois)


elif opcao_usuario == 4:
    resultado_multiplicacao = numero_um * numero_dois
    print(f"O resultado da multiplicação é: {resultado_multiplicacao}")
    par_impar(numero_um,numero_dois)
    positivo_negativo(numero_um,numero_dois)
    inteiro_decimal(numero_um,numero_dois)

else:
    print("ERRO")

