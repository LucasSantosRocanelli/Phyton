def calcular_dias_perdidos(cigarros_por_dia, anos_fumando):
   """
   Calcula quantos dias de vida um fumante perderá baseado no consumo de cigarros.


   Args:
       cigarros_por_dia (int): Quantidade de cigarros fumados por dia
       anos_fumando (int): Quantidade de anos que a pessoa fumou


   Returns:
       float: Total de dias de vida perdidos
   """
   minutos_perdidos_por_cigarro = 10
   dias_por_ano = 365


   # Cálculo do total de cigarros fumados
   total_cigarros = cigarros_por_dia * dias_por_ano * anos_fumando


   # Conversão de minutos perdidos para dias (1440 minutos = 1 dia)
   dias_perdidos = (total_cigarros * minutos_perdidos_por_cigarro) / 1440


   return dias_perdidos




def main():
   # Entrada de dados
   cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
   anos_fumando = int(input("Há quantos anos você fuma? "))


   # Cálculo
   dias_perdidos = calcular_dias_perdidos(cigarros_por_dia, anos_fumando)


   # Saída
   print(f"\nVocê já perdeu aproximadamente {dias_perdidos:.1f} dias de vida por fumar.")




if __name__ == "__main__":
   main()

