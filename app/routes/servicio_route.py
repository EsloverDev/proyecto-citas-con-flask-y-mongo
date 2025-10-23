from flask import Blueprint
from app.controllers.servicio_controller import ServicioController

servicio_bp = Blueprint("servicios", __name__)
controller = ServicioController()

@servicio_bp.route("/agregarServicio", methods=["POST"])
def agregar_servicio():
    return controller.insertar_servicio()

@servicio_bp.route("/obtenerServicios", methods=['GET'])
def obtener_servicios():
    return controller.obtener_servicios()

@servicio_bp.route("/buscarServicio/<string:servicio_id>", methods=['GET'])
def buscar_servicio(servicio_id):
    return controller.buscar_servicio(servicio_id)

@servicio_bp.route("/buscarServiciosPorCategoria/<string:categoria_id>", methods=['GET'])
def buscar_servicios_categoria(categoria_id):
    return controller.buscar_servicios_por_categoria(categoria_id)

@servicio_bp.route("/buscarServiciosSinCategoria", methods=['GET'])
def buscar_servicios_sin_categoria():
    return controller.buscar_servicios_sin_categoria()

@servicio_bp.route("/actualizarServicio/<string:servicio_id>", methods=['PUT'])
def actualizar_servicio(servicio_id):
    return controller.modificar_servicio(servicio_id)

@servicio_bp.route("/actualizarCategoriaServicio/<string:servicio_id>", methods=['PUT'])
def actualizar_categoria_servicio(servicio_id):
    return controller.modificar_categoria_servicio(servicio_id)

@servicio_bp.route("/eliminarServicio/<string:servicio_id>", methods=['DELETE'])
def eliminar_servicio(servicio_id):
    return controller.eliminar_servicio(servicio_id)

@servicio_bp.route("/contarServiciosPorCategoria/<string:categoria_id>", methods=['GET'])
def contar_servicios_categoria(categoria_id):
    return controller.contar_servicios_categoria(categoria_id)

@servicio_bp.route("/verificarServicio/<string:servicio_id>", methods=['GET'])
def verificar_servicio(servicio_id):
    return controller.verificar_servicio(servicio_id)