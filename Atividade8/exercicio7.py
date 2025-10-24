
numero_inicial = int(input("Digite o número inicial: "))

if numero_inicial >= 50:
    print("O número inicial deve ser menor que 50.")
else:
    print(f"Números pares de {numero_inicial} até 50:")

    for numero in range(numero_inicial, 51):
        if numero % 2 == 0:
            print(numero, end=' ')