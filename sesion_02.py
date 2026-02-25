#tuplas
mi_tupla = (2,4)
print("mi dupla: ", mi_tupla)

#lista
mi_lista = [1, 3.1416, "odalis", mi_tupla]
print("el primer elemento  de mi lista: ", mi_lista[0])
print("el primer elemento  de mi lista: ", mi_lista[3])
print("el primer elemento  de mi lista: ", mi_lista[2])

#diccionarios
mi_diccionario = {
    "mi_lista": mi_lista,
    "nombre" : "odalis",
    "pi": 3.1416,
    "tel":"664-532-4237"
}
print("llave para accesar a mi diccionario mi lista", mi_diccionario["mi_lista"])
print("llave para accesar a mi diccionario pi", mi_diccionario["pi"])
print("llave para accesar a mi diccionario tel", mi_diccionario["tel"])