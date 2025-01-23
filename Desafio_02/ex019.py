#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.

frase_usuario = input("Digite uma frase: ")

frase_tratada = frase_usuario.strip().lower()

print(frase_tratada)