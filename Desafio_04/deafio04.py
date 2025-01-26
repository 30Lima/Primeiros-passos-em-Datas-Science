#4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. 
# A leitura deve ser encerrada ao ser enviado o valor -273°C.

import os
os.system("cls")
temperatura1 = 0
contador = 0

while True:
    try: 
        temperatura2 = float(input("Digite a temperatura: "))
        if temperatura2 != -273:
            temperatura1 += temperatura2
            contador += 1
        
        elif temperatura2 == -273:
            if contador > 0 :
                exibicao = temperatura1 / contador
                print(f"A média das temperaturas é: {exibicao:.2f}")
                break

        else:
            print("Como primeiro valor, digite uma temperatura diferente de -273ºC")
       
    except ValueError:
        print("Entrada inválida! Insira um número válido.")


