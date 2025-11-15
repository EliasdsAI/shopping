Compra = float(input("Digite valor da compra:"))
if Compra <= 2000:
    Desconto = Compra *2/100

elif Compra > 2000 and Compra <= 3000:
    Desconto = Compra * 3/100

elif Compra > 3000 and Compra <= 5000:
    Desconto = Compra * 5/100

elif Compra > 5000:
    Desconto = Compra * 10/100

Total = Compra - Desconto
print("O valor da compra é de:", Compra, "\nO valor do deconto:", Desconto, "\nO total a pagar é:", Total)