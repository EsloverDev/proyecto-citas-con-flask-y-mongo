from flask import jsonify, request
from bson.errors import InvalidId
from app.services.categoria_servicio_service import CategoriaServicioService

class CategoriaServicioController:
    def __init__(self):
        self.service = CategoriaServicioService()

    def agregar_categoria(self):
        try:
            categoria_data = request.get_json()
            if not categoria_data:
                return jsonify({"error": "No se enviaron datos para crear la categoría"}), 400
            
            resultado = self.service.crearCategoria(categoria_data)
            return jsonify(resultado), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def obtener_categorias(self):
        try:
            resultado = self.service.obtener_todas_categorias()
            return jsonify(resultado), 200
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def buscar_categoria(self, categoria_id):
        try:
            categoria = self.service.obtener_categoria_por_id(categoria_id)
            return jsonify(categoria), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id de la categoría inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def modificar_categoria(self, categoria_id):
        try:
            datos_actualizacion = request.get_json()
            if not datos_actualizacion:
                return jsonify({"error": "No se enviaron datos para actualizar"}), 400
            
            resultado = self.service.actualizar_categoria(categoria_id, datos_actualizacion)
            return jsonify(resultado), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id de categoría inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def ingresar_servicio(self, categoria_id):
        try:
            servicio_data = request.get_json()
            if not servicio_data:
                return jsonify({"error": "No se enviaron los datos del servicio"}), 400

            resultado = self.service.agregar_servicio(categoria_id, servicio_data)
            return jsonify(resultado), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id de la categoría o del servicio inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def quitar_servicio(self, categoria_id, servicio_id):
        try:
            resultado = self.service.eliminar_servicio(categoria_id, servicio_id)
            return jsonify(resultado), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id de la categoría o del servicio inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        
    def quitar_categoria(self, categoria_id):
        try:
            resultado = self.service.eliminar_categoria(categoria_id)
            return jsonify(resultado), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except InvalidId:
            return jsonify({"error": "Id de la categoría inválido"}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500