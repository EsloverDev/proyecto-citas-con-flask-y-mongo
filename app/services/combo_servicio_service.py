from app.models.combo_servicio_model import ComboServicioModel
from app.models.servicio_model import ServicioModel

class ComboServicioService:
    
    def crearCombo(self, combo_data):
        combo_id = ComboServicioModel.create_combo(combo_data)
        return {
            "message": "Combo creado exitosamente",
            "combo_id": str(combo_id)
        }
    
    def obtener_todos_combos(self):
        combos = ComboServicioModel.get_all_combos()
        for combo in combos:
            combo['_id'] = str(combo['_id'])
            for servicio in combo.get('servicios_incluidos', []):
                servicio['id_servicio'] = str(servicio['id_servicio'])

        return {
            "combos": combos,
            "total": len(combos),
            "message": "Combos obtenidos correctamente"
        }
    
    def obtener_combo_por_id(self, combo_id):
        combo = ComboServicioModel.get_combo_by_id(combo_id)

        if not combo:
            raise ValueError("Combo no encontrado")
        
        combo['_id'] = str(combo['_id'])
        for servicio in combo.get('servicios_incluidos', []):
            servicio['id_servicio'] = str(servicio['id_servicio'])

        return combo
    
    def obtener_combos_activos(self):
        combos = ComboServicioModel.get_combos_activos()

        for combo in combos:
            combo['_id'] = str(combo['_id'])
            for servicio in combo.get('servicios_incluidos', []):
                servicio['id_servicio'] = str(servicio['id_servicio'])

        return {
            "combos": combos,
            "total": len(combos),
            "message": "Combos con promociones activas"
        }
    
    def obtener_combos_por_servicio(self, servicio_id):
        if not ServicioModel.service_exists(servicio_id):
            raise ValueError("Servicio no encontrado")
        
        combos = ComboServicioModel.get_combos_por_servicio(servicio_id)

        for combo in combos:
            combo['_id'] = str(combo['_id'])
            for servicio in combo.get('servicios_incluidos', []):
                servicio['id_servicio'] = str(servicio['id_servicio'])

        return {
            "combos": combos,
            "total": len(combos),
            "servicio_id": servicio_id,
            "message": f"Combos que contienen el servicio {servicio_id}"
        }
    
    def actualizar_combo(self, combo_id, datos_actualizacion):
        if not ComboServicioModel.combo_exists(combo_id):
            raise ValueError("Combo no encontrado")
        
        combo_actualizado = ComboServicioModel.update_combo(combo_id, datos_actualizacion)

        if combo_actualizado.modified_count > 0:
            return {"message": "Combo actualizado exitosamente"}
        else:
            return {"message": "No se realizaron cambios en el combo"}
        
    def agregar_servicio_al_combo(self, combo_id, servicio_data):
        
        if not ComboServicioModel.combo_exists(combo_id):
            raise ValueError("Combo no encontrado")
        
        if not ServicioModel.service_exists(servicio_data['id_servicio']):
            raise ValueError("Servicio no encontrado")
        
        servicio_agregado = ComboServicioModel.add_servicio_a_combo(combo_id, servicio_data)

        if servicio_agregado.modified_count > 0:
            return {"message": "Servicio agregado al combo exitosamente"}
        else:
            raise ValueError("No se pudo agregar el servicio al combo")
        
    def eliminar_servicio_del_combo(self, combo_id, servicio_id):
        if not ComboServicioModel.combo_exists(combo_id):
            raise ValueError("Combo no encontrado")
        
        servicio_removido = ComboServicioModel.remove_servicio_de_combo(combo_id, servicio_id)

        if servicio_removido.modified_count > 0:
            return {"message": "Servicio eliminado del combo exitosamente"}
        else:
            raise ValueError("No se pudo eliminar el servicio del combo")
        
    def eliminar_combo(self, combo_id):
        if not ComboServicioModel.combo_exists(combo_id):
            raise ValueError("Combo no encontrado")
        
        combo_eliminado = ComboServicioModel.delete_combo(combo_id)

        if combo_eliminado.deleted_count > 0:
            return {"message": "Combo eliminado exitosamente"}
        else:
            raise ValueError("No se pudo eliminar el combo")
        
    def contar_combos(self):
        total_combos = ComboServicioModel.count_combos()

        return {
            "total_combos": total_combos,
            "message": f"Existen {total_combos} combos en el sistema"
        }
    
    def verificar_combo_existe(self, combo_id):
        existe = ComboServicioModel.combo_exists(combo_id)

        return {
            "combo_id": combo_id,
            "existe": existe,
            "message": "combo encontrado" if existe else "Combo no encontrado"
        }
    
    def buscar_combo_por_nombre(self, nombre):
        combo = ComboServicioModel.get_combo_by_nombre(nombre)

        if not combo:
            raise ValueError(f"No se encontró ningún combo con el nombre '{nombre}'")
        
        combo['_id'] = str(combo['_id'])
        
        for servicio in combo.get('servicios_incluidos', []):
            servicio['id_servicio'] = str(servicio['id_servicio'])

        return combo