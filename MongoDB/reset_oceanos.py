from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()

baseDatos = cliente["oceanos"]

coleccion = baseDatos["zonas"]

# Eliminar todos los documentos de la colección
resultado = coleccion.delete_many({})

# Mostrar el número de documentos eliminados
print(f"Documentos eliminados: {resultado.deleted_count}")