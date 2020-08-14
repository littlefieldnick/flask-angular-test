from flask import Blueprint, jsonify, request
from sqlalchemy import join

from app.models import Resource, ResourceCategory

resource_bp = Blueprint('resource', __name__)

def convert_resources_to_dict(resources):
    resources_as_dicts = []
    for resource in resources:
        resource = resource.__dict__
        resource["category"] = ResourceCategory.get_resource_category_name(resource["category_id"])

        if '_sa_instance_state' in resource:
            del resource['_sa_instance_state']

        resources_as_dicts.append(resource)
    return resources_as_dicts

@resource_bp.route("/resources/<int:id>")
def get_resource(id):
    resource = Resource.get_single_resource_as_dict(id)

    if resource is None:
        return jsonify({})

    return jsonify(resource)

@resource_bp.route("/resources/")
def get_resources():
    resources = Resource.get_resources_as_dict()
    return jsonify(resources)

@resource_bp.route("/resources/search/")
def search():
    print(request.args)
    category = request.args.get('category', None)
    resource = request.args.get('resource', None)
    resources = Resource.query
    print(category, resource)
    if category:
        resources = resources.select_from(join(Resource, ResourceCategory)) \
            .filter(ResourceCategory.name.like('%' + category + '%'))
    if resource:
        resources = resources.filter(Resource.name.like('%' + resource + '%'))

    return jsonify(convert_resources_to_dict(resources))