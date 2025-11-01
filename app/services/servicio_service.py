from app.models.servicio_model import ServicioModel
from app.models.categoria_servicio_model import CategoriaServicioModel
from bson.objectid import ObjectId

class ServicioService:

    def crear_servicio(self, servicio_data):
        if "categoria_id" in servicio_data and servicio_data['categoria_id']:
            if not CategoriaServicioModel.categoria_exists(servicio_data['categoria_id']):
                raise ValueError("Categoría no encontrada")

        servicio_id = ServicioModel.create_service(servicio_data)
        if "categoria_id" in servicio_data and servicio_data["categoria_id"]:
            servicio_para_categoria = {
                "id_servicio": servicio_id,
                "nombre": servicio_data["nombre"],
                "precio": servicio_data["precio"]
            }

            CategoriaServicioModel.add_servicio_to_categoria(servicio_data["categoria_id"], servicio_para_categoria)

        return {
            "message": "Servicio insertado" + (" con categoria" if servicio_data['categoria_id'] else " sin categoria"),
            "servicio_id": str(servicio_id),
            "categoria_id": str(servicio_data['categoria_id']) if servicio_data['categoria_id'] else None
            }
    
    def obtener_todos_servicios(self):
        servicios = ServicioModel.get_all_services()

        for servicio in servicios:
            servicio['_id'] = str(servicio['_id'])
            if 'categoria_id' in servicio and servicio['categoria_id']:
                servicio['categoria_id'] = str(servicio['categoria_id'])

        return {
            "Servicios": servicios,
            "total": len(servicios),
            "message": "Servicios obtenidos correctamente"
            }
    
    def obtener_servicio_por_id(self, servicio_id):
        servicio = ServicioModel.get_service_by_id(servicio_id)
        
        if servicio:
            servicio['_id'] = str(servicio['_id'])
            if 'categoria_id' in servicio and servicio['categoria_id']:
                servicio['categoria_id'] = str(servicio['categoria_id'])
            return servicio
        else:
            raise ValueError("Servicio no encontrado")
        
    def obtener_servicios_por_categoria(self, categoria_id):
        if not CategoriaServicioModel.categoria_exists(categoria_id):
            raise ValueError("Categoría no encontrada")
        
        servicios = ServicioModel.get_services_by_categoria(categoria_id)
        for servicio in servicios:
            servicio['_id'] = str(servicio['_id'])
            servicio['categoria_id'] = str(servicio['categoria_id'])

        return {
            "servicios": servicios,
            "total": len(servicios),
            "categoria_id": categoria_id,
            "message": f"Servicios de la categoría {categoria_id}"
        }
    
    def obtener_servicios_sin_categoria(self):
        servicios = ServicioModel.get_services_sin_categoria()
        for servicio in servicios:
            servicio['_id'] = str(servicio['_id'])

        return {
            "servicios": servicios,
            "total": len(servicios),
            "message": "Servicios sin categoría asignada"
        }

    def actualizar_servicio(self, servicio_id, datos_actualizacion):
        if not ServicioModel.service_exists(servicio_id):
            raise ValueError("Servicio no encontrado")
        
        if "categoria_id" in datos_actualizacion and datos_actualizacion["categoria_id"]:
            if not CategoriaServicioModel.categoria_exists(datos_actualizacion["categoria_id"]):
                raise ValueError("Categoría no encontrada")
            
        resultado = ServicioModel.update_service(servicio_id, datos_actualizacion)
        if resultado.modified_count > 0:
            return {"message": "Servicio actualizado"}
        else:
            return {"message": "No se realizaron cambios en el servicio"}
    
    def actualizar_categoria_servicio(self, servicio_id, nueva_categoria_id=None):
        servicio = ServicioModel.get_service_by_id(servicio_id)
        if not servicio:
            raise ValueError("Servicio no encontrado")
        
        if nueva_categoria_id and not CategoriaServicioModel.get_categoria_by_id(nueva_categoria_id):
            raise ValueError("Categoría no encontrada")
        
        categoria_anterior = servicio.get('categoria_id')
        if categoria_anterior:
            CategoriaServicioModel.remove_servicio_from_categoria(str(categoria_anterior), servicio_id)

        resultado = ServicioModel.update_service_categoria(servicio_id, nueva_categoria_id)

        if nueva_categoria_id:
            servicio_para_categoria = {
                "id_servicio": ObjectId(servicio_id),
                "nombre": servicio['nombre'],
                "precio": servicio['precio']
            }

            CategoriaServicioModel.add_servicio_to_categoria(nueva_categoria_id, servicio_para_categoria)

        mensaje = "Categoría del servicio actualizada" if nueva_categoria_id else "Servicio removido de categoría"
        return {
            "message": mensaje,
            "servicio_id": servicio_id,
            "categoria_anterior": str(categoria_anterior) if categoria_anterior else None,
            "categoria_nueva": str(nueva_categoria_id) if nueva_categoria_id else None
        }

    def eliminar_servicio(self, servicio_id):
        servicio = ServicioModel.get_service_by_id(servicio_id)
        if not servicio:
            raise ValueError("Servicio no encontrado")
        
        if servicio.get('categoria_id'):
            CategoriaServicioModel.remove_servicio_from_categoria(str(servicio['categoria_id']), servicio_id)
        
        resultado = ServicioModel.delete_service(servicio_id)
        if resultado.deleted_count > 0:
            return {"message": "Servicio eliminado correctamente"}
        else:
            raise ValueError("No se pudo eliminar el servicio")
        
    def contar_servicios_por_categoria(self, categoria_id):
        if not CategoriaServicioModel.categoria_exists(categoria_id):
            raise ValueError("Categoria no encontrada")
        
        cantidad = ServicioModel.count_services_by_categoria(categoria_id)
        return {
            "categoria_id": categoria_id,
            "total_servicios": cantidad,
            "message": f"La categoría tiene {cantidad} servicios"
        }
    
    def verificar_servicio_existe(self, servicio_id):
        existe = ServicioModel.service_exists(servicio_id)
        return {
            "servicio_id": servicio_id,
            "existe": existe,
            "message": "Servicio encontrado" if existe else "Servicio no encontrado"
        }