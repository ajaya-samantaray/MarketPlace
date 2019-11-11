from flask_restful import Resource
import logging as logger
from MarketPlace.common import mpdb
from flask import request, jsonify,Response

class Task(Resource):
    def __init__(self):
        self.prd = mpdb.Product()

    def post(self):
        logger.debug("Inside the post method of Task")
        request_data = request.get_json()
        logger.debug(request_data)
        if self.prd.validProduct(request_data):
            self.prd.add_product(request_data['ProductCode'], request_data['Name'], request_data['Price'])
            response = Response("", 201, mimetype='application/json')
            response.headers['location'] = "/products" +str(request_data['ProductCode'])
            return response
        else:
            InvalidProductMesg ={
                "error": "Invalid Product Object passed",
                "helpString": "Input data should be in format ProductCode, Name and Price"
            }
            response = Response(json.dumps(InvalidProductMesg),status=400, mimetype="application/json")
            return response

    def get(self):
        logger.debug("Inisde the get method of Task")
        return jsonify({'products': self.prd.get_all_products()})
        response = Response("", 200, mimetype='application/json')
        return response






