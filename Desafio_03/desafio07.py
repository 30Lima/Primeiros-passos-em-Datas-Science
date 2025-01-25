#7) Escreva um programa que pergunte em qual turno a pessoa usuária estuda 
# ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.

import os 
os.system("cls")

turno = (input("Em qual turno você estuda? \n Manhã \n Tarde \n Noite \nDigite aqui: " ))
turno_usuario = turno.capitalize()

print(turno_usuario)

if turno_usuario == "Manhã":
    print("Bom dia!")
elif turno_usuario == "Tarde":
    print("Boa tarde")
elif turno_usuario == "Noite":
    print("Boa noite")
else:
    print("Erro.")