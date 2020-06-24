#programa para determinar s e um número é primo

n = int ( input ( "Entre com o numero : " ) )

numDivs = 0

for k in range ( 2 , n) :
    if n%k == 0 :
        numDivs += 1

if numDivs == 0 :
    print ( "Este numero e primo ! " )
else:
    print ( "Este numero nao e primo" )