
maior = -1
menor = float('inf')

for i in range(1, 11):
    while True:
        try:
            numero = int(input(f"Digite o {i}º número inteiro positivo: "))
            if numero > 0:
                break
            else:
                print("Por favor, digite um número inteiro positivo.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"O maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {menor}")