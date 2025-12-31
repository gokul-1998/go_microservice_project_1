import os,gridfs,pika,json
# gridfs is used to store large files in mongodb
# pika is used to connect to rabbitmq
from flask import Flask,request,Response
from flask_pymongo import PyMongo
from auth import validate
from auth_svc import access
from storage import util

server = Flask(__name__)
server.config["MONGO_URI"] = os.getenv("MONGO_URI","mongodb://host.minikube.internal:27017/videos")

mongo = PyMongo(server)

fs=gridfs.GridFS(mongo.db)

connection=pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel=connection.channel()
# this will create the queue if it does not exist
# this is synchronous queue declaration, we are not using async here because this is a simple example, in production we should use async


@server.route("/login",methods=["POST"])
def login():
    token,err= access.login(request)