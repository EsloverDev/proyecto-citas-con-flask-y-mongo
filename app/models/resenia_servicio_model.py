from bson.objectid import ObjectId
from app.extensions import mongo

class ReseniaServicioModel:
    @staticmethod
    def create_resenia(data):
        return mongo.db.resenias_servicios.insert_one(data).inserted_id

    @staticmethod
    def get_resenia_by_id(resenia_id):
        return mongo.db.resenias_servicios.find_one({"_id": ObjectId(resenia_id)})

    @staticmethod
    def get_all_resenias():
        return list(mongo.db.resenias_servicios.find())

    @staticmethod
    def update_resenia(resenia_id, data):
        return mongo.db.resenias_servicios.update_one(
            {"_id": ObjectId(resenia_id)}, {"$set": data}
        )

    @staticmethod
    def delete_resenia(resenia_id):
        return mongo.db.resenias_servicios.delete_one({"_id": ObjectId(resenia_id)})

    @staticmethod
    def get_resenias_by_servicio(id_servicio):
        return list(mongo.db.resenias_servicios.find({"id_servicio": ObjectId(id_servicio)}))
