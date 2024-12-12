1=[]
while true: #condicion a evaluar
    opcion=imput("menu de opcion\n1-agregar producto\n2-eliminar producto\n3-modificar producto\n4-mostrar producto\n5-salir \n")
    if opcion=="1":
        elementoAgregar=imput("ingrese el elementoa agregar: ")
        l.append(elementosAgregar)
    elif opcion=="2":
        elemntosAeliminar=imput("ingrese el nombre del elemento a modificar: ")
        if elementoAeliminar in l:
            l.remove(elemntoaeliminar)
            print("elento eliminado exitosacamente")
        else:
            print("el elmento que desea eliminar no se encuentra en la lista")
            elif opcion=="3"
elementoAmodificar=input("ingrese el nombre del elemnto a modificar: ")
if elementoAmodificar in l:
    elementoAmodificacion=imput("ingrese el nombre por el que quere modificar: ")
    #fin