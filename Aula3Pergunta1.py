Homens = 0
Mulheres = 0
for i in range(10):
    nome = input("Digite seu nome:")
    sexo = input("Digite seu sexo:")
    if sexo == "feminino":
        Mulheres +=1
    elif sexo == "masculino":
        Homens +=1
    else:
        print("Sexo Invalido")

print("A quantidade de pessoas:", "\nHomens:", Homens, "\nMulheres:", Mulheres)

