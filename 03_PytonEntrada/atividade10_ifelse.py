nome = input("digite seu nome: ")
telefone = input("digite seu telefone: ")
cidade = input("digite a sua cidade: ")
salario = float(input("digite o seu salario "))

if salario >= 1000:
    print("voce possui uma renda boa")
elif salario >= 700:
    print("voce possui uma renda estavel")
else:
    print("voce possui uma renda baixa ")
