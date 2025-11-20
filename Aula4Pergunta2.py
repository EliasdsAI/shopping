QPD = 0
QPC = 0
QPP = 0
resp = (input("Entrar no Cadastro? Digite S para sim ou qualquer tecla para não - ")).strip().upper()
while resp == "S":
 nome = input("Digite o nome do paciente: ")
 idade = int(input("Digite a idade:"))
 Doutor = input("Nome do médico:")
 esp = input("Digite a especialidade sendo P pra Pediatria ou C para Clinica:")

 if esp == "C":
     QPC += 1
 elif esp == "P":
     QPP +=1
 else:
     print("Error")
     continue
 QPD += 1


 resp = (input("Continuar no Cadastro? Digite S para sim ou qualquer tecla para não - ")).strip().upper()
print(f"Quantidade de Pacientes no dia são:{QPD}")
print(f"Quantidade de pacientes na clinica são:{QPC}")
print(f"Quantidade de pessoas na pediatria são:{QPP}")