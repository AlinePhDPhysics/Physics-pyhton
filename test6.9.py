#calculo do IMC
a = float(input('Digite o seu peso: '))
b = float(input('Digite a sua altura: '))
a = float(a) 
b = float(b)

imc = (a/(b**2))
imc = float (imc)
print ('O seu IMC é:'"%.2f" % imc)
if imc>30.0:
    print ('Você está obeso!Precisa de dieta e atividades físicas!')
else: 
    if imc<30.0:
         print ("Parabéns! Você está no peso ideal!")


