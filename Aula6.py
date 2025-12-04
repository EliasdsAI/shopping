class Pessoa:
    def __init__(self, nome, data_nascimento, sexo):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.sexo = sexo

    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem}")
#def cadastrar():
  # nome = input("Digite Nome:")
 #  dnasc = input("Digite data de nascimento")
 #  sexo = input("Digite sexo:")
 #  pessoa = Pessoa(nome, dnasc, sexo)
 #  print("Nome:",pessoa.nome,"\nData de Nascimento:",pessoa.data_nascimento)


#resp = "s"
#while resp=="s":
 #     cadastrar()
 #     resp = input("Deseja continuar? ")

#pessoa1 = Pessoa("José", "20/10/1995", "masculino")
#pessoa2 = Pessoa("Maria", "15/01/2001", "feminino")

#print("Nome:",pessoa1.nome,"\nData de Nascimento:",pessoa1.data_nascimento)
#print("Nome:",pessoa2.nome,"\nData de Nascimento:",pessoa2.data_nascimento)