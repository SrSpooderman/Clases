#Array modificable
array = []
#Empieza el bucle bastante bonito xd
for pasada in range (len(array)):
    min = array[len(array)-1]
    #print("es la pasada", pasada)
    min_pos = len(array)
    #Segundo bucle para saber cual es el numero mas pequeño dentro del array "max(array)"
    for num in range(pasada,len(array)):
        #print("el numero es :",array[num])
        if array[num] < min:
            min = array[num]
            min_pos = num
        elif array[num] > min:
            pass
        elif array[num] == min:
            min = array[num]
            min_pos = num
    #Aqui se colocan los datos dentro del array, el comentario es para comprobar
    #print("pongo el numero",min, "en la posicion", pasada)
    array.pop(min_pos)
    array.insert(pasada,min)
#printar el array ya ordenado, los comentarios son para comprobar
    #print(array)
    #print("---")
print(array)
