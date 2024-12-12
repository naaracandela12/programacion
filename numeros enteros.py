#incializamos la suma total
suma_total=0

#pedimos al usario que ingrese un numero
numero=int(input("ingrese un numero entero:"))
#bucle que se ejecuta hasta que el usario ingresa 0
while numero!=0:
    #si el nuemro es pórsetivo, lo sumamos a la suma total
    if numero>0:
        suma_total+=numero

        #pedimosa al usario que ingrese otro numero
        numero=int(input("ingrese otro numero entero:"))

        #inprimimos la suma total
        print("la suma total de los numeros positivos es:",suma_total)

