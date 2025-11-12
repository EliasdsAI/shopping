Premio = float(input("Digite o valor do premio:"))
Imposto = Premio * (7/100)
PremioTotal = Premio - Imposto
N1 = PremioTotal * (46/100)
N2 = PremioTotal * (32/100)
N3 = PremioTotal - (N1 + N2)
print(f"O premio total foi de: {PremioTotal: .2f}", f"\nO desconto foi de:{Imposto:.2f}", f"\nO primeiro ganhador ganhou:{N1:.2f}", f"\nO segundo ganhador ganhou:{N2:.2f}", f"\nE o terceiro ganhador ganhou:{N3:.2f}")