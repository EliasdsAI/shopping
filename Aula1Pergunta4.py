import math

Altura =float(input("Digite a altura da parede:"))
Com = float(input("Digite o comprimento da parede:"))
LT = 3.6
Area = Altura * Com
Litros = Area / 3
QT = Litros / 3.6
QT = math.ceil(Litros / 3.6)
PF = QT * 107
print("A quantidades de tintas são: ", QT, " e o valor a ser pago é de: ", PF, "\nA area total é de=", Area , "\nQuantidade de tintas foram = ", Litros)