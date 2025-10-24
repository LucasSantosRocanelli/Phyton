
maior_altura = 0
menor_altura = float('inf')
soma_altura_mulheres = 0
quantidade_mulheres = 0
quantidade_homens = 0

for i in range(1, 11):
    print(f"Pessoa {i}:")
    sexo = input("Digite o sexo (M - Masculino, F - Feminino): ").upper()
    while sexo not in ['M', 'F']:
        print("Sexo inválido! Digite M para Masculino ou F para Feminino.")
        sexo = input("Digite o sexo (M - Masculino, F - Feminino): ").upper()

    altura = float(input("Digite a altura (em metros): "))
    while altura <= 0:
        print("Altura inválida! Digite um valor positivo.")
        altura = float(input("Digite a altura (em metros): "))

    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura

    if sexo == 'F':
        soma_altura_mulheres += altura
        quantidade_mulheres += 1
    else:
        quantidade_homens += 1

media_altura_mulheres = soma_altura_mulheres / quantidade_mulheres if quantidade_mulheres > 0 else 0

print("Resultados:")
print(f"Maior altura do grupo: {maior_altura:.2f} metros")
print(f"Menor altura do grupo: {menor_altura:.2f} metros")
print(f"Média de altura das mulheres: {media_altura_mulheres:.2f} metros")
print(f"Número de homens: {quantidade_homens}")