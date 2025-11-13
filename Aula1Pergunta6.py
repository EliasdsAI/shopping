Pao = int(input("Numero de pães:"))
Broa = int(input("Numero de Broas:"))
PP = Pao * 0.8
PB = Broa * 2.5
Tot = PP + PB
CF = Tot * 43/100
Restante = Tot - CF
CP = Restante * 15/100
Viagem = Restante * 15/100
Euro = Viagem / 6.14
print(f"A quantidade de pão={Pao:.2f}", f"\nQuantidade de Broas={Broa:.2f}", f"\nO total da venda={Tot:.2f}", f"\nCusto de fabricação={CF:.2f}", f"\nPoupança={CP:.2f}", f"\nEuros={Euro:.2f}")
