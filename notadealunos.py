numAlunos = input ( "Digite o número de alunos : " )
numAlunos = int ( numAlunos )

contador = 1
while contador <= numAlunos:

    nota = input ( "Digite a nota do aluno " + str ( contador ) + ":" )
    nota = float ( nota )

    if nota < 5.0 :
        print ( "Aluno " , contador , " reprovado! " )
    else:
        print ( "Aluno " , contador , " aprovado! " )

    contador += 1

print ( "Tenha um bom dia! " )