#crear un diccionario con las provincias argentinas y sus capitales.
provincias_argentinas={"cordoba":"cordoba","buenos aires":"la plata","catamarca":"san fernando del valle catamarca","chaco":"resistencia","chubut":"rawson","corrientes":"coriientes","entre rios":"paraná","formosa":"formosa","jujuy":"san salvador de jujuy","la pampa":"santa rosa","la rioja":"la rioja","mendoza":"mendoza","misiones":"posadas","neunquen":"neunquen","rio negro":"viedm a","salta":"salta","san juan":"san juan","san luis":"san luis","santa cruz":"rio gallegos","santa fe":"santa fe de la vera cruz","santiago del estero":"santiago del estero","tierra del fuego":"ushuaia","tucuman":"san miguel del tucuman"}

#mostrar el diccionario
for provincias, capital in provincias_argentinas.items():
    print(f"la capital de {provincias} es {capital}.")