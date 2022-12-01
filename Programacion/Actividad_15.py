uno = input("Que año estamos?: ")
dos = input("Un año cualquiera: ")
if uno or dos == str:
    print("Son strings no funciona")
else:
    if uno < dos:
        print("Para llegar al año ",dos," faltan",dos-uno)
    elif uno > dos:
        print("Desde el año ",dos," han pasado", uno-dos)
    elif uno == dos:
        print("Son el mismo año!")