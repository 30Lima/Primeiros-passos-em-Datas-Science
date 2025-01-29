#9) Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). 
# Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:

#Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
#Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
#Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. 
# Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em 
# branco em relação ao total de votos.


import os
os.system("cls")

primeiro_candidato = 0 
segundo_candidato = 0 
terceiro_candidato = 0 
quarto_candidato = 0 
nulo = 0
branco = 0 

for i in range(1,21):
    voto_usuario = int(input("Digite o número do candidato: "))
    while voto_usuario >= 7 and voto_usuario <= 0:
          print("Por favor, digite um número válido.")

    if voto_usuario == 1:
       primeiro_candidato += 1
    elif voto_usuario == 2:
       segundo_candidato += 1
    elif voto_usuario == 3:
       terceiro_candidato += 1
    elif voto_usuario == 4:
        quarto_candidato += 1
    elif voto_usuario == 5:
       nulo += 1
    elif voto_usuario == 6:
       branco += 1
    break

print(f"{primeiro_candidato}")
    

