from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()

baseDatos = cliente["oceanos"]

coleccion = baseDatos["zonas"]

#1 - Inserta un registro en una Colección (0.5 puntos)
print("\n- Apartado 1:")
#Crear un documento
documento = {"nombre":"Pacífico", "ubicacion":"hawai","descripcion":"Concentracion de residuos plasticos", "nivel_contaminacion":"media","tipo_contaminacion":"plasticos","area":50,"biodiversidad":"delfines" }

# Insertar el documento en la colección
resultado = coleccion.insert_one(documento)

# Mostrar el ID del documento insertado
print("\nDocumento insertado con ID:", resultado.inserted_id)

#2 - Insertar varios registros en una Coleccion  (0.5 puntos)
print("\n- Apartado 2:")
#Crear varios documentos
documentos = [
    {
        "nombre": "Pacífico",
        "ubicacion": "Caribe",
        "descripcion": "Derrame de petróleo en zona costera",
        "nivel_contaminacion": None,
        "tipo_contaminacion": "petróleo",
        "area": 120,
        "biodiversidad": "tiburones"
    },
    {
        "nombre": "Mar Mediterráneo",
        "ubicacion": "Europa",
        "nivel_contaminacion": "media",
        "tipo_contaminacion": "microplásticos",
        "area": 35,
        "biodiversidad": "tortugas marinas"
    },
    {
        "nombre": "Pacífico Sur",
        "ubicacion": "Australia",
        "descripcion": "Contaminación por redes de pesca abandonadas",
        "nivel_contaminacion": "alta",
        "tipo_contaminacion": "redes de pesca",
        "area": 70,
        "biodiversidad": None
    },
    {
        "nombre": "Ártico",
        "ubicacion": "Círculo Polar Ártico",
        "descripcion": "Aumento de contaminantes químicos por derretimiento de hielos",
        "nivel_contaminacion": "baja",
        "tipo_contaminacion": "químicos",
        "area": 15,
        "biodiversidad": "osos polares"
    },
    {
        "nombre": "Océano Índico",
        "ubicacion": "Sudeste Asiático",
        "descripcion": "Altas concentraciones de basura marina",
        "nivel_contaminacion": "media",
        "tipo_contaminacion": "basura marina",
        "area": 90,
        "biodiversidad": "manta rayas"
    }
]


#Insertar varios documentos
resultado = coleccion.insert_many(documentos)

# Mostrar los IDs de los documentos insertados
print("\nDocumentos insertados con IDs:", resultado.inserted_ids)

#3 - Actualizar un registro de una Colección  (0.5 puntos)
print("\n- Apartado 3:")

# Solicitar al usuario el filtro de búsqueda
print("Introduce el campo y valor para el filtro de búsqueda (por ejemplo, nombre: Pacífico):")
campo_filtro = input("Campo de filtro: ")
valor_filtro = input("Valor de filtro: ")

filtro = {campo_filtro: valor_filtro}

# Cambios a realizar
print("Introduce los campos y valores para la actualización (por ejemplo, nivel_contaminacion: alta):")
campo_actualizacion = input("Campo de actualización: ")
valor_actualizacion = input("Valor de actualización: ")

actualizacion = {"$set": {campo_actualizacion: valor_actualizacion}}

# Actualizar un documento
resultado = coleccion.update_one(filtro, actualizacion)

print(f"\nDocumentos encontrados: {resultado.matched_count}")
print(f"\nDocumentos modificados: {resultado.modified_count}")

#4 - Actualizar varios registros en una Colección  (0.5 puntos)
print("\n- Apartado 4:")

# Solicitar al usuario el filtro de búsqueda
print("Introduce el campo y valor para el filtro de búsqueda (por ejemplo, area: 90):")
campo_filtro = input("Campo de filtro: ")
valor_filtro = input("Valor de filtro: ")

# Crear el filtro dinámico
filtro = {campo_filtro: eval(valor_filtro)}

# Solicitar al usuario los campos a actualizar y sus nuevos valores
print("Introduce los campos y valores para la actualización (por ejemplo, area: 85):")
campo_actualizacion = input("Campo de actualización: ")
valor_actualizacion = input("Valor de actualización: ")

# Crear el documento de actualización
actualizacion = {"$set": {campo_actualizacion: eval(valor_actualizacion)}}

# Realizar la actualización
resultado = coleccion.update_many(filtro, actualizacion)

# Mostrar el resultado
print(f"\nDocumentos encontrados: {resultado.matched_count}")
print(f"\nDocumentos modificados: {resultado.modified_count}")

#5 - Obtener varios registros por un filtro de un atributo dentro de una Colección  (0.5 puntos)
print("\n- Apartado 5:")

