temp = float(input("Digite a temperatura:"))
if temp >= 30:
    print("Muito calor")
elif temp >= 24:
    print("Calor")
elif temp >= 17:
    print("Temperatura Amena")
elif temp >= 7:
    print("Temperatura Fria")
else:
    print("Temperatura Glacial")