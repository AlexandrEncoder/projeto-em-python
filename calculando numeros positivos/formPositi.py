import numpy
print("Formula \nd = r + S / 2, \nOnde:\n R = (A + B)^2 e S = (B + C)^2 \n")
n1=n2=n3=0
while True:
    firstNumb = int(input("Digite o primeiro numero: "))
    if firstNumb < 0:
        print("APENAS NUMEROS INTEIRO: ")
    else:
        n1=firstNumb
        while True:
            secondNum = int(input('Digite o segundo numero: '))
            if secondNum < 0:
                print("APENAS NUMEROS INTEIRO: ")
            else:
                n2=secondNum
                while True:
                    thirtNumb = int(input('Digite o terceiro numero: '))
                    if thirtNumb < 0:
                        print("APENAS NUMEROS INTEIRO: ")
                    else:
                        n3 = thirtNumb
                        break

                break
        break

r = (n1+n2)**2
s = (n2+n3)**2
d = (r+s)/2

print(f'O resultado da equação d = r + S / 2, onde R = ({n1} + {n2})^2 e S = ({n2} + {n3})^2 é : \n{d}')