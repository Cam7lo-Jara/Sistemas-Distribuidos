import firebase_admin
from firebase_admin import credentials
from firebase_admin import db 

firebase_sdk = credentials.Certificate('C:/Users/camil/OneDrive/Documents/Documentos/Camilo/Universidad/Sistemas distribuidos/sistemas-distribuidos-fd365-firebase-adminsdk-8und0-3febd669ed.json')
firebase_admin.initialize_app(firebase_sdk,{'databaseURL':'https://sistemas-distribuidos-fd365-default-rtdb.firebaseio.com/'})


ref =db.reference('/Automoviles')
ref.push({'Marca':'Chevrolet','Modelo':'Spark life','Año':'2019'})

ref.push({'Marca':'Renault','Modelo':'Logan','Año':'2017'})

ref.push({'Marca':'Chevrolet','Modelo':'Aveo','Año':'2010'})

ref.push({'Marca':'Mazda','Modelo':'2','Año':'2023'})

ref1 =db.reference('/Camionetas')

ref1.push({'Marca':'Mazda','Modelo':'CX5','Año':'2023'})

ref1.push({'Marca':'Chevrolet','Modelo':'Tracker','Año':'2021'})

ref1.push({'Marca':'Renault','Modelo':'Alaskan','Año':'2023'})

ref1.push({'Marca':'Renault','Modelo':'Duster','Año':'2021'})
