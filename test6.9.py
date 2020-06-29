#calculo do IMC
a = float(input('Digite o seu peso: '))
b = float(input('Digite a sua altura: '))
a = float(a) 
b = float(b)

imc = (a/(b**2))
imc = float (imc)
print ('O seu IMC é:'"%.2f" % imc)
if imc <= 18.5:
    print ('magreza')
if imc >= 18.5 and imc <= 24.9: 
    print ('normal') 
if imc>=25.0 and imc<=29.9: 
    print ('sobrepeso') 
else:
    if imc>30.0:
        print ('Você está obeso!Precisa de dieta e atividades físicas!')
print ('Obrigado por realizar o teste!')
