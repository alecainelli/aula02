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

# exercicio 10 de outra forma
import math

def calcular_area_circulo(raio):
  """Calcula a área de um círculo dado o seu raio."""
  if raio < 0:
    return "O raio não pode ser negativo."
  area = math.pi * (raio ** 2)
  return area

# Exemplo de uso:
#raio_circulo = float(input("Digite o raio do círculo: "))
#area_calculada = calcular_area_circulo(raio_circulo)

#if isinstance(area_calculada, str):
#  print(area_calculada)
#else:
#  print(f"A área do círculo com raio {raio_circulo} é: {area_calculada:.2f}")


#11
# texto = input("Digite um texto: ")
#texto = "Olá, mundo!"  # Exemplo de entrada
#texto_maiusculas = texto.upper()
#print("Texto em maiúsculas:", texto_maiusculas)

#12
#texto = input("Digite um texto: ")
#texto = texto_minusculas = texto.lower()
#print(texto_minusculas)

#13
# frase = input("Digite uma frase: ")
#frase = "  Olá, mundo!  "  # Exemplo de entrada
#frase_sem_espacos = frase.strip()
#print("Frase sem espaços no início e no final:", frase_sem_espacos)

#14
# data = input("Digite uma data no formato dd/mm/aaaa: ")
#data = "01/01/2024"  # Exemplo de entrada
#dia, mes, ano = data.split("/")
#print("Dia:", dia)
#print("Mês:", mes)
#print("Ano:", ano)

#15
#parte1 = "Olá,"  # Exemplo de entrada
#parte2 = " mundo!"  # Exemplo de entrada
#texto_concatenado = parte1 + parte2
#print("Texto concatenado:", texto_concatenado)

#16
# Exemplo de entrada
#valor1 = True
#valor2 = False
#resultado_and = valor1 and valor2
#print("Resultado do AND lógico:", resultado_and)

#17
# Exemplo de entrada
#valor1 = True
#valor2 = False
#resultado_or = valor1 or valor2
#print("Resultado do OR lógico:", resultado_or)

#18
# Exemplo de entrada
#valor2 = True
#resultado_not = not valor2
#print("Resultado do NOT lógico:", resultado_not)

#19
# Exemplo de entrada
#num1 = 5
#num2 = 6
#resultado_igualdade = (num1 == num2)
#print("Resultado da igualdade:", resultado_igualdade)

#20
# Exemplo de entrada
#num1 = 5
#num2 = 5
#resultado_diferenca = (num1 != num2)
#print("Resultado da diferença:", resultado_diferenca)


#Tratamento de Erro
#21
#try:
    #celsius = float(input("Digite a temperatura em Celsius: "))
    #fahrenheit = (celsius * 9/5) + 32
    #print(f"{celsius}°C é igual a {fahrenheit}°F")
#except ValueError:
    #print("É necessário digitar um numero")


#22
# entrada = input("Digite uma palavra ou frase: ")
# if isinstance(entrada, str):
#     formatado = entrada.replace(" ", "").lower()
#     if formatado == formatado[::-1]:
#         print("É um palíndromo.")
#     else:
#         print("Não é um palíndromo.")
# else:
#     print("Entrada inválida. Por favor, digite uma palavra ou frase.")

#23
# try:
#     n1 = float(input("Digite o primeiro numero: "))
#     n2 = float(input("Digite o segundo numero: "))
#     op = input("Digite o operado(+, -, *, /): ")
#     if op == '+':
#         resultado = n1 + n2
#     elif op == '-':
#         resultado = n1 - n2
#     elif op == '*':
#         resultado = n1 * n2
#     elif op == '/' and n2 != 0:
#         resultado = n1 / n2
#     else:
#         print("Operador inválido ou divisão por 0")
#         resultado = ''
#     print("Resultado: ", resultado)
# except ValueError:
#    print("Erro: Entrada inválida. Certifique-se de inserir números.")

#24
# try:
#     num = int(input("Digite um número: "))
#     if num > 0:
#         print("Positivo")
#     elif num < 0:
#         print("Negativo")
#     else:
#         print("Zero")
#     if num %2 == 0:
#         print("Par")
#     else:
#         print("Ímpar")
# except ValueError:
#     print("Por favor, digite um número inteiro válido.")

#25
entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")