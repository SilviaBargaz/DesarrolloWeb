
email_correcto = 'admin@gmail.com'
password_correcta = '1234'


email = input ('introduce to email: ')
password = input('Introduce password:  ')


if email == email_correcto and password == password_correcta:
     print('credenciales correctas')
else:
    print('redenciales incorrectas')
    
    
    
#or O
#flexible por que estrue si aal menos se cumple
#una condicion 

es_estudiante = input('¿es estudiante ? si o no: ') == 'si' #True o False
precio = float(input('introduce el precio de tu compra : '))

if es_estudiante or precio >= 100:
    print(f"descuento del 20%, precio final :{precio *0.80} ")
else:
    print(f"precio final: {precio}")
    
#not invierte una condición o bool existente
edad = int(input ('introduce tu edad'))
if not edad >= 18:
    print ('no tiene acceso.')
    #ejemplo not: todos los campos son obligatorios
    #si email o password estan vacias entonces se cumple if
    
if not email or not password:
    print('todos los campos son obligatorios.')
else: 
    print('registro completo.')
    

   