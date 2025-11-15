quantidade_homens = 0
quantidade_mulheres = 0
qt = int(input("Quantas pessoas você deseja cadastrar? "))
contador = 0
while contador < qt:
    nome = input("Digite o nome da pessoa: ")
    sexo = input("Digite o sexo da pessoa (M/F): ").strip().upper()
    if sexo == 'M':
        quantidade_homens += 1
    elif sexo == 'F':
        quantidade_mulheres += 1
    else:
        print("Sexo inválido! Por favor, digite 'M' para masculino ou 'F' para feminino.")
        continue
    contador += 1

print(f"Quantidade de homens: {quantidade_homens}")
print(f"Quantidade de mulheres: {quantidade_mulheres}")