#lo mismo pero con un maximo de [3 intentos]
#ejemplo 2


password = 'admin'
password_user = ' '
intento = 1 #contador para el numero de intentos
max_intentos = 3

while intento <= 3:
    password_user = input('introduce tu contraseña: ')
    if password_user == password:
        print('credenciales correctas.')
        #invocar una funcion que realice la accion deseada
        break #es para romper (salir) el bucle
    #break es una palabra clave en Python que se utiliza para salir de un bucle 
    #(ya sea un bucle for o while) antes de que se complete su ejecución normal. 
    intento += 1 # hasta aqui puede ir el codigo con print fin
    #pero tambien puedes agregar if intento

if intento > max_intentos:
    print('alcanzado limite maximo de intentos (3)')

print ('fin')


