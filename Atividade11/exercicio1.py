def calcular_aumento(salario_atual, percentual_aumento):
   """
   Calcula o valor do aumento e o novo salário.


   Args:
       salario_atual (float): Salário atual do funcionário
       percentual_aumento (float): Porcentagem de aumento (ex: 10 para 10%)


   Returns:
       tuple: (valor_aumento, novo_salario)
   """
   valor_aumento = salario_atual * (percentual_aumento / 100)
   novo_salario = salario_atual + valor_aumento
   return valor_aumento, novo_salario




def main():

   salario_atual = float(input("Digite o valor do salário atual: R$ "))
   percentual = float(input("Digite o percentual de aumento (%): "))


   aumento, novo_salario = calcular_aumento(salario_atual, percentual)


   print("Resultado do cálculo:")
   print(f"Valor do aumento: R$ {aumento:.2f}")
   print(f"Novo salário: R$ {novo_salario:.2f}")




if __name__ == "__main__":
   main()

