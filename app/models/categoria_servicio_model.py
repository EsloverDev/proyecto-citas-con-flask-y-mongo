from bson.objectid import ObjectId
from app.extensions import mongo

class CategoriaServicioModel:

    @staticmethod
    def create_categoria(data):
        required_fields = ["nombre", "descripcion"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Campo requerido faltante: {field}")
            
        if "servicios" not in data:
            data["servicios"] = []
        else:
            if not isinstance(data["servicios"], list) or len(data["servicios"]) < 1:
                raise ValueError("El campo 'servicios' debe ser un array con al menos un elemento")
        
            for servicio in data["servicios"]:
                required_servicio_fields = ["id_servicio"]
                for field in required_servicio_fields:
                    if field not in servicio:
                        raise ValueError(f"Campo requerido en servicio: {field}")
                
                if not isinstance(servicio["id_servicio"], ObjectId):
                    try:
                        servicio["id_servicio"] = ObjectId(servicio["id_servicio"])
                    except:
                        raise ValueError(f"id_servicio inválido: {servicio['id_servicio']}")
                
                if not isinstance(servicio["precio"], (int, float)) or servicio["precio"] < 0:
                    raise ValueError(f"Precio debe ser número positivo: {servicio['precio']}")
        
        return mongo.db.categorias_servicios.insert_one(data).inserted_id

    @staticmethod
    def get_all_categorias():
        return list(mongo.db.categorias_servicios.find())

    @staticmethod
    def get_categoria_by_id(categoria_id):
        return mongo.db.categorias_servicios.find_one({"_id": ObjectId(categoria_id)})

    @staticmethod
    def update_categoria(categoria_id, data):
        return mongo.db.categorias_servicios.update_one(
            {"_id": ObjectId(categoria_id)},
            {"$set": data}
        )

    @staticmethod
    def delete_categoria(categoria_id):
        return mongo.db.categorias_servicios.delete_one({"_id": ObjectId(categoria_id)})

    @staticmethod
    def add_servicio_to_categoria(categoria_id, servicio):
        required_servicio_fields = ["id_servicio", "nombre", "precio"]
        for field in required_servicio_fields:
            if field not in servicio:
                raise ValueError(f"Campo requerido en servicio: {field}")
            
        if not isinstance(servicio["id_servicio"], ObjectId):
            try:
                servicio["id_servicio"] = ObjectId(servicio["id_servicio"])
            except:
                raise ValueError(f"id_servicio inválido: {servicio['id_servicio']}")
            
        if not isinstance(servicio["precio"], (int, float)) or servicio["precio"] < 0:
            raise ValueError(f"Precio debe ser un número positivo: {servicio['precio']}")

        return mongo.db.categorias_servicios.update_one(
            {"_id": ObjectId(categoria_id)},
            {"$push": {"servicios": servicio}}
        )

    @staticmethod
    def remove_servicio_from_categoria(categoria_id, id_servicio):
        if not isinstance(id_servicio, ObjectId):
            try:
                id_servicio = ObjectId(id_servicio)
            except:
                raise ValueError(f"id_servicio inválido: {id_servicio}")

        return mongo.db.categorias_servicios.update_one(
            {"_id": ObjectId(categoria_id)},
            {"$pull": {"servicios": {"id_servicio": id_servicio}}}
        )
