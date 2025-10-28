from bson.objectid import ObjectId
from datetime import datetime
from app.extensions import mongo

class ReseniaServicioModel:
    @staticmethod
    def create_resenia(data):
        required_fields = ["id_servicio", "cliente"]

        for field in required_fields:
            if field not in data:
                raise ValueError(f"El campo {field} es requerido")
            
        if "cliente" in data:
            required_cliente_fields = ["nombre", "comentario", "calificacion"]

            for field in required_cliente_fields:
                if field not in data["cliente"]:
                    raise ValueError(f"El campo {field} es requerido")

            calificacion = data["cliente"]["calificacion"]
            if not isinstance(calificacion, (int, float)) or calificacion < 1 or calificacion > 5:
                raise ValueError("La calificación debe ser un número entre 1 y 5")
            
            if len(data["cliente"]["nombre"]) > 50:
                raise ValueError("El nombre del cliente no puede exceder 50 caracteres")
            
            if len(data["cliente"]["comentario"]) > 300:
                raise ValueError("El comentario no puede exceder los 300 caracteres")
            
        if not isinstance(data["id_servicio"], ObjectId):
            try:
                data["id_servicio"] = ObjectId(data["id_servicio"])
            except:
                raise ValueError("Id del servicio inválido")
            
        data["fecha"] = datetime.now()
            
        return mongo.db.resenias_servicios.insert_one(data).inserted_id

    @staticmethod
    def get_resenia_by_id(resenia_id):
        return mongo.db.resenias_servicios.find_one({"_id": ObjectId(resenia_id)})

    @staticmethod
    def get_all_resenias():
        return list(mongo.db.resenias_servicios.find())

    @staticmethod
    def update_resenia(resenia_id, data):
        if "cliente" in data:
            if "calificacion" in data["cliente"]:
                calificacion = data["cliente"]["calificacion"]
                if not isinstance(calificacion, (int, float)) or calificacion < 1 or calificacion > 5:
                    raise ValueError("La calificacion debe ser un número entre 1 y 5")
                
            if "nombre" in data["cliente"] and len(data["cliente"]["nombre"]) > 50:
                raise ValueError("El nombre del cliente no puede exceder los 50 caracteres")
            
            if "comentario" in data["cliente"] and len(data["cliente"]["comentario"]) > 300:
                raise ValueError("El comentario no puede exceder los 300 caracteres")

        return mongo.db.resenias_servicios.update_one(
            {"_id": ObjectId(resenia_id)}, {"$set": data}
        )

    @staticmethod
    def delete_resenia(resenia_id):
        return mongo.db.resenias_servicios.delete_one({"_id": ObjectId(resenia_id)})

    @staticmethod
    def get_resenias_by_servicio(id_servicio):
        if not isinstance(id_servicio, ObjectId):
            try:
                id_servicio = ObjectId(id_servicio)
            except:
                raise ValueError("Id del servicio inválido")
        return list(mongo.db.resenias_servicios.find({"id_servicio": id_servicio}))

    @staticmethod
    def get_promedio_calificacion_servicio(id_servicio):
        if not isinstance(id_servicio, ObjectId):
            try:
                id_servicio = ObjectId(id_servicio)
            except:
                raise ValueError("Id del servicio inválido")
            
        agregacion = [
            {"$match": {"id_servicio": id_servicio}},
            {"$group": {
                "_id": "$id_servicio",
                "promedio_calificacion": {"$avg": "$cliente.calificacion"},
                "total_resenias": {"$sum": 1}
            }}
        ]

        resultado = list(mongo.db.resenias_servicios.aggregate(agregacion))

        return resultado[0] if resultado else {"promedio_calificacion": 0, "total_resenias": 0}
    
    @staticmethod
    def resenia_exists(resenia_id):
        resenia = mongo.db.resenias_servicios.find_one({"_id": ObjectId(resenia_id)})
        return resenia is not None
    
    @staticmethod
    def count_resenias_by_servicio(id_servicio):
        if not isinstance(id_servicio, ObjectId):
            try:
                id_servicio = ObjectId(id_servicio)
            except:
                raise ValueError("Id del servicio inválido")
            
        return mongo.db.resenias_servicios.count_documents({"id_servicio": id_servicio})