from flask_restful import Resource
import json
import logging as logger

from MarketPlace.common import mpdb
from flask import request, jsonify,Response

class TaskByID(Resource):

    def __init__(self):
        self.prd = mpdb.Product()

    def get(self,taskId):
        retVal = self.prd.get_product(taskId)
        if retVal:
            return jsonify(retVal)
        else:
            return {"message" : "No products found by ProductCode : {}".format(taskId)},404

    def put(self,taskId):
        request_data = request.get_json()
        retVal = self.prd.get_product(taskId)
        if retVal:
            if self.prd.validProduct(request_data):
                self.prd.update_product(request_data['ProductCode'], request_data['Name'], request_data['Price'])
                return {"message": "Successfully updated ProductCode".format(taskId)}, 200
            else:
                return {"message": "Error while updating ProductCode".format(taskId)}, 401
        else:
            return {"message": "No products found by ProductCode : {}".format(taskId)}, 404

    def delete(self, taskId):
        retVal = self.prd.get_product(taskId)
        if retVal:
            self.prd.delete_product(taskId)
            return {"message": "Successfully deleted ProductCode".format(taskId)}, 200
        else:
            return {"message": "No products found by ProductCode : {}".format(taskId)}, 404







