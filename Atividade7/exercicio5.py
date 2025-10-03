
soma_pares = 0
quantidade_pares = 0

for i in range(4):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))

    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1

if quantidade_pares > 0:
    media = soma_pares / quantidade_pares
    print(f"A média dos números pares digitados é: {media:.2f}")
else:
    print("Nenhum número par foi digitado.")