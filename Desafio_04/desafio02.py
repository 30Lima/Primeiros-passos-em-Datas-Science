#2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria 
# A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. 
# Considere que a colônia A inicia com 4 elementos e a B com 10.

import os 
os.system("cls")

colonia_a = 4
colonia_b = 10
crescimento_a = 0.03
crescicmento_b = 0.015
dias = 0

while colonia_a <= colonia_b:
    colonia_a *= 1 + crescimento_a
    colonia_b *= 1 + crescicmento_b

    dias += 1

print(f'Irá levar {dias} dias para a colônia A ultrapassar a colônia B.')


