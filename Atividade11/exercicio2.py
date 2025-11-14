def calcular_desconto(preco, percentual_desconto):
   """
   Calcula o valor do desconto e o preço a pagar.


   Args:
       preco (float): Preço original da mercadoria.
       percentual_desconto (float): Percentual de desconto.


   Returns:
       tuple: Valor do desconto e preço a pagar.
   """
   valor_desconto = preco * (percentual_desconto / 100)
   preco_a_pagar = preco - valor_desconto
   return valor_desconto, preco_a_pagar




def main():

   preco = float(input("Digite o preço da mercadoria: R$ "))
   percentual_desconto = float(input("Digite o percentual de desconto (%): "))


   desconto, preco_final = calcular_desconto(preco, percentual_desconto)


   print(f"Valor do desconto: R$ {desconto:.2f}")
   print(f"Preço a pagar: R$ {preco_final:.2f}")




if __name__ == "__main__":
   main()
