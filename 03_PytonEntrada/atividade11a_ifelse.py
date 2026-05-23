nome = input("digite seu nome: ")
idade = int(input("digite sua idade: ") )
cnh = input("possui CNH 1=sim ou 2=nao")
if idade >= 18:
    if cnh == "1":
        print(f"{nome} voce pode dirigir")
    else:
        print(f"{nome} voce nao pode dirigir")
else:
        print(f"{nome}voce e menor de idade")