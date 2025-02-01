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
      while True:
         try:
             voto_usuario = int(input("Digite o número do candidato: "))
             if voto_usuario in [1,2,3,4,5,6]:
                  break
             print("Por gentileza, digite um número válido.")
         except ValueError:
              print("Por gentileza, digite um número válido.")

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

if primeiro_candidato > max(segundo_candidato, terceiro_candidato, quarto_candidato):
   mensagem = "\n".join ([
         (f"""QUANTIDADE DE VOTOS POR CANDIDATO:,
          Primeiro candidato: {primeiro_candidato}
          Segundo candidato: {segundo_candidato}
          Terceiro candidato: {terceiro_candidato}
          Quarto candidato: {quarto_candidato}
          Votos nulos: {nulo}
          Votos em branco: {branco}
          O primeiro candidato venceu as eleições com {primeiro_candidato} votos!""")
   ])
   print(mensagem)

elif segundo_candidato > max(primeiro_candidato, terceiro_candidato, quarto_candidato):
   print(f"""QUANTIDADE DE VOTOS POR CANDIDATO: \n Primeiro candidato: {primeiro_candidato} 
         Segundo candidato: {segundo_candidato} \n Terceiro candidato: {terceiro_candidato} 
         Quarto candidato: {quarto_candidato} \n Votos nulos: {nulo}\n Votos em branco: {branco}\n 
         O segundo candidato venceu as eleições com {segundo_candidato} votos!""")

elif terceiro_candidato > max(primeiro_candidato, segundo_candidato, terceiro_candidato, quarto_candidato):
   print(f"""QUANTIDADE DE VOTOS POR CANDIDATO: \n Primeiro candidato: {primeiro_candidato} 
         Segundo candidato: {segundo_candidato} \n Terceiro candidato: {terceiro_candidato} 
         Quarto candidato: {quarto_candidato} \n Votos nulos: {nulo}\n Votos em branco: {branco}\n +
         O terceiro candidato venceu as eleições com {terceiro_candidato} votos!""")
   
elif quarto_candidato > max(primeiro_candidato, segundo_candidato, terceiro_candidato):
    print(f"""QUANTIDADE DE VOTOS POR CANDIDATO: \n Primeiro candidato: {primeiro_candidato} 
         Segundo candidato: {segundo_candidato} \n Terceiro candidato: {terceiro_candidato} 
         Quarto candidato: {quarto_candidato} \n Votos nulos: {nulo}\n Votos em branco: {branco}\n 
         O quarto candidato venceu as eleições com {quarto_candidato} votos!""")
    


if (primeiro_candidato == segundo_candidato == terceiro_candidato == quarto_candidato):
    print("Empate entre todos os candidatos!")
elif primeiro_candidato == segundo_candidato:
    print("Empate entre o primeiro e o segundo candidato!")
elif primeiro_candidato == terceiro_candidato:
    print("Empate entre o primeiro e o terceiro candidato!")
elif primeiro_candidato == quarto_candidato:
    print("Empate entre o primeiro e o quarto candidato!")
elif segundo_candidato == terceiro_candidato:
    print("Empate entre o segundo e o terceiro candidato!")
elif segundo_candidato == quarto_candidato:
    print("Empate entre o segundo e o quarto candidato!")
elif terceiro_candidato == quarto_candidato:
    print("Empate entre o terceiro e o quarto candidato!")

soma_votos = primeiro_candidato + segundo_candidato + terceiro_candidato + quarto_candidato + nulo + branco

if soma_votos > 0:
   porcentagem_nulos = (nulo / soma_votos) * 100
   porcentagem_brancos = (branco / soma_votos) * 100
   print("")
   print(f"Porcentagem de votos nulos: {porcentagem_nulos:.2f}%")
   print(f"Porcetame de votos em branco: {porcentagem_brancos:.2f}%")

