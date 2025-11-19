F = 0
QDH = 0
M = 0
QDM = 0
NN = 0
resp = (input("Entrar no Cadastro? Digite S para sim ou qualquer tecla para não - ")).strip().upper()
while resp == "S":
 nome = input("Digite o nome da pessoa: ")
 sexo = input("Digite o sexo da pessoa (M/F): ").strip().upper()
 altura = float(input("Digite sua altura:"))
 if sexo == 'M':
     M +=1
 elif(sexo == 'M' and altura >= 1.7):
    QDH += 1
 elif sexo == 'M' and altura <= 1.6:
    NN +=1
 elif sexo == 'F':
     F += 1
 elif sexo == 'F' and altura >= 1.65:
    QDM += 1
 elif sexo == 'F' and altura <= 1.6:
    NN +=1
 else:
    print("Error")

 resp = (input("Continuar no Cadastro? Digite S para sim ou qualquer tecla para não - ")).strip().upper()

print(f"Quantidade de Homens:{M} e Mulheres{F}")
print(f"Quantidade de homens altura superior a 1.7: {QDH}")
print(f"Quantidade de Pessoas altura menor a 1.6: {NN}")
print(f"Quantidade de mulheres com altura superior 1.65 : {QDM}")


