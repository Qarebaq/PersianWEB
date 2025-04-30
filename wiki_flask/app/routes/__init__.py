from flask import Blueprint

bp = Blueprint('routes', __name__)

from app.routes.auth import bp as auth_bp

bp.register_blueprint(auth_bp)