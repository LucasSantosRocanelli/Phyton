def calcular_tempo_viagem(distancia, velocidade_media):
   """
   Calcula o tempo de uma viagem com base na distância e velocidade média.


   Args:
       distancia (float): Distância a percorrer em km
       velocidade_media (float): Velocidade média esperada em km/h


   Returns:
       float: Tempo da viagem em horas
   """
   if velocidade_media <= 0:
       raise ValueError("A velocidade média deve ser maior que zero")
   return distancia / velocidade_media




def converter_horas_para_horas_minutos(horas):
   """
   Converte horas decimais para horas e minutos.


   Args:
       horas (float): Tempo em horas decimais


   Returns:
       tuple: (horas_inteiras, minutos)
   """
   horas_inteiras = int(horas)
   minutos = int((horas - horas_inteiras) * 60)
   return horas_inteiras, minutos




def main():
   print("Calculadora de Tempo de Viagem")
   print("------------------------------")


   try:
       distancia = float(input("Digite a distância a percorrer (km): "))
       velocidade_media = float(input("Digite a velocidade média esperada (km/h): "))


       if distancia <= 0 or velocidade_media <= 0:
           print("Por favor, digite valores positivos para distância e velocidade.")
           return


       horas = calcular_tempo_viagem(distancia, velocidade_media)
       horas_inteiras, minutos = converter_horas_para_horas_minutos(horas)


       print(f"\nTempo estimado de viagem: {horas_inteiras} horas e {minutos} minutos")


   except ValueError:
       print("Erro: Por favor, digite valores numéricos válidos.")




if __name__ == "__main__":
   main()
