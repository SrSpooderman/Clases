tu_dni = int(input("EScribe los valores sin la letra de un DNI:"))
resto = tu_dni%23
array = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
print("La letra de tu DNI es: ", array[resto])