n = int(input("Quantidade de alunos: "))
soma = 0
contador = 0

while contador < n:
    nota = float(input("Digite a nota do aluno: "))
    soma += nota
    contador += 1

media = soma / n
print("A média da turma é:", media)