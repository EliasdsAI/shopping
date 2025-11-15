PN1 = 56
PN2 = 66
nivel = int(input("Digite seu nivel:"))
Hora = int(input("Digite quantidade de horas:"))
if nivel == 1:
    salar = PN1 * Hora
    Descanso = salar * 15 / 100
    Total = salar + Descanso
    print("O salario do Professor é:", Total)

elif nivel == 2:
    salar = PN2 * Hora
    Descanso = salar * 15/100
    Total = salar + Descanso
    print("O salario do Professor é:", Total)


