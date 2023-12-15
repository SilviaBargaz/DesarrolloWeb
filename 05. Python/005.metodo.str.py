texto = "hola curso java"

#len ()calcular la longitud de un texto y de una estructura de datos
print(len(texto))


#upper () convierte a mayúsculas
print(texto.upper())

#lower () convierte minúsculas
print(texto.lower())

#lower () convierte la primera letra de la frase(sting) a mayúsculas
print (texto.capitalize())

#metodo split(cortar/dividir o partir) divide el texto en funcion de un seprarado, una lista de texto

texto.split() #sino ponemos nada dentro split () entonces separa por espacips
palabras = texto.split()
print (palabras) #['hola', 'curso', 'java']
print (palabras [0]) #hola
print (palabras [1]) #curso
print (palabras [2]) #java

#fortmat {} {} # string con dos huecos 
mensaje = "hola curso {} la nota minima es de {} puntos."
print(mensaje.format("java", 5))
print(mensaje.format("python", 5))
print(mensaje.format("spring", 7))



plantilla = " {} {} {} " # string con 3 huecos separados por espacios
texto_capitalized = plantilla.format(
    palabras [0].capitalize(),
     palabras [1].capitalize(),
      palabras [2].capitalize()
    
)

print (texto_capitalized)

# f string : cadenas con formato. permiten incrustar expresionees dentro de cadenas literales

producto = "laptop asus"
precio = 500.00 
print (f"El producto seleccionado es {producto} con {precio} euros.")

#replace (x,y) reeemplaza las ocurrencias del primer valor por el segundo valor
texto.replace
print (texto.replace( "java", "python"))
print ( "silvia sanchez". replace (" ", "")) #reemplaza todos los espacios por nada, es decir, los elimina
print ( "silvia sanchez". replace (" ", " "))

