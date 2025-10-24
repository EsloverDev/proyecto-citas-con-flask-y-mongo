from flask import jsonify
from bson.errors import InvalidId
from app.services.categoria_servicio_service import CategoriaServicioService

class CategoriaServicioController:
    def __init__(self):
        self.service = CategoriaServicioService()

    def agregar_categoria(self):
        try:
            resultado = self.service.crearCategoria()
            return jsonify(resultado), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    def obtener_categorias(self):
        try:
            resultado = self.service.obtener_todas_categorias()
            return jsonify(resultado), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    def buscar_categoria(self, categoria_id):
        try:
            categoria = self.service.obtener_categoria_por_id(categoria_id)
            return jsonify(categoria), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    def modificar_categoria(self, categoria_id):
        try:
            resultado = self.service.actualizar_categoria(categoria_id)
            return jsonify(resultado), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    def ingresar_servicio(self, categoria_id):
        try:
            resultado = self.service.agregar_servicio(categoria_id)
            return jsonify(resultado), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    def quitar_servicio(self, categoria_id, servicio_id):
        try:
            resultado = self.service.eliminar_servicio(categoria_id, servicio_id)
            return jsonify(resultado)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    def quitar_categoria(self, categoria_id):
        try:
            resultado = self.service.eliminar_categoria(categoria_id)
            return jsonify(resultado), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500