
nota = int(input("ingrese una nota 0-10 :"))

while nota >10 or nota <0:
    print ("nota invalida, vuelva a ingresar")
    nota = int(input(" ingrese una nota 0 - 10"))

    print (f" tu nota: + { nota}")
