#leer un buleano hasta que el usuario escriba una edad correcta 18 a 100

while True:
    #para capturar valueError : invalid literal for int()whit base 10: 'hola'
    #este codigo ejecutado sin try y sin except paras que suceds la captura
    try:
        edad = int(input('introduce tu edad (18 - 100): '))
        if  18 <= edad <= 100:
            print('edad correcta.')
            break
        
    except ValueError:
        print('formato de datos incorrecto')
           

    
#leer un booleano hasta que este bien escrito
