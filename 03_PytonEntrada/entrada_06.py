# Autor: Dennys Anderson 
# Projeto: IMC com input e f-string

#  declaraçao de variaveis 
peso = float(input("digite o seu peso : "))
altura = float(input("digite sua altura: "))
imc = peso / (altura * altura)

# exibindo os resultados 
print(f"seu imc e: {imc}")