import psycopg2
import psycopg2.extras
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING




print('Bienvenido')
print('1. Log In\n' + '2. Register')
opcion1 = int(input('Ingrese el numero de su eleccion: '))

if opcion1 == 1:
    print('Inicie sesion')
    
if opcion1 == 2:
    print('Registro de usuario')
    
    
