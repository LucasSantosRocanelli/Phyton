
contador_21 = 0

for i in range(5):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    if idade == 21:
        contador_21 += 1

print(f"Total de pessoas com 21 anos: {contador_21}")