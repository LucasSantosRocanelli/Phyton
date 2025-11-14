def celsius_para_fahrenheit(celsius):
   """Converte temperatura de Celsius para Fahrenheit."""
   fahrenheit = (9 * celsius) / 5 + 32
   return fahrenheit


temperatura_celsius = float(input("Digite a temperatura em graus Celsius (°C): "))


temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C equivalem a {temperatura_fahrenheit:.1f}°F")
