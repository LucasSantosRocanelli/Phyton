
preco_combustivel = float(input("Digite o preço do combustível por litro (R$): "))
odometro_inicio = float(input("Digite a marcação do odômetro no início do dia (Km): "))
odometro_final = float(input("Digite a marcação do odômetro no final do dia (Km): "))
litros_gastos = float(input("Digite o número de litros de combustível gasto: "))
valor_total_passageiros = float(input("Digite o valor total recebido dos passageiros (R$): "))


quilometragem_total = odometro_final - odometro_inicio
media_consumo = quilometragem_total / litros_gastos
gasto_combustivel = litros_gastos * preco_combustivel
lucro_liquido = valor_total_passageiros - gasto_combustivel


print(f"Relatório do dia:")
print(f"Quilometragem percorrida: {quilometragem_total:.2f} Km")
print(f"Média de consumo: {media_consumo:.2f} Km/L")
print(f"Gasto com combustível: R$ {gasto_combustivel:.2f}")
print(f"Lucro líquido do dia: R$ {lucro_liquido:.2f}")