# Solicitar al usuario el filtro de búsqueda
print("Introduce el campo y valor para el filtro de búsqueda (por ejemplo, nivel_contaminacion: alta):")
campo_filtro = input("Campo de filtro: ")
valor_filtro = input("Valor de filtro: ")

# Crear el filtro dinámico
filtro = {campo_filtro: valor_filtro}

# Obtener los documentos que coinciden con el filtro
documentos = coleccion.find(filtro)

# Mostrar los documentos obtenidos
print(f"\nDocumentos encontrados con {campo_filtro} = {valor_filtro}:")
for documento in documentos:
    print(f"\n{documento}")

#6 - Obtener varios registros por un filtro por varios atributos dentro de una Colección  (0.5 puntos)
print("\n- Apartado 6:")

# Solicitar al usuario los valores para el filtro $or
print("Introduce los campos y valores para el filtro $or:")
campo_filtro1 = input("Campo de filtro 1 (por ejemplo, nivel_contaminacion): ")
valor_filtro1 = input("Valor de filtro 1 (por ejemplo, alta): ")

campo_filtro2 = input("Campo de filtro 2 (por ejemplo, tipo_contaminacion): ")
valor_filtro2 = input("Valor de filtro 2 (por ejemplo, basura marina): ")

# Crear el filtro dinámico con $or
filtro = {
    "$or": [
        {campo_filtro1: valor_filtro1},
        {campo_filtro2: valor_filtro2}
    ]
}

# Obtener los documentos que coinciden con el filtro
documentos = coleccion.find(filtro)

# Mostrar los documentos obtenidos
print(f"\nDocumentos encontrados con {campo_filtro1} = {valor_filtro1} o {campo_filtro2} = {valor_filtro2}:")
for documento in documentos:
    print(f"\n{documento}")

#7 - Obtener todos los registros que no tengan valores nulos en un atributo dentro de una Colección (Debe existir atributos con valor a nulo)  (0.5 puntos)
print("\n- Apartado 7:")

# Solicitar al usuario el campo y el valor para el filtro
campo_filtro = input("Introduce el campo para el filtro (por ejemplo, nivel_contaminacion): ")

# Crear el filtro dinámico
filtro = {campo_filtro: {"$ne": None}}

# Obtener los documentos que cumplen con el filtro
documentos = coleccion.find(filtro)

# Mostrar los documentos encontrados
print(f"\nDocumentos encontrados donde {campo_filtro} no es igual a nulo")
for documento in documentos:
    print(f"\n{documento}")

#8 - Obtener todos los registros que no tengan un atributo en concreto dentro de una Colección (Debe existir registros que tengan no tengan ese atributo)  (0.5 puntos)
print("\n- Apartado 8:")

# Solicitar al usuario el campo para el filtro
campo_filtro = input("Introduce el campo para el filtro (por ejemplo, descripcion): ")

# Crear el filtro dinámico con $exists
filtro = {campo_filtro: {"$exists": False}}

# Obtener los documentos que cumplen con el filtro
documentos = coleccion.find(filtro)

# Mostrar los documentos encontrados
print(f"\nDocumentos que no tienen el atributo {campo_filtro}:")
for documento in documentos:
    print(f"\n{documento}")

#9 - Obtener todos los registros que tengan un valor que coincida con una lista de valores.  (0.5 puntos)
print("\n- Apartado 9:")

# Lista de valores
valores = ["baja", "media"]

# Definir el filtro
filtro = {"nivel_contaminacion": {"$in": valores}}

# Obtener los documentos que coinciden con el filtro
documentos = coleccion.find(filtro)

# Mostrar los documentos encontrados
print("\nDocumentos encontrados en los que el nivel de contaminacion es bajo o medio:")
for documento in documentos:
    print(f"\n{documento}")

#10 - Obtener todos los registros que tengan un atributo numérico y que su valor sea superior al especificado en el filtro.  (0.5 puntos)

print("\n- Apartado 10:")

# Definir el filtro para valores mayores que 50
filtro = {"area": {"$gt": 50}}

# Obtener los documentos que cumplen con el filtro
documentos = coleccion.find(filtro)

# Mostrar los documentos encontrados
print("\nDocumentos encontrados con área superior a 50:")
for documento in documentos:
   print(f"\n{documento}")

#11- Obtener todos los registros que cumpla una condición u otra (0.5 puntos)
print("\n- Apartado 11:")

# Definir el filtro para que sea mayor de 50 o que contenga quimicos en su descripcion
filtro = {
    "$or": [
        {"area": {"$gt": 50}},
        {"descripcion": "químicos"}
    ]
}

# Obtener los documentos que cumplen con alguna de las condiciones
documentos = coleccion.find(filtro)

