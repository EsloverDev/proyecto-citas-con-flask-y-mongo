from flask import jsonify, request
from bson.errors import InvalidId
from app.services.combo_servicio_service import ComboServicioService

class ComboServicioController:
    def __init__(self):
        self.service = ComboServicioService()

    def crear_combo(self):
        try:
            combo_data = request.get_json()

            if not combo_data:
                return jsonify({"error": "No se enviaron datos para crear el combo"}), 400
            
            combo = self.service.crearCombo(combo_data)
            return jsonify(combo), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def obtener_combos(self):
        try:
            combos = self.service.obtener_todos_combos()
            return jsonify(combos), 200
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500

    def buscar_combo(self, combo_id):
        try:
            combo = self.service.obtener_combo_por_id(combo_id)
            return jsonify(combo), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id de combo inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def buscar_combos_activos(self):
        try:
            combos = self.service.obtener_combos_activos()
            return jsonify(combos), 200
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def buscar_combos_por_servicio(self, servicio_id):
        try:
            combos = self.service.obtener_combos_por_servicio(servicio_id)
            return jsonify(combos), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id del servicio inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def modificar_combo(self, combo_id):
        try:
            datos_actualizacion = request.get_json()
            if not datos_actualizacion:
                return jsonify({"error": "No se enviaron datos para actualizar"}), 400
            
            combo_modificado = self.service.actualizar_combo(combo_id, datos_actualizacion)

            return jsonify(combo_modificado), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id del combo inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def agregar_servicio_combo(self, combo_id):
        try:
            servicio_data = request.get_json()

            if not servicio_data:
                return jsonify({"error": "No se enviaron datos del servicio"}), 400
            
            resultado = self.service.agregar_servicio_al_combo(combo_id, servicio_data)

            return jsonify(resultado), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id del combo o del servicio inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def eliminar_servicio_combo(self, combo_id, servicio_id):
        try:
            resultado = self.service.eliminar_servicio_del_combo(combo_id, servicio_id)
            return jsonify(resultado), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id de combo o de servicio inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def eliminar_combo(self, combo_id):
        try:
            combo_a_eliminar = self.service.eliminar_combo(combo_id)
            return jsonify(combo_a_eliminar), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id del combo inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def contar_combos(self):
        try:
            combos = self.service.contar_combos()
            return jsonify(combos), 200
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def verificar_combo(self, combo_id):
        try:
            combo = self.service.verificar_combo_existe(combo_id)
            return jsonify(combo), 200
        except InvalidId:
            return jsonify({"error": "Id del combo inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def buscar_combo_por_nombre(self):
        try:
            nombre = request.args.get('nombre')
            if not nombre:
                return jsonify({"error": "Se requiere el parámetro nombre en el query string"}), 400
            
            combo = self.service.buscar_combo_por_nombre(nombre)
            return jsonify(combo), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500

