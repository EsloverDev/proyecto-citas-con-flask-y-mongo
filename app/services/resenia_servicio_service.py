from app.models.resenia_servicio_model import ReseniaServicioModel
from app.models.servicio_model import ServicioModel

class ReseniaServicioService:
    
    def crear_resenia(self, resenia_data):
        if not ServicioModel.service_exists(resenia_data["id_servicio"]):
            raise ValueError("Servicio no encontrado")
        
        resenia_id = ReseniaServicioModel.create_resenia(resenia_data)
        return {
            "message": "Reseña creada exitosamente",
            "resenia_id": str(resenia_id)
        }
         
    def obtener_todas_resenias(self):
        resenias = ReseniaServicioModel.get_all_resenias()

        for resenia in resenias:
            resenia['_id'] = str(resenia['_id'])
            resenia['id_servicio'] = str(resenia['id_servicio'])

        return {
            "reseñas": resenias,
            "total": len(resenias),
            "message": "Reseñas obtenidas correctamente"
        }
        
    def obtener_resenia_por_id(self, resenia_id):        
        resenia = ReseniaServicioModel.get_resenia_by_id(resenia_id)
        if not resenia:
            raise ValueError("Reseña no encontrada")
        
        resenia['_id'] = str(resenia['_id'])
        resenia['id_servicio'] = str(resenia['id_servicio'])
        return resenia
        
    def obtener_resenia_por_servicio(self, servicio_id):        
        if not ServicioModel.service_exists(servicio_id):
            raise ValueError("Servicio no encontrado")
        
        resenias = ReseniaServicioModel.get_resenias_by_servicio(servicio_id)
        for resenia in resenias:
            resenia['_id'] = str(resenia['_id'])
            resenia['id_servicio'] = str(resenia['id_servicio'])

        return {
            "reseñas": resenias,
            "total": len(resenias),
            "servicio_id": servicio_id,
            "message": f"Reseñas del servicio {servicio_id}"
        }
        
    def obtener_promedio_servicio(self, servicio_id):
        if not ServicioModel.service_exists(servicio_id):
            raise ValueError("Servicio no encontrado")
        
        promedio_data = ReseniaServicioModel.get_promedio_calificacion_servicio(servicio_id)
        promedio_redondeado = round(promedio_data['promedio_calificacion'], 2) if promedio_data['promedio_calificacion'] else 0
        return {
            "servicio_id": servicio_id,
            "promedio_calificacion": promedio_redondeado,
            "total_resenias": promedio_data['total_resenias'],
            "message": f"Promedio de calificación del servicio {servicio_id}"
        }
        
    def actualizar_resenia(self, resenia_id, datos_actualizacion):        
        if not ReseniaServicioModel.resenia_exists(resenia_id):
            raise ValueError("Reseña no encontrada")
        
        resultado = ReseniaServicioModel.update_resenia(resenia_id, datos_actualizacion)
        if resultado.modified_count > 0:
            return {"message": "Reseña actualizada exitosamente"}
        else:
            return {"message": "No se realizaron cambios en la reseña"}
            
    def eliminar_resenia(self, resenia_id):        
        if not ReseniaServicioModel.resenia_exists(resenia_id):
            raise ValueError("Reseña no encontrada")
        
        resultado = ReseniaServicioModel.delete_resenia(resenia_id)
        if resultado.deleted_count > 0:
            return {"message": "Reseña eliminada exitosamente"}
        else:
            raise ValueError("No se pudo eliminar la reseña")
        
    def contar_resenias_servicio(self, servicio_id):        
        if not ServicioModel.service_exists(servicio_id):
            raise ValueError("Servicio no encontrado")
        
        cantidad = ReseniaServicioModel.count_resenias_by_servicio(servicio_id)
        return {
            "servicio_id": servicio_id,
            "total_resenias": cantidad,
            "message": f"El servicio tiene {cantidad} reseñas"
        }
        
    def verificar_resenia_existe(self, resenia_id):        
        existe = ReseniaServicioModel.resenia_exists(resenia_id)
        return {
            "resenia_id": resenia_id,
            "existe": existe,
            "message": "Reseña encontrada" if existe else "Reseña no encontrada"
        }