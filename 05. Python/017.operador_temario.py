numero= -10
numero_absoluto = None

#if else normal

if numero <= 0:
        numero_absoluto = -numero
else:
    numero_absoluto = numero
    
print(numero_absoluto)


#operador ternario: if else en una linea

numero_absoluto = -numero if numero <= 0 else numero

## otras opciones: opcion 1 - nativa abs(), buscar en numpy
# USARLO solo en casos sencillos para evitarque:
#la sentencia se vuelva muy compleja
