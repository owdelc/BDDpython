
import psycopg2
import psycopg2.extras
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
import pandas as pd
import numpy as np, numpy.random
import datetime 
import random 

# Conectividad 

conn = psycopg2.connect (
        dbname="ProyectoFinal",
        user="postgres",
        password="Krewella2001",
        host="localhost")

client = MongoClient('localhost')

db = client['prueba']
col = db['canciones']

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
    while a != 10:
        print('\nIngrese la operacion que desea realizar')
        print('1. Agregar un usuario \n' + '2. Actualizar usuario \n' + '3. Eliminar Usuario \n' + '4. Agregar Cancion \n' + '5. Modificar Cancion \n' + '6. Eliminar Cancion \n' +'7. Ver bitacora de acciones \n' + '8. Realizar simulacion de reproducciones \n' + '9. Perfilar usuario en MongoDB \n'+ '10. Salir')
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
            print('Opciones de modificacion:\n' + '1. Cambiar contraseña \n' + '2. Modificar rol')
            b = int(input('Ingrese la opcion deseada: '))
            if b == 1:
                usuario = input('Ingrese el usuario al que quiere mldificar la contraseña:')
                password1a = input('Ingrese nueva contraseña: ')
                password2a = input('Confirme nueva contraseña: ')
                if password1a == password2a:
                    try:
                        cur = conn.cursor()
                        cur.execute('UPDATE users SET password = %s WHERE name = %s;',(password1a, usuario))
                        conn.commit()
                        cur.close()
                        print('Modificacion realizada exitosamente!')
                    except (Exception, psycopg2.DatabaseError) as error:
                        print("Error en la transaccion, revirtiendo operaciones ", error)
                        conn.rollback()
            if b == 2:
                usuario2 = input('Ingrese el usuario al que quiere mldificar el rol: ')
                nrol = int(input('Ingrese el nuevo rol: '))
                try:
                    cur = conn.cursor()
                    cur.execute('UPDATE users SET rol = %s WHERE name = %s;',(nrol, usuario2))
                    conn.commit()
                    cur.close()
                    print('Modificacion realizada exitosamente!')
                except (Exception, psycopg2.DatabaseError) as error:
                    print("Error en la transaccion, revirtiendo operaciones ", error)
                    conn.rollback()
        if a == 8:
            generador()


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
            
        if a == 9:
            perfilar()


def generador():
    songs = { 
        'cancion1':{'nombre':'Shape of you', 'album':'Counting star' , 'artista':'saijs'},
        'album':{'nombre':'Shape of you', 'album':'Counting star' , 'artista':'saijs'},
        'artista': {'nombre':'Shape of you', 'album':'Counting star' , 'artista':'saijs'},
        'Eraser': {'nombre':'Shape of you', 'album':'Counting star' , 'artista':'saijs'},
        'Dive': {'nombre':'Shape of you', 'album':'Counting star' , 'artista':'saijs'},
        'Perfect': {'nombre':'Shape of you', 'album':'Counting star' , 'artista':'saijs'},
        'Cielo en la tierra': {'nombre':'Shape of you', 'album':'Counting star' , 'artista':'saijs'},
        'Holy': {'nombre':'Shape of you', 'album':'Counting star' , 'artista':'saijs'},
        'Happier': {'nombre':'Shape of you', 'album':'Counting star' , 'artista':'saijs'},
        'Habitual': {'nombre':'Shape of you', 'album':'Counting star' , 'artista':'saijs'},
        'Forever': {'nombre':'Shape of you', 'album':'Counting star' , 'artista':'saijs'}
        }
    
    usuarios = {
        'oscar',
        'hugo',
        'roberto',
        'julio',
        
    }
    
    a = int(input("Ingrese la cantidad de tracks a generar: "))
    rep = int(input("Ingrese la cantidad de reproducciones: "))
    date = input("fecha: ")

    for i in range (a):
        song = random.choice(list(songs))
        for j in range(rep):
            cur = conn.cursor()
            cur.execute("INSERT INTO repro(usuario,nombre, album, artista, fecha) VALUES(%s,%s,%s,%s,%s);",(song,date))
            conn.commit()
            cur.close()
            
#Perfilar usuario en Mongo
def perfilar():
    usuario = input('Ingrese usuario que desea perfilar: ')
    fecha = input('Ingrese fecha de perfilamiento: ')
    
    cur = conn.cursor()
    cur.execute("select nombre from reproducciones Where usuario = %s and fecha = %s;",(usuario, fecha))
    resultado = cur.fetchall()
    #resultado = [i [] for i in cur.fetchall()]
    #resultado2 = [i [1] for i in cur.fetchall()]
    print(resultado)
    cur.execute("select genero, count(genero) as total from reproducciones Where usuario = %s and fecha = %s group by genero;",(usuario, fecha))
    resultado2 = cur.fetchall()
    print(resultado2)
    conn.commit()
    cur.close()
    
    new = {
        "user":usuario,
        "fecha":fecha,
        "canciones":resultado,
        "generos":resultado2}
    col.insert_one(new)

"""    
def recomendaciones():
    fecha = input('Ingrese fecha para sacar recomendaciones: ')
    cur = conn.cursor()
    cur.execute() 
"""

#Log in y Register 

print('Bienvenido')
print('1. Log In\n' + '2. Register')

############################
numero = int(input("numero: "))
canciones = int(input('canciones: '))
rs = []
for i in range(numero):
    r = random.random()
    numero = numero - r
    rs.append(r)

print(rs)
############################

opcion1 = int(input('Ingrese el numero de su eleccion: '))



if opcion1 == 1:
    username = input("Ingrese ususario: ")
    password = input("Ingrese contaseña: ")
    Login(username, password)
    
if opcion1 == 2:   
    SignUp()
    
    


