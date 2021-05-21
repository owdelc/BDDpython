
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
    #print(userp)
    if userp == [username]:
        cur.execute('select password from users where password = %s;',[password])
        passp = [i [0] for i in cur.fetchall()]
        print(passp)
        if passp == [password]:
            cur.execute('select rol from users where name = %s;',[username])
            roles = [i [0] for i in cur.fetchall()]
            if roles == [1]:
                print("*********************************\n" + "Bienvenido a Administracion")
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
    while a != 9:
        print('Ingrese la operacion que desea realizar')
        print('1. Agregar un usuario \n' + '2. Actualizar usuario \n' + '3. Eliminar Usuario \n' + '4. Agregar Cancion \n' + '5. Modificar Cancion \n' + '6. Eliminar Cancion \n' +'7. Ver bitacora de acciones \n' + '8. Realizar simulacion de reproducciones \n' + '9. Salir \n')
        a = int(input('La operacion que desea realizar: '))
        
        #Agregar usuario
        if a == 1:
            usuario = input('Ingrese usuario que desea registrar: ')
            password1 = input('Ingrese contraseña: ')
            password2 = input('Confirme contraseña: ')
            print('Debe designar un tipo de usuario. Las opciones son las siguientes: \n' + '1. Administrador \n' + '2. Freemium \n' + '3. Premium \n' + '4. Artista/Manager')
            tipo = int(input('Tipo de usuario: '))
            try:
                cur = conn.cursor()
                cur.execute('INSERT INTO users(name,password,rol) VALUES(%s,%s,%s);',(usuario, password1, tipo))
                conn.commit()
                cur.close()
                print('Ingreso exitoso! Usuario: ' + usuario + ' Contraseña: ' + password1)
            except (Exception, psycopg2.DatabaseError) as error:
                print("Error en la transaccion, revirtiendo operaciones ", error)
                conn.rollback()
            
        #Editar usuario
        if a == 2:
            print("opcion")
        
        #Eliminar usuario
        if a == 3:
            usuario1 = input('Ingrese el usuario que desea eliminar: ')
            usuario2 = input('Confirme usuario que desea eliminar: ')
            if usuario1 == usuario2:
                try:
                    cur = conn.cursor()
                    cur.execute('DELETE FROM users WHERE name = %s;',[usuario1])
                    conn.commit()
                    cur.close()
                    print(usuario1, ' Eliminado correctamente')
                except (Exception, psycopg2.DatabaseError) as error:
                    print('Error en la ejecucion' , error)
        
        
        #Agregar cancion       
        if a == 4:
            titulo = input('Ingrese titulo de la cancion: ')
            album = input('Ingrese album al que pertene la cancion: ')
            artista = input('Ingrese artista al que pertenece la cancion: ')
            anio = int(input('Ingrese año de lanzamiento: '))
            url = input('Ingrese url de reproduccion: ')
            reproducciones = 0
            try:
                cur = conn.cursor()
                cur.execute('INSERT INTO canciones(cancion, album, artista, anio, url, reproducciones) VALUES(%s,%s,%s,%s,%s,%s);',[titulo, album, artista, anio, url, reproducciones])
                conn.commit()
                cur.close()
                print('Ingreso exitoso! Titulo: ' + titulo + ' Album: ' + album + ' Artista: ' + artista)
            except (Exception, psycopg2.DatabaseError) as error:
                print("Error en la transaccion, revirtiendo operaciones ", error)
                conn.rollback()
            
        #Editar cancion
        if a == 5:
            print("opcion")
            
        #Eliminar cancion
        if a == 6:
            cancion = input('Ingrese cancion que desea eliminar: ')
            album = input('Ingrese album al que pertenece la cancion: ')
            try:
                    cur = conn.cursor()
                    cur.execute('DELETE FROM canciones WHERE cancion = %s AND album = %s;',[cancion, album])
                    conn.commit()
                    cur.close()
                    print(cancion, ' eliminada correctamente')
            except (Exception, psycopg2.DatabaseError) as error:
                    print('Error en la ejecucion' , error)
            
        
        if a == 7:
            print("opcion")
        if a == 8:
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
    
    
