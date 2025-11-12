Bruto = float(input("Digite o valor:"))
IR = (11/100) * Bruto
INSS = (8/100) * Bruto
Sindicato = (5/100) * Bruto
Descontos = IR + INSS + Sindicato
Liquido = Bruto - Descontos
print("O funcionario recebeu ", Bruto, "teve descontos de ", Descontos, "e no final recebeu o valor de ", Liquido, "\n Os descontos foram: Inss= ", INSS, " Sindicato= ", Sindicato, " Imposto de renda= ", IR)