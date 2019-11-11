from flask import Flask
from flask_restful import Api
from MarketPlace.resources.task import Task
from MarketPlace.resources.taskbyid import TaskByID

app = Flask(__name__)

restServerInstance = Api(app)

restServerInstance.add_resource(Task,"/api/v1.0/task")
restServerInstance.add_resource(TaskByID,"/api/v1.0/task/prdCd/<string:taskId>")