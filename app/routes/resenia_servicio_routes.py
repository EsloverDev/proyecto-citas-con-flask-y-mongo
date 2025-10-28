from flask import Blueprint
from app.controllers.resenia_servicio_controller import ReseniaServicioController

resenia_servicio_bp = Blueprint('resenias_servicios', __name__)
controller = ReseniaServicioController()

@resenia_servicio_bp.route("/crearResenia", methods=['POST'])
def crear_resenia():
    return controller.crear_resenia()

@resenia_servicio_bp.route('/listarResenias', methods=['GET'])
def obtener_resenias():
    return controller.obtener_resenias()

@resenia_servicio_bp.route('/buscarResenia/<string:resenia_id>', methods=['GET'])
def buscar_resenia(resenia_id):
    return controller.buscar_resenia(resenia_id)

@resenia_servicio_bp.route('/buscarReseniasServicio/<string:servicio_id>', methods=['GET'])
def buscar_resenias_servicio(servicio_id):
    return controller.buscar_resenias_por_servicio(servicio_id)

@resenia_servicio_bp.route('/obtenerPromedioServicio/<string:servicio_id>', methods=['GET'])
def obtener_promedio_servicio(servicio_id):
    return controller.obtener_promedio_servicio(servicio_id)

@resenia_servicio_bp.route('/actualizarResenia/<string:resenia_id>', methods=['PUT'])
def actualizar_resenia(resenia_id):
    return controller.actualizar_resenia(resenia_id)

@resenia_servicio_bp.route('/eliminarResenia/<string:resenia_id>', methods=['DELETE'])
def eliminar_resenia(resenia_id):
    return controller.eliminar_resenia(resenia_id)

@resenia_servicio_bp.route('/contarReseniasServicio/<string:servicio_id>', methods=['GET'])
def contar_resenias_servicio(servicio_id):
    return controller.contar_resenias_servicio(servicio_id)

@resenia_servicio_bp.route('/verificarResenia/<string:resenia_id>', methods=['GET'])
def verificar_resenia(resenia_id):
    return controller.verificar_resenia(resenia_id)