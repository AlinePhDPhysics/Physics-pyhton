def potencia ( base , expoente ) :
    resultado = base ** expoente
    return resultado


b = float ( input ( "Entre com uma base : " ))
exp = float ( input ( "Entre com um expoente : " ) )

pot = potencia (b , exp )
print ( "Resultado de " , b , " elevado a " , exp , " : " , pot )