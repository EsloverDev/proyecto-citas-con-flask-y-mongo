from bson.objectid import ObjectId
from datetime import datetime
from app.extensions import mongo

class ComboServicioModel:
    @staticmethod
    def create_combo(data):
        required_fields = ["nombre", "descripcion", "precio_total", "servicios_incluidos"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Campo requerido faltante: {field}")
            
        if not isinstance(data["servicios_incluidos", list]) or len(data["servicios_incluidos"]) < 1:
            raise ValueError("El campo ´servicios_incluidos' debe ser un array con al menos un servicio")
        
        for servicio in data["servicios_incluidos"]:
            required_servicio_fields = ["id_servicio", "nombre"]
            for field in required_servicio_fields:
                if field not in servicio:
                    raise ValueError(f"Campo requerido en servicio: {field}")
                
            if not isinstance(servicio["id_servicio"], ObjectId):
                try:
                    servicio["id_servicio"] = ObjectId(servicio["id_servicio"])
                except:
                    raise ValueError(f"id_servicio inválido: {servicio['id_servicio']}")
                
            if not isinstance(data["precio_total"], (int, float)) or data["precio_total"] < 0:
                raise ValueError("precio_total debe ser un número positivo")
            
            if "promocion" in data and data["promocion"]:
                required_promocion_fields = ["porcentaje_descuento", "fecha_inicio", "fecha_fin"]

                for field in required_promocion_fields:
                    if field not in data["promocion"]:
                        raise ValueError(f"Campo requerido en promocion: {field}")
                    
                descuento = data["promocion"]["porcentaje_descuento"]
                if not isinstance(descuento, (int, float)) or descuento < 0 or descuento > 100:
                    raise ValueError("porcentaje_descuento debe ser un número entre 0 y 100")
                
                if not isinstance(data["promoción"]["fecha_inicio"], datetime):
                    raise ValueError("fecha_inicio debe ser una fecha válida")
                
                if not isinstance(data["promocion"]["fecha_fin"], datetime):
                    raise ValueError("fecha_fin debe ser una fecha válida")
                
        return mongo.db.combos_servicios.insert_one(data).inserted_id

    @staticmethod
    def get_combo_by_id(combo_id):
        return mongo.db.combos_servicios.find_one({"_id": ObjectId(combo_id)})

    @staticmethod
    def get_all_combos():
        return list(mongo.db.combos_servicios.find())

    @staticmethod
    def get_combos_activos():
        hoy = datetime.now()
        return list(mongo.db.combos_servicios.find(
            {
                "promocion.fecha_inicio": {"$lte": hoy},
                "promocion.fecha_fin": {"$gte": hoy}
        }
        ))
    
    @staticmethod
    def get_combos_por_servicio(servicio_id):
        return list(mongo.db.combos_servicios.find({
            "servicios_incluidos.id_servicio": ObjectId(servicio_id)
        }))

    @staticmethod
    def update_combo(combo_id, data):
        if "precio_total" in data:
            if not isinstance(data["precio_total"], (int, float)) or data["precio_total"] < 0:
                raise ValueError("precio total debe ser un número positivo")
            
        if "servicios_incluidos" in data:
            if not isinstance(data["servicios_incluidos"], list) or len(data["servicios_incluidos"]) < 1:
                raise ValueError("El campo 'servicios_incluidos' debe ser un array con al menos un servicio")
            
        return mongo.db.combos_servicios.update_one(
            {"_id": ObjectId(combo_id)},
            {"$set": data}
        )

    @staticmethod
    def add_servicio_a_combo(combo_id, servicio_data):
        required_fields = ["id_servicio", "nombre"]
        for field in required_fields:
            if field not in servicio_data:
                raise ValueError(f"Campo requerido en servicio: {field}")
            
        if not isinstance(servicio_data["id_servicio"], ObjectId):
            try:
                servicio_data["id_servicio"] = ObjectId(servicio_data["id_servicio"])
            except:
                raise ValueError("id_servicio inválido")
        
        return mongo.db.combos_servicios.update_one(
            {"id": ObjectId(combo_id)},
            {"$push": {"servicios_incluidos": servicio_data}}
        )
    
    @staticmethod
    def remove_servicio_de_combo(combo_id, servicio_id):
        if not isinstance(servicio_id, ObjectId):
            try:
                servicio_id = ObjectId(servicio_id)
            except:
                raise ValueError("servicio_id inválido")
            
        return mongo.db.combos_servicios.update_one(
            {"_id": ObjectId(combo_id)},
            {"$pull": {"servicios_incluidos": {"id_servicio": servicio_id}}}
        )

    @staticmethod
    def delete_combo(combo_id):
        return mongo.db.combos_servicios.delete_one({"_id": ObjectId(combo_id)})

    @staticmethod
    def combo_exists(combo_id):
        combo = mongo.db.combos_servicios.find_one({"_id": ObjectId(combo_id)})
        return combo is not None
    
    @staticmethod
    def count_combos():
        return mongo.db.combos_servicios.count_documents({})

    @staticmethod
    def get_combo_by_nombre(nombre):
        return mongo.db.combos_servicios.find_one({"nombre": nombre})