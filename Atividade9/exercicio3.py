
mais_gordo = {"nome": "", "peso": float('-inf')}
mais_magro = {"nome": "", "peso": float('inf')}

for i in range(1, 6):
    nome = input(f"Digite o nome da {i}ª pessoa: ")
    peso = float(input(f"Digite o peso da {i}ª pessoa (em kg): "))

    if peso > mais_gordo["peso"]:
        mais_gordo["nome"] = nome
        mais_gordo["peso"] = peso

    if peso < mais_magro["peso"]:
        mais_magro["nome"] = nome
        mais_magro["peso"] = peso

print("Resultados:")
print(f"Mais gordo: {mais_gordo['nome']} com {mais_gordo['peso']} kg")
print(f"Mais magro: {mais_magro['nome']} com {mais_magro['peso']} kg")