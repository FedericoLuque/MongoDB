from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()

baseDatos = cliente["oceanos"]

coleccion = baseDatos["zonas"]

documento = {"nombre":"pacifico", "ubicacion":"hawai","descripcion":"Concentracion de residuos plasticos", "nivel_contaminacion":"media","tipo_contaminacion":"plasticos","area":50,"biodiversidad":"delfines" }
