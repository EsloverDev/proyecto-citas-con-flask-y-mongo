from bson.objectid import ObjectId
from app.extensions import mongo

class ComboServicioModel:
    @staticmethod
    def create_combo(data):
        return mongo.db.combos_servicios.insert_one(data).inserted_id

    @staticmethod
    def get_combo_by_id(combo_id):
        return mongo.db.combos_servicios.find_one({"_id": ObjectId(combo_id)})

    @staticmethod
    def get_all_combos():
        return list(mongo.db.combos_servicios.find())

    @staticmethod
    def update_combo(combo_id, data):
        return mongo.db.combos_servicios.update_one(
            {"_id": ObjectId(combo_id)}, {"$set": data}
        )

    @staticmethod
    def delete_combo(combo_id):
        return mongo.db.combos_servicios.delete_one({"_id": ObjectId(combo_id)})

    @staticmethod
    def get_combo_by_nombre(nombre):
        return mongo.db.combos_servicios.find_one({"nombre": nombre})
