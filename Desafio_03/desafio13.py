#13) Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar 
#a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 
# e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:

#Para variação acima de 20%: bonificação para o time de vendas.
#Para variação entre 2% e 20%: pequena bonificação para time de vendas.
#Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
#Para bonificações abaixo de -10%: corte de gastos.

import os
os.system("cls")

quantidade_2022 = float(input("Digite a quantidade de vendas em 2022: "))
quantidade_2023 = float(input("Digite a quantidade de vendas em 2023: "))
print("")

variacao_2022 = quantidade_2022 - quantidade_2023 / quantidade_2023 * 100
variacao_2023 = quantidade_2023 - quantidade_2022 / quantidade_2023 * 100

if variacao_2022 > 20:
    print(f"A variação de 2022 foi de {variacao_2022}% | Bonificação para o time de vendas.")

elif 20 <= variacao_2022 >=2  :
    print(f"A variação de 2022 foi de {variacao_2022}% | Pequena bonificação ao time de vendas.")

elif -10 <= variacao_2022 <= 2:
    print(f"A variação de 2022 foi de {variacao_2022}% | Planejamento de políticas de incentivo às vendas.")

elif variacao_2022 < -10:
    print(f"A variação de 2022 foi de {variacao_2022}% | Corte de gastos.")

else:
    print("ERRO")

if variacao_2023 > 20:
    print(f"A variação de 2023 foi de {variacao_2023}% | Bonificação para o time de vendas.")

elif 20 <= variacao_2023 >=2  :
    print(f"A variação de 2023 foi de {variacao_2023}% | Pequena bonificação ao time de vendas.")    

elif -10 <= variacao_2023 <= 2:
    print(f"A variação de 2023 foi de {variacao_2023}% | Planejamento de políticas de incentivo às vendas.")

elif variacao_2023 < -10:
    print(f"A variação de 2023 foi de {variacao_2023}% | Corte de gastos.")

else:
    print("ERRO")

