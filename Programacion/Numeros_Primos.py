#imprimir todos los numeros primos hasta 100
array=[0,1,2,3,4,5,6,7,8,9]
primos=[]
for numero in range(1,200):
        div2=numero%2
        div3=numero%3
        div5=numero%5
        div7=numero%7
        if numero == 1:
            pass
        elif numero in [2,3,5,7]:
            primos.append(numero) 
        elif div2 != 0 and div3 != 0 and div5 != 0 and div7 != 0:
            primos.append(numero)
        else:
            pass
print(primos)