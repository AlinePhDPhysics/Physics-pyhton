#programa que termos e informa o maior termo lido:

numTermos = int ( input ( "Entre com o numero de termos: " ) )

maior = float ( input ( "Entre com o termo 1: " ) )

for i in range ( 2 , numTermos+1) :
    termo = float ( input ( "Entre com o termo " + str ( i ) + " : " ) )
    if termo > maior :
        maior = termo

print ( "Maior termo : " , maior )