#Given a number count the total number of digits in a number
num = input ("Digite um número extenso qualquer: ")
num = int (num)
count = 0

while num != 0:
    num //= 10
    count+= 1
print("O total de dígitos neste número é: ", count)