# Mostrar los documentos encontrados
print("Documentos encontrados que cumplen con al menos una condición:")
for documento in documentos:
   print(f"\n{documento}")

#12 - Obtener todos los registros que no cumplan una condición en concreto (0.5 puntos)
print("\n- Apartado 12:")

# Definir el filtro para registros en los que el nivel de contaminacion no sea medio
filtro = {"nivel_contaminacion": {"$ne": "media"}}

# Obtener los documentos que cumplen con el filtro
documentos = coleccion.find(filtro)

# Mostrar los documentos encontrados
print("Documentos encontrados que no tienen nivel de contaminacion medio:")
for documento in documentos:
   print(f"\n{documento}")

#13 - Eliminar un registro de una Colección  (0.5 puntos)
print("\n- Apartado 13:")

# Definir el filtro para eliminar el documento
filtro = {"nombre": "Pacífico Sur"}

# Eliminar el primer documento que cumple con el filtro
resultado = coleccion.delete_one(filtro)

# Verificar si se eliminó un documento
if resultado.deleted_count > 0:
    print(f"\nDocumento con el filtro {filtro} eliminado correctamente.")
else:
    print(f"\nNo se encontró ningún documento con el filtro {filtro}.")

#14 - Eliminar varios registros de una Colección  (0.5 puntos)
print("\n- Apartado 14:")

# Definir el filtro para eliminar los documentos
filtro = {"nombre": "Pacífico"}

# Eliminar todos los documentos que cumplen con el filtro
resultado = coleccion.delete_many(filtro)

# Verificar cuantos documentos se eliminaron
if resultado.deleted_count == 1:
    print(f"\n{resultado.deleted_count} documento con el filtro {filtro} eliminado correctamente.")
elif resultado.deleted_count > 1:
    print(f"\n{resultado.deleted_count} documentos con el filtro {filtro} eliminado correctamente.")
else:
    print(f"\nNo se encontró ningún documento con el filtro {filtro}.")

#15 - Realiza una búsqueda y ordenala de forma ascedente.   (0.5 puntos)
print("\n- Apartado 15:")

# Realizar la búsqueda y ordenarla por el campo area en orden ascendente
documentos = coleccion.find().sort("area", 1)

# Mostrar los documentos encontrados
print("\nDocumentos encontrados ordenados por area ascendente:")
for documento in documentos:
   print(f"\n{documento}")

#16 - Realiza una búsqueda y ordenala de forma descendente.   (0.5 puntos)
print("\n- Apartado 16:")

# Realizar la búsqueda y ordenarla por el campo area en orden descendente
documentos = coleccion.find().sort("area", -1)

# Mostrar los documentos encontrados
print("\nDocumentos encontrados ordenados por area descendente:")
for documento in documentos:
   print(f"\n{documento}")

#17 - Realiza una búsqueda que este limitada por 10 registros.   (0.5 puntos)
print("\n- Apartado 17:")

# Realizar la búsqueda limitada a 10 documentos
documentos = coleccion.find().limit(10)

# Mostrar los documentos encontrados
print("\nDocumentos encontrados (limitados a 10):")
for documento in documentos:
   print(f"\n{documento}")

#18 - Realizar una operación que filtre por una expresión regular. (0.5 puntos)
print("\n- Apartado 18:")

# Definir el filtro para filtrar por nombres que empiecen por Mar
filtro = {"nombre": {"$regex": "^Mar"}}

# Obtener los documentos que cumplen con el filtro
documentos = coleccion.find(filtro)

# Mostrar los documentos encontrados
print("\nDocumentos encontrados cuyo nombre empieza por Mar:")
for documento in documentos:
   print(f"\n{documento}")

#19 - Realizar una operación que filtre con una operación de tipo Array (0.5 puntos)
print("\n- Apartado 19:")

# Lista de valores a buscar
valores = ["basura marina", "químicos"]

# Definir el filtro
filtro = {"tipo_contaminacion": {"$in": valores}}

# Obtener los documentos que cumplen con el filtro
documentos = coleccion.find(filtro)

# Mostrar los documentos encontrados
print("\nDocumentos encontrados con tipos de contaminacion que contienen plástico o químicos:")
for documento in documentos:
   print(f"\n{documento}")

#20 - Realizar una operación que filtre con una operación de tipo Evaluation, que no sea regex. (0.5 puntos)
print("\n- Apartado 20:")

# Usar $where con una expresión de evaluación para filtrar los documentos
filtro = {"area": {"$gt": 20}}

# Obtener los documentos que cumplen con el filtro
documentos = coleccion.find(filtro)

# Mostrar los documentos encontrados
print("\nDocumentos encontrados donde area es mayor que 20:")
for documento in documentos:
   print(f"\n{documento}")