from app.models.categoria_servicio_model import CategoriaServicioModel
from app.models.servicio_model import ServicioModel

class CategoriaServicioService:
    def crearCategoria(self, categoria_data):
        categoria_id = CategoriaServicioModel.create_categoria(categoria_data)
        return {
            "message": "Categoría creada",
            "id": str(categoria_id)
            }
    
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
        
    def actualizar_categoria(self, categoria_id, datos_actualizacion):
        if not CategoriaServicioModel.categoria_exists(categoria_id):
            raise ValueError("Categoria no encontrada")
        
        resultado = CategoriaServicioModel.update_categoria(categoria_id, datos_actualizacion)
        if resultado.modified_count > 0:
            return {"message": "Categoria actualizada", "categoria_id": categoria_id}
        else:
            return {"message": "No se realizaron cambios en la categoría"}
        
    def agregar_servicio(self, categoria_id, servicio_data):
        if not CategoriaServicioModel.categoria_exists(categoria_id):
            raise ValueError("Categoria no encontrada")
        
        if not ServicioModel.service_exists(servicio_data['id_servicio']):
            raise ValueError("Servicio no encontrado")
        
        if "nombre" not in servicio_data or "precio" not in servicio_data:
            servicio_completo = ServicioModel.get_service_by_id(servicio_data['id_servicio'])
            if servicio_completo:
                servicio_data['nombre'] = servicio_completo['nombre']
                servicio_data['precio'] = servicio_completo['precio']

        resultado = CategoriaServicioModel.add_servicio_to_categoria(categoria_id, servicio_data)
        if resultado.modified_count > 0:
            try:
                ServicioModel.update_service_categoria(servicio_data['id_servicio'], categoria_id)
            except Exception as e:
                print(f"Error actualizando el servicio: {e}")

            return {"message": "Servicio agregado a la categoría"}
        else:
            raise ValueError("No se pudo agregar el servicio a la categoría")
        
    def eliminar_servicio(self, categoria_id, servicio_id):
        if not CategoriaServicioModel.categoria_exists(categoria_id):
            raise ValueError("Categoria no encontrada")
        
        resultado = CategoriaServicioModel.remove_servicio_from_categoria(categoria_id, servicio_id)
        if resultado.modified_count > 0:
            try:
                ServicioModel.update_service_categoria(servicio_id, None)
            except Exception as e:
                print(f"Error actualizando servicio: {e}")
            
            return {"message": "Servicio eliminado de la categoría"}
        else:
            raise ValueError("No se pudo eliminar el servicio de la categoría")
        
    def eliminar_categoria(self, categoria_id):
        if not CategoriaServicioModel.categoria_exists(categoria_id):
            raise ValueError("Categoria no encontrada")
        
        categoria = CategoriaServicioModel.get_categoria_by_id(categoria_id)
        servicios_a_actualizar = []

        if categoria is not None and "servicios" in categoria:
            for servicio in categoria["servicios"]:
                id_servicio = servicio.get('id_servicio')
                if id_servicio:
                    servicios_a_actualizar.append(str(id_servicio))

        resultado = CategoriaServicioModel.delete_categoria(categoria_id)
        if resultado.deleted_count > 0:
            for servicio_id in servicios_a_actualizar:
                try:
                    ServicioModel.update_service_categoria(servicio_id, None)
                except Exception as e:
                    print(f"Error actualizando servicio {servicio_id}: {e}")
                    
            return {"message": "Categoria eliminada correctamente"}
        else:
            raise ValueError("No se pudo eliminar la categoría")