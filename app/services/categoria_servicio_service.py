from app.models.categoria_servicio_model import CategoriaServicioModel
from bson.objectid import ObjectId

class CategoriaServicioService:
    
    def crearCategoria(self):
        nueva_categoria = {
            "nombre": "Cortes de cabello",
            "descripcion": "Servicios profesionales de corte y estilo",
            "servicios": [
                {
                    "id_servicio": ObjectId(),
                    "nombre": "Corte Básico",
                    "precio": 15000
                },
                {
                    "id_servicio": ObjectId(),
                    "nombre": "Corte con shaver",
                    "precio": 26000
                }
            ]
        }

        inserted_id = CategoriaServicioModel.create_categoria(nueva_categoria)
        return {"message": "Categoría de ejemplo creada", "id": str(inserted_id)}
    
    def obtener_todas_categorias(self):
        categorias = CategoriaServicioModel.get_all_categorias()

        for categoria in categorias:
            categoria['_id'] = str(categoria['_id'])
            for servicio in categoria['servicios']:
                servicio['id_servicio'] = str(servicio['id_servicio'])

        return {
            "categorias": categorias,
            "total": len(categorias),
            "message": "Categorias obtenidas correctamente"
        }
    
    def obtener_categoria_por_id(self, categoria_id):
        categoria = CategoriaServicioModel.get_categoria_by_id(categoria_id)

        if categoria:
            categoria['_id'] = str(categoria['_id'])
            for servicio in categoria['servicios']:
                servicio['id_servicio'] = str(servicio['id_servicio'])
            return categoria
        else:
            raise ValueError("Categoria no encontrada")
        
    def actualizar_categoria(self, categoria_id):
        datos_actualizacion = {
            "descripcion": "servicios premium de corte y estilo",
            "servicios": [
                {
                    "id_servicio": ObjectId(),
                    "nombre": "Corte tradicional",
                    "precio": 18000
                }
            ]
        }

        resultado = CategoriaServicioModel.update_categoria(categoria_id, datos_actualizacion)

        if resultado.modified_count > 0:
            return {"message": "Categoria actualizada", "categoria_id": categoria_id}
        else:
            return {"message": "No se realizaron cambios en la categoría"}
        
    def agregar_servicio(self, categoria_id):
        nuevo_servicio = {
            "id_servicio": ObjectId(),
            "nombre": "Corte con tijera",
            "precio": 28000
        }

        resultado = CategoriaServicioModel.add_servicio_to_categoria(categoria_id, nuevo_servicio)

        if resultado.modified_count > 0:
            return {"message": "Servicio agregado a la categoría"}
        else:
            raise ValueError("No se pudo agregar el servicio a la categoría")
        
    def eliminar_servicio(self, categoria_id, servicio_id):
        resultado = CategoriaServicioModel.remove_servicio_from_categoria(categoria_id, servicio_id)

        if resultado.modified_count > 0:
            return {"message": "Servicio eliminado de la categoría"}
        else:
            raise ValueError("No se pudo eliminar el servicio de la categoría")
        
    def eliminar_categoria(self, categoria_id):
        resultado = CategoriaServicioModel.delete_categoria(categoria_id)

        if resultado.deleted_count > 0:
            return {"message": "Categoria eliminada correctamente"}
        else:
            raise ValueError("No se pudo eliminar la categoría")