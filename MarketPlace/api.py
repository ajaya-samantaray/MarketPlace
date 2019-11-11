from flask import Flask
from flask_restful import Api
from MarketPlace.resources.task import Task
from MarketPlace.resources.taskbyid import TaskByID

app = Flask(__name__)

restServerInstance = Api(app)

restServerInstance.add_resource(Task,"/v1/products")
restServerInstance.add_resource(TaskByID,"/v1/product/<string:taskId>")