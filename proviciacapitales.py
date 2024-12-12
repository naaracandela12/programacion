#crear un programa que guarde en un diccionario las provincias argentinas
#con sus respectativa capitale4s, luego las muestro
provincias={"cordoba":"cordoba","buenos aires":"la plata",}

pciabuscarvalorcapital=input("ingresar provincia a buscar capital: ")
#buscamos elementos al diccionario
x = provincias[pciabuscarvalorcapital]
print("su capital es" ,x)
print("_______________")
#agregar elementos al diccionario
pciaAgregar=input("ingrese la provincia que desea agregar:")
capitalpcia=input("ingrese la capital de la provincia argentina:")
provincias[pciaAgregar]=capitalpcia
print("________________")


for p, c in provincias.intems():
    print("_", c)