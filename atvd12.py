# Crie um programa que receba a nota de um aluno e informe se ele foi aprovado ou reprovado. Considere que a média para aprovação é 7.
nome = input("Qual o nome do aluno? ")
nota = int(input(f"A nota da(o) aluna(o) {nome}: "))

if nota < 7:
    print (f"a(o) aluna(o) {nome} foi reprovado.")
elif nota >= 7:
    print (f'a(o) aluna(o) {nome} foi aprovado.')