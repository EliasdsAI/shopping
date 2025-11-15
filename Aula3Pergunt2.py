Turma= int(input("Quantos alunos tem?"))
mediat=0
for i in range(Turma):
    print(f"Aluno{i+1}:")
    Aluno =input("Nome do aluno")
    N1 =float(input("Digite a nota"))
    N2 =float(input("Digite a nota"))
    N3 =float(input("Digite a nota"))
    N4 =float(input("Digite a nota"))
    media =(N1 + N2 + N3 +N4)/4
    mediat +=media
    print(f"Média anul de{Aluno}:{media:.2f}")
    if media >=7:
        print("Aprovado")
    else:
        print("Reprovado")

MediaTotal= mediat / Turma
print(f"Média da turma na disciplina:{MediaTotal:.2f}")
