from flask import jsonify, request
from bson.errors import InvalidId
from app.services.servicio_service import ServicioService

class ServicioController:
    def __init__(self):
        self.service = ServicioService()

    def insertar_servicio(self):
        try:
            servicio_data = request.get_json()
            if not servicio_data:
                return jsonify({"error": "No se enviaron datos para crear el servicio"}), 400

            servicio = self.service.crear_servicio(servicio_data)
            return jsonify(servicio), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except InvalidId:
            return jsonify({"error": "Id de categoría inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def obtener_servicios(self):
        try:
            servicios = self.service.obtener_todos_servicios()
            return jsonify(servicios), 200
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def buscar_servicio(self, servicio_id):
        try:
            servicio = self.service.obtener_servicio_por_id(servicio_id)
            return jsonify(servicio), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id de servicio inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def buscar_servicios_por_categoria(self, categoria_id):
        try:
            servicios = self.service.obtener_servicios_por_categoria(categoria_id)
            return jsonify(servicios), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id de categoría inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def buscar_servicios_sin_categoria(self):
        try:
            servicios = self.service.obtener_servicios_sin_categoria()
            return jsonify(servicios), 200
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500

    def modificar_servicio(self, servicio_id):
        try:
            datos_actualizacion = request.get_json()
            if not datos_actualizacion:
                return jsonify({"error": "No se enviaron datos para actualizar"}), 400
            
            servicio_modificado = self.service.actualizar_servicio(servicio_id, datos_actualizacion)
            return jsonify(servicio_modificado), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id de servicio o de la categoría inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500

    def modificar_categoria_servicio(self, servicio_id):
        try:
            nueva_categoria_id = request.args.get('nueva_categoria_id')
            if nueva_categoria_id in ["null", "", "None"]:
                nueva_categoria_id = None

            servicio_nueva_categoria = self.service.actualizar_categoria_servicio(servicio_id, nueva_categoria_id)
            return jsonify(servicio_nueva_categoria), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id de servicio o categoría inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def eliminar_servicio(self, servicio_id):
        try:
            servicio_eliminado = self.service.eliminar_servicio(servicio_id)
            return jsonify(servicio_eliminado), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id de servicio inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def contar_servicios_categoria(self, categoria_id):
        try:
            total_servicios_categoria = self.service.contar_servicios_por_categoria(categoria_id)
            return jsonify(total_servicios_categoria), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id de la categoría inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500

    def verificar_servicio(self, servicio_id):
        try:
            servicio = self.service.verificar_servicio_existe(servicio_id)
            return jsonify(servicio), 200
        except InvalidId:
            return jsonify({"error": "Id del servicio inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500