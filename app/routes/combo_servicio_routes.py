from flask import Blueprint
from app.controllers.combo_servicio_controller import ComboServicioController

combo_servicio_bp = Blueprint("combos_servicios", __name__)
controller = ComboServicioController()

@combo_servicio_bp.route("/crearCombo", methods=['POST'])
def crear_combo():
    return controller.crear_combo()

@combo_servicio_bp.route("/obtenerCombos", methods=['GET'])
def obtener_combos():
    return controller.obtener_combos()

@combo_servicio_bp.route("/buscarCombo/<string:combo_id>", methods=['GET'])
def buscar_combo(combo_id):
    return controller.buscar_combo(combo_id)

@combo_servicio_bp.route("/buscarCombosActivos", methods=['GET'])
def buscar_combos_activos():
    return controller.buscar_combos_activos()

@combo_servicio_bp.route("/buscarCombosServicio/<string:servicio_id>", methods=['GET'])
def buscar_combos_servicio(servicio_id):
    return controller.buscar_combos_por_servicio(servicio_id)

@combo_servicio_bp.route("/buscarComboNombre", methods=['GET'])
def buscar_combo_nombre():
    return controller.buscar_combo_por_nombre()

@combo_servicio_bp.route("/actualizarCombo/<string:combo_id>", methods=['PUT'])
def actualizar_combo(combo_id):
    return controller.modificar_combo(combo_id)

@combo_servicio_bp.route("/agregarServicioCombo/<string:combo_id>", methods=['PUT'])
def agregar_servicio_combo(combo_id):
    return controller.agregar_servicio_combo(combo_id)

@combo_servicio_bp.route("/eliminarServicioCombo/<string:combo_id>/<string:servicio_id>", methods=['DELETE'])
def eliminar_servicio_combo(combo_id, servicio_id):
    return controller.eliminar_servicio_combo(combo_id, servicio_id)

@combo_servicio_bp.route("/eliminarCombo/<string:combo_id>", methods=['DELETE'])
def eliminar_combo(combo_id):
    return controller.eliminar_combo(combo_id)

@combo_servicio_bp.route("/contarCombos", methods=['GET'])
def contar_combos():
    return controller.contar_combos()

@combo_servicio_bp.route("/verificarCombo/<string:combo_id>", methods=['GET'])
def verificar_combo(combo_id):
    return controller.verificar_combo(combo_id)