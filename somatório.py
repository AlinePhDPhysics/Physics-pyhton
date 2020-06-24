#programa que c a l c u l a o somatório de termos fornecidos pelo usuário:

numTermos = int ( input ( "Entre com o numero de termos : " ) )

soma = 0
for k in range ( 0 , numTermos ) :

    termo = float ( input ( "Entre com o termo " + str ( k+1 ) + " : " ))

    soma += termo

print ( " Somatorio dos termos : " , soma )