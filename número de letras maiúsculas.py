"""Programa que lê uma string do teclado e conta o número de caracteres maiúsculos"""

texto = input ( "Entre com o texto : " )

nmaiusculos = 0
for c in texto :
    if "A" <= c <= "Z" :
        nmaiusculos += 1

print ( "Numero de caracteres maiúsculos: " , nmaiusculos )