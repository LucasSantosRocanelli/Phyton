def calcular_preco_aluguel(dias, km):
   """
   Calcula o preço a pagar pelo aluguel do carro.


   Args:
       dias (int): Quantidade de dias que o carro foi alugado.
       km (float): Quantidade de quilômetros percorridos.


   Returns:
       float: Preço total a pagar.
   """
   preco_por_dia = 60.0
   preco_por_km = 0.15


   total_dias = dias * preco_por_dia
   total_km = km * preco_por_km


   return total_dias + total_km




def main():
   # Solicita os dados do usuário
   dias_aluguel = int(input("Digite a quantidade de dias que o carro foi alugado: "))
   km_percorridos = float(input("Digite a quantidade de quilômetros percorridos: "))


   # Calcula o preço a pagar
   total_a_pagar = calcular_preco_aluguel(dias_aluguel, km_percorridos)


   # Exibe o resultado
   print(f"O preço total a pagar pelo aluguel do carro é: R$ {total_a_pagar:.2f}")




if __name__ == "__main__":
   main()
