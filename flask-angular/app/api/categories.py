from flask import Blueprint, jsonify
from app.models import ResourceCategory

categories_bp = Blueprint('categories', __name__)

@categories_bp.route("/categories/")
def get_categories():
    categories = ResourceCategory.get_resource_categories_as_dict()
    return jsonify(categories)