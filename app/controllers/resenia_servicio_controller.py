from flask import jsonify, request
from bson.errors import InvalidId
from app.services.resenia_servicio_service import ReseniaServicioService

class ReseniaServicioController:
    def __init__(self):
        self.service = ReseniaServicioService()

    def crear_resenia(self):
        try:
            resenia_data = request.get_json()
            if not resenia_data:
                return jsonify({"error": "No se enviaron datos para crear la reseña"}), 400
            
            resenia = self.service.crear_resenia(resenia_data)
            return jsonify(resenia), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id del servicio es inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def obtener_resenias(self):
        try:
            resultado = self.service.obtener_todas_resenias()
            return jsonify(resultado), 200
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def buscar_resenia(self, resenia_id):
        try:
            resenia = self.service.obtener_resenia_por_id(resenia_id)
            return jsonify(resenia), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id de la reseña inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def buscar_resenias_por_servicio(self, servicio_id):
        try:
            resultado = self.service.obtener_resenia_por_servicio(servicio_id)
            return jsonify(resultado), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id del servicio inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def obtener_promedio_servicio(self, servicio_id):
        try:
            resultado = self.service.obtener_promedio_servicio(servicio_id)
            return jsonify(resultado), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id del servicio inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def actualizar_resenia(self, resenia_id):
        try:
            datos_actualizacion = request.get_json()
            if not datos_actualizacion:
                return jsonify({"error": "No se enviaron datos para actualizar"}), 400
            
            resultado = self.service.actualizar_resenia(resenia_id, datos_actualizacion)
            return jsonify(resultado), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id de la reseña inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def eliminar_resenia(self, resenia_id):
        try:
            resultado = self.service.eliminar_resenia(resenia_id)
            return jsonify(resultado), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id de reseña inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def contar_resenias_servicio(self, servicio_id):
        try:
            resultado = self.service.contar_resenias_servicio(servicio_id)
            return jsonify(resultado), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id del servicio inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def verificar_resenia(self, resenia_id):
        try:
            resultado = self.service.verificar_resenia_existe(resenia_id)
            return jsonify(resultado), 200
        except InvalidId:
            return jsonify({"error": "Id de la reseña inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500