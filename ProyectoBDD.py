
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
    cur.execute('select %s from users;', [username])
    userp = [i [0] for i in cur.fetchall()]
    if userp == [username]:
        cur.execute('select %s from users;',[password])
        passp = [i [0] for i in cur.fetchall()]
        if passp == [password]:
            cur.execute('select rol from users')
            roles = [i [0] for i in cur.fetchall()]
            if roles == [1]:
                print("Admin user")
                #AdminUser()
            if roles == 'free':
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


def SignUp(username,password1,password2):
    if password1 == password2:
        cur = conn.cursor()
        cur.execute('insert into users (nombre,password) values (%s,%s);' [username,password1])
        print("Registro Exitoso")
        Login()


#Log in y Register 

print('Bienvenido')
print('1. Log In\n' + '2. Register')
opcion1 = int(input('Ingrese el numero de su eleccion: '))

if opcion1 == 1:
    username = input("Ingrese ususario: ")
    password = input("Ingrese contaseña: ")
    Login(username, password)
    
if opcion1 == 2:
    username = input("Ingrese usuario: ")
    password1 = input("Ingrese contraseña: ")
    password2 = input("Confirme contraseña: ")
    SignUp(username, password1, password2)
    
    
