from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()

libreriaBD = cliente["libreria"]
librosColeccion = libreriaBD["libros"]

print("Libros en el que el numero de paginas sea 1072")

miquery = { "paginas": 1072 } 

libros = librosColeccion.find(miquery,{"_id": 0}) 

for l in libros:
    print(l)

print("\n")

print("Libros con precio mayor o igual a 5 y el titulo empiece por 1")

miquery = { "$and": [
    { "precio" : {"$gte":5} },
    { "titulo" : {"$regex":"^1"}}
] } 

libros2 = librosColeccion.find(miquery,{"_id": 0}) 

for r in libros2:
    print(r)

print("\n")

print("Libros que no tengan mas de 600 paginas y no cuesten mas de 30")

miquery = { "$and": [
    { "paginas" : {"$lt":600} },
    { "precio" : {"$lt":30}}
] } 

libros3 = librosColeccion.find(miquery,{"_id": 0}).sort("titulo",-1) 

for t in libros3:
    print(t)

print("\n")

resultado = librosColeccion.delete_one({"titulo":"1984"})

print(resultado.deleted_count, " documentos eliminados")

print("\n")

miquery = {"titulo":"El Principito"}
nuevosValores = {"$set": {"precio":10}}

resultado = librosColeccion.update_one(miquery, nuevosValores)

