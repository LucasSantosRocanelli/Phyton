
nomes = []
notas = []
cont_4_7 = 0
cont_maior_7 = 0
cont_menor_4 = 0

for i in range(10):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    nota = float(input(f"Digite a nota bimestral de {nome}: "))

    nomes.append(nome)
    notas.append(nota)

    if nota >= 4 and nota <= 7:
        cont_4_7 += 1
    elif nota > 7:
        cont_maior_7 += 1
    else:
        cont_menor_4 += 1

media = sum(notas) / len(notas)

maior_nota = max(notas)
menor_nota = min(notas)

aluno_maior = nomes[notas.index(maior_nota)]
aluno_menor = nomes[notas.index(menor_nota)]

print("--- RESULTADOS ---")
print(f"Média da turma: {media:.2f}")
print(f"Quantidade de notas entre 4 e 7: {cont_4_7}")
print(f"Quantidade de notas acima de 7: {cont_maior_7}")
print(f"Quantidade de notas menores que 4: {cont_menor_4}")
print(f"Aluno com maior nota: {aluno_maior} ({maior_nota:.2f})")
print(f"Aluno com menor nota: {aluno_menor} ({menor_nota:.2f})")