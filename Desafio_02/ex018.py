#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.

frase_usuario = input("Digite uma frase: ")

frase_sem_espaco = str.strip(frase_usuario)

print(frase_sem_espaco)