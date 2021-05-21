
import psycopg2
import psycopg2.extras
#from pymongo import MongoClient
#from pymongo import ASCENDING, DESCENDING

# Conectividad 

conn = psycopg2.connect (
        dbname="ProyectoFinal",
        user="postgres",
        password="Krewella2001",
        host="localhost")


#client = MongoClient('localhost')

#db = client['']
#col = db['']

#Funciones 

def Login(username,password):
    cur = conn.cursor()
    cur.execute('select name from users where name = %s;', [username])
    userp = [i [0] for i in cur.fetchall()]
    print(userp)
    if userp == [username]:
        cur.execute('select password from users where password = %s;',[password])
        passp = [i [0] for i in cur.fetchall()]
        print(passp)
        if passp == [password]:
            cur.execute('select rol from users where name = %s;',[username])
            roles = [i [0] for i in cur.fetchall()]
            if roles == [1]:
                print("*********************************")
                AdminUser()
            if roles == [2]:
                print("Free user")
                #FreeUser()
            if roles == 'premium':
                print("Premium user")
                #PremiumUser()
            if roles == 'artist':
                print("Artist user")
                #ArtistUser()

        else:
            print("Password is incorrect.")
        

    else:
        print("Username is incorrect.")


def SignUp():
    username = input("Ingrese usuario: ")
    password1 = input("Ingrese contraseña: ")
    password2 = input("Confirme contraseña: ")
    tipo = 2
    if password1 == password2:
        try:
            cur = conn.cursor()
            cur.execute('INSERT INTO users(name,password,rol) VALUES(%s,%s,%s);',(username, password1, tipo))
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error en la transaccion, revirtiendo operaciones ", error)
            conn.rollback()

# Definicion de funcionalidades de Administrador 
def AdminUser():
    a = 0
    while a != 6:
        print('Ingrese la operacion que desea realizar')
        print('1. Agregar un usuario \n' + '2. Actualizar usuario \n' + '3. Eliminar Usuario \n' + '4. Ver vitacora de acciones \n' + '5. Realizar simulacion de reproducciones \n' + '6. Salir \n')
        a = int(input('La operacion que desea realizar: '))
        
        if a == 1:
            usuario = input('Ingrese usuario que desea registrar: ')
            password1 = input('Ingrese contraseña: ')
            password2 = input('Confirme contraseña: ')
            print('Debe designar un tipo de usuario. Las opciones son las siguientes: \n' + '1. Administrador \n' + '2. Freemium \n' + '3. Premium \n' + '4. Artista/Manager')
            tipo = int(input('Tipo de usuario: '))
            
        
        if a == 2:
            print("opcion")
        if a == 3:
            print("opcion")
        if a == 4:
            print("opcion")
        if a == 5:
            print("opcion")

#Log in y Register 

print('Bienvenido')
print('1. Log In\n' + '2. Register')
opcion1 = int(input('Ingrese el numero de su eleccion: '))

if opcion1 == 1:
    username = input("Ingrese ususario: ")
    password = input("Ingrese contaseña: ")
    Login(username, password)
    
if opcion1 == 2:
    
    SignUp()
    
    
