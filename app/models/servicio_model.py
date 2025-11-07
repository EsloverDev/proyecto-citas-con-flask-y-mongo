from bson.objectid import ObjectId
from app.extensions import mongo

class ServicioModel:

    @staticmethod
    def create_service(data):
        required_fields = ["nombre", "precio", "detalle", "imagen"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Campo requerido faltante: {field}")
            
        if "descripcion" not in data["detalle"]:
            raise ValueError("El detalle debe contener descripción")
        
        for img in data["imagen"]:
            if "url" not in img:
                raise ValueError("Cada imagen debe tener URL")
            
        if "categoria_id" in data and data["categoria_id"]:
            if not isinstance(data["categoria_id"], ObjectId):
                try:
                    data["categoria_id"] = ObjectId(data["categoria_id"])
                except:
                    raise ValueError("categoria_id inválido")
                
        return mongo.db.servicios.insert_one(data).inserted_id

    @staticmethod
    def get_service_by_id(service_id):
        return mongo.db.servicios.find_one({"_id": ObjectId(service_id)})

    @staticmethod
    def get_all_services():
        return list(mongo.db.servicios.find())
    
    @staticmethod
    def get_services_by_categoria(categoria_id):
        return list(mongo.db.servicios.find({"categoria_id": ObjectId(categoria_id)}))
    
    @staticmethod
    def get_services_sin_categoria():
        return list(mongo.db.servicios.find({
            "$or": [
                {"categoria_id": {"$exists": False}},
                {"categoria_id": {"$in": [None, ""]}}
            ]
        }))

    @staticmethod
    def update_service(service_id, data):
        if "categoria_id" in data and data["categoria_id"]:
            if not isinstance(data["categoria_id"], ObjectId):
                try:
                    data["categoria_id"] = ObjectId(data["categoria_id"])
                except:
                    raise ValueError("categoria_id inválido")
                
        return mongo.db.servicios.update_one(
            {"_id": ObjectId(service_id)},
            {"$set": data}
        )
    
    @staticmethod
    def update_service_categoria(service_id, categoria_id):
        if not isinstance(service_id, ObjectId):
            try:
                service_id = ObjectId(service_id)
            except:
                raise ValueError("service_id inválido")

        if categoria_id:
            if not isinstance(categoria_id, ObjectId):
                try:
                    categoria_id = ObjectId(categoria_id)
                except:
                    raise ValueError("categoria_id inválido")
            
            return mongo.db.servicios.update_one(
                {"_id": service_id},
                {"$set": {"categoria_id": categoria_id}})

        else:
            return mongo.db.servicios.update_one(
                {"_id": service_id},
                {"$unset": {"categoria_id": ""}})



    @staticmethod
    def delete_service(service_id):
        return mongo.db.servicios.delete_one({"_id": ObjectId(service_id)})
    
    @staticmethod
    def service_exists(service_id):
        servicio = mongo.db.servicios.find_one({"_id": ObjectId(service_id)})
        return servicio is not None
    
    @staticmethod
    def count_services_by_categoria(categoria_id):
        if not isinstance(categoria_id, ObjectId):
            try:
                categoria_id = ObjectId(categoria_id)
            except:
                raise ValueError("categoria_id inválido")
        return mongo.db.servicios.count_documents({"categoria_id": categoria_id})
