from flask import Flask
from app.config import Config
from app.extensions import mongo
from app.routes.servicio_route import servicio_bp
from app.routes.categoria_servicio_routes import categoria_servicio_bp
from app.routes.combo_servicio_routes import combo_servicio_bp
from app.routes.resenia_servicio_routes import resenia_servicio_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)

    app.register_blueprint(servicio_bp, url_prefix="/api")
    app.register_blueprint(categoria_servicio_bp, url_prefix="/api")
    app.register_blueprint(combo_servicio_bp, url_prefix="/api")
    app.register_blueprint(resenia_servicio_bp, url_prefix="/api")
    
    return app