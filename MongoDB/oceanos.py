from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()

baseDatos = cliente["oceanos"]

coleccion = baseDatos["zonas"]

#1 - Inserta un registro en una Colección (0.5 puntos)

#Crear un documento
documento = {"nombre":"Pacífico", "ubicacion":"hawai","descripcion":"Concentracion de residuos plasticos", "nivel_contaminacion":"media","tipo_contaminacion":"plasticos","area":50,"biodiversidad":"delfines" }

# Insertar el documento en la colección
resultado = coleccion.insert_one(documento)

# Mostrar el ID del documento insertado
print("Documento insertado con ID:", resultado.inserted_id)

#2 - Insertar varios registros en una Coleccion  (0.5 puntos)

#Crear varios documentos
documentos = [
    {
        "nombre": "Atlántico Norte",
        "ubicacion": "Caribe",
        "descripcion": "Derrame de petróleo en zona costera",
        "nivel_contaminacion": "alta",
        "tipo_contaminacion": "petróleo",
        "area": 120,
        "biodiversidad": "tiburones"
    },
    {
        "nombre": "Mar Mediterráneo",
        "ubicacion": "Europa",
        "descripcion": "Incremento de microplásticos",
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
        "biodiversidad": "corales"
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
print("Documentos insertados con IDs:", resultado.inserted_ids)

#3 - Actualizar un registro de una Colección  (0.5 puntos)

# Criterio para seleccionar el documento a actualizar
filtro = {"nombre": "Pacífico"}

# Cambios que quieres realizar
actualizacion = {"$set": {"nivel_contaminacion": "alta", "descripcion": "Zona en estado crítico"}}

# Actualizar un documento
resultado = coleccion.update_one(filtro, actualizacion)

print(f"Documentos encontrados: {resultado.matched_count}")
print(f"Documentos modificados: {resultado.modified_count}")

#4 - Actualizar varios registros en una Colección  (0.5 puntos)

# Criterio para seleccionar los documentos a actualizar
filtro = {"area": 90}

# Cambios que quieres realizar
actualizacion = {"$set": {"area": 85}}

# Actualizar múltiples documentos
resultado = coleccion.update_many(filtro, actualizacion)

# Mostrar el resultado
print(f"Documentos encontrados: {resultado.matched_count}")
print(f"Documentos modificados: {resultado.modified_count}")

#5 - Obtener varios registros por un filtro de un atributo dentro de una Colección  (0.5 puntos)

# Definir el filtro
filtro = {"nivel_contaminacion": "alta"}

# Obtener los documentos que coinciden con el filtro
documentos = coleccion.find(filtro)

# Mostrar los documentos obtenidos
print("Documentos encontrados:")
for documento in documentos:
    print(documento)

#6 - Obtener varios registros por un filtro por varios atributos dentro de una Colección  (0.5 puntos)