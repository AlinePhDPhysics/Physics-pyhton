n = input ('Digite um número inteiro qualquer: ')
n = int (n)

if n<= 11:
    for n in range(1, 11, 1):
        n = n+1
        print (n)
else:
    if n > 11:
        print("Feito!")