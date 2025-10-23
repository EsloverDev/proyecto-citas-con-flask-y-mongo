from flask import Blueprint
from app.controllers.categoria_servicio_controller import CategoriaServicioController

categoria_servicio_bp = Blueprint("categoria_servicio", __name__)
controller = CategoriaServicioController()

@categoria_servicio_bp.route("/crearCategoria", methods=['POST'])
def ingresar_categoria():
    return controller.agregar_categoria()

@categoria_servicio_bp.route("/obtenerCategorias", methods=['GET'])
def traer_categorias():
    return controller.obtener_categorias()

@categoria_servicio_bp.route("/buscarCategoria/<string:categoria_id>", methods=['GET'])
def traer_una_categoria(categoria_id):
    return controller.buscar_categoria(categoria_id)

@categoria_servicio_bp.route("/actualizarCategoria/<string:categoria_id>", methods=['PUT'])
def cambiar_categoria(categoria_id):
    return controller.modificar_categoria(categoria_id)

@categoria_servicio_bp.route("/insertarServicioCategoria/<string:categoria_id>", methods=['POST'])
def insertar_servicio(categoria_id):
    return controller.ingresar_servicio(categoria_id)

@categoria_servicio_bp.route("/eliminarServicio/<string:categoria_id>/<string:servicio_id>", methods=['DELETE'])
def borrar_servicio(categoria_id, servicio_id):
    return controller.quitar_servicio(categoria_id, servicio_id)

@categoria_servicio_bp.route("/eliminarCategoria/<string:categoria_id>", methods=['DELETE'])
def borrar_categoria(categoria_id):
    return controller.quitar_categoria(categoria_id)
