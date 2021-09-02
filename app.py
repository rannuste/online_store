from main import app, mongo
from bson import json_util
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
import json


@app.route('/add', methods=['POST'])
def add_product():
    product = mongo.db.product
    name = request.json['name']
    description = request.json['description']
    value1 = request.json['attributes']['key1']
    value2 = request.json['attributes']['key2']
	# save details
    id = product.insert({'name': name, 'description': description,'attributes' : {'key1': value1, 'key2': value2}})
    new_product = product.find_one({'_id': id})
    resp = json.loads(json_util.dumps(new_product))
    return resp


@app.route('/products/name/<name>', methods=['GET'])
def products_name(name):
	product = mongo.db.product.find({'name': name})
	resp = dumps(product)
	return resp
		

@app.route('/products/attributes/<key>/<value>', methods=['GET'])
def products_attribute_key1(key, value):
	product = mongo.db.product.find({'attributes.' + key : value})
	resp = dumps(product)
	return resp


@app.route('/product/<id>', methods=['GET'])
def product(id):
	products = mongo.db.product.find_one({'_id': ObjectId(id)})
	resp = dumps(products)
	return resp

		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run()