#10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar.
#O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

import os 
os.system("cls")

def par_impar (a):
    verificador1 = a % 2
    if verificador1 == 0:
        print("O resultado é par.")
    else:
        print("O resultado é impar.")

def positivo_negativo (a,):
    if a > 0:
        print("O resultado é positivo.")
    else:
        print("O resultado é negativo.")
    

def inteiro_decimal (a):
    if a % 1 == 0:
        print("O resultado é inteiro.")
    else:
        print("O presultado é decimal.")
    
numero_um = float(input("Digite o primeiro número: "))
numero_dois = float(input("Digite o segundo número: "))
print("")

opcao_usuario = int(input("MENU DE OPERAÇÕES\n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n\n Digite a operação desejada: "))

if opcao_usuario == 1:
    resultado_soma = numero_um + numero_dois
    print(f"A soma dos números é: {resultado_soma}")
    par_impar(resultado_soma)
    positivo_negativo(resultado_soma)
    inteiro_decimal(resultado_soma)

elif opcao_usuario == 2:
    resultado_subtracao = numero_um - numero_dois
    print(f"A subtração dos números é: {resultado_subtracao}")
    par_impar(resultado_subtracao)
    positivo_negativo(resultado_subtracao)
    inteiro_decimal(resultado_subtracao)


elif opcao_usuario == 3:
    resultado_divisao = numero_um / numero_dois
    print(f"O resultado da divisão é: {resultado_divisao}")
    par_impar(resultado_divisao)
    positivo_negativo(resultado_divisao)
    inteiro_decimal(resultado_divisao)


elif opcao_usuario == 4:
    resultado_multiplicacao = numero_um * numero_dois
    print(f"O resultado da multiplicação é: {resultado_multiplicacao}")
    par_impar(resultado_multiplicacao)
    positivo_negativo(resultado_multiplicacao)
    inteiro_decimal(resultado_multiplicacao)

else:
    print("ERRO")

