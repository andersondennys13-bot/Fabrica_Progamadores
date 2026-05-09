# Autor: Dennys Anderson 
# Projeto: Entrada com input e f-string

#  declaraçao de variaveis
nome = input("digite seu nome: ") 
valor1 = int(input("digite o primeiro valor: "))
valor2 = int(input("digite o segundo valor: "))
soma = valor1 + valor2
subtracao = valor1 - valor2
multipicacao = valor1 * valor2
divisao = valor1 / valor2
# exibindo os resultados com f-string
print(nome) 
print(f" o resultado da soma e: {soma}")
print(f"o resultado da subtracao e: {subtracao}")
print(f"o resultado da multiplicacao e: {multipicacao} ")
print(f"o resultado da divisao e: {divisao} ")
