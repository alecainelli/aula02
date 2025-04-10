# 1
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# print(num1+num2)

# 2
#num1 = int(input("Digite um número: "))
#calc = num1 % 5
#print("O resto da divisão por 5 é: ", calc)

#3
#num1 = int(input("Digite o primeiro número: "))
#num2 = int(input("Digite o segundo número: "))
#resultado_multiplicacao = num1 * num2
#print("O resultado da multiplicação é:", resultado_multiplicacao)

#4
# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o segundo número inteiro: "))
#num1 = 20  # Exemplo de entrada
#num2 = 3  # Exemplo de entrada
#resultado_divisao_inteira = num1 // num2
#print("O resultado da divisão inteira é:", resultado_divisao_inteira)

#5
# num = int(input("Digite um número: "))
#num = 6  # Exemplo de entrada
#resultado_quadrado = num ** 2
#print("O quadrado do número é:", resultado_quadrado)

#6
#num1 = float(input("Digite o primeiro número flutuante: "))
#num2 = float(input("Digite o segundo número flutuante: "))
#print("A soma é: ", num1 + num2)

#7
# num1 = float(input("Digite o primeiro número flutuante: "))
# num2 = float(input("Digite o segundo número flutuante: "))
#num1 = 3.5  # Exemplo de entrada
#num2 = 7.5  # Exemplo de entrada
#media = (num1 + num2) / 2
#print("A média é:", media)

#8
#base = float(input("Digite a base: "))
#expoente = float(input("Digite o expoente: "))
#base = 2.0  # Exemplo de entrada
#expoente = 3.0  # Exemplo de entrada
#potencia = base ** expoente
#print("O resultado da potência é:", potencia)

#9
#celsius = float(input("Digite a temperatura em Celsius: "))
#celsius = 30.0  # Exemplo de entrada
#fahrenheit = (celsius * 9/5) + 32
#print(f"{celsius}°C é igual a {fahrenheit}°F")

#10
#raio = float(input("Digite o raio: "))
#area = 3.14159  * (raio ** 2)
#print("A área do c´írculo é: ", area)

import math

def calcular_area_circulo(raio):
  """Calcula a área de um círculo dado o seu raio."""
  if raio < 0:
    return "O raio não pode ser negativo."
  area = math.pi * (raio ** 2)
  return area

# Exemplo de uso:
raio_circulo = float(input("Digite o raio do círculo: "))
area_calculada = calcular_area_circulo(raio_circulo)

if isinstance(area_calculada, str):
  print(area_calculada)
else:
  print(f"A área do círculo com raio {raio_circulo} é: {area_calculada:.2f}")