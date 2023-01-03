print('#################################################')
print('Bem vindo ao programa de cálculo de média escolar')
print('#################################################')
nome = input('Digite seu nome: ')
materia = input('Digite o nome da matéria ')
print('Agora você precisa informar as quatro notas')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
nota4 = float(input('Digite sua quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4)/4
if media < 7:
    print('Aluno %s, você foi REPROVADO. Sua média em %s foi de %.2f.'
          % (nome, materia, media))
else:
    print('Parabéns!!!!')
    print('Aluno %s, você foi APROVADO. Sua média em %s foi %.2f.'
          % (nome, materia, media))
