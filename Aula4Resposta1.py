qth = 0
qtm = 0
alt160h = 0
alt170h = 0
alt160m = 0
alt165m = 0

print("************************ Inscrição *********************************")
resp = (input("Entrar no Cadastro? Digite S para sim ou qualquer tecla para não - ")).strip().upper()
while resp == "S":
    nome = input("Nome do Candidato: ")
    sexo = input("Sexo do Candidato (M/F): ").strip().upper()
    altura = float(input("Altura do Candidato: "))

    if sexo == 'M':
        qth += 1
        if altura > 1.70:
            alt170h += 1
        elif altura < 1.60:
            alt160h += 1
    elif sexo == 'F':
        qtm += 1
        if altura > 1.65:
            alt165m += 1
        elif altura < 1.60:
            alt160m += 1
    else:
        print("Sexo inválido! Por favor, digite 'M' para masculino ou 'F' para feminino.")
        continue

    resp = (input("Continuar no Cadastro? Digite S para sim ou qualquer tecla para não - ")).strip().upper()


print(f"Quantidade de homens: {qth}")
print(f"Quantidade de homens com altura superior a 1.70m : {alt170h}")
print(f"Quantidade de homens com altura inferior a 1.60m : {alt160h}")
print(f"Quantidade de mulheres: {qtm}")
print(f"Quantidade de mulheres com altura superior a 1.65m : {alt165m}")
print(f"Quantidade de mulheres com altura inferior a 1.60m : {alt160m}")