import logging as logger
from flask import request, jsonify,Response

class ApiCall:

    def getRequest():       
        try:
            request_data = request.get_json()

            if not request_data:
                InvalidProductMesg ={
                "error": "No Product Object passed",
                "helpString": "Input data should be in format ProductCode, Name and Price"
                }
                response = Response(json.dumps(InvalidProductMesg),status=400, mimetype="application/json")
                return response
            else:
                return request_data

        except Exception as e:
            logger.debug('Error connecting to API: '+ str(e))
            InvalidProductMesg ={
                "error": "Error connecting to API",
                "helpString": "Please check the api end point"
                }
            response = Response(json.dumps(InvalidProductMesg),status=400, mimetype="application/json")
            return response