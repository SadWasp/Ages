from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializer
from .serializers import UserSerializer
from .models import Item
from .models import User
import pymongo
#from pymongo import MongoClient
import ssl
import base64

#from flask import Flask
#from flask.ext.bcrypt import Bcrypt

#from cryptography.fernet import Fernet
#import basehash

connection_string = "mongodb+srv://admin2:123@cluster0.khvrb.mongodb.net/ages?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_string, ssl_cert_reqs=ssl.CERT_NONE)

db = client['ages']
items_collection = db["Items"]
users_collection = db["Users"]

client.close()



@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/items',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of items'
        },
        {
            'Endpoint': '/items/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single item object'
        },
        {
            'Endpoint': '/items/create',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new item with data sent in post request'
        },
        {
            'Endpoint': '/items/update',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing item with data sent in put request'
        },
        {
            'Endpoint': '/items/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing item'
        },
        #######################   USERS   #####################################
        {
            'Endpoint': '/users',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of users'
        },
        {
            'Endpoint': '/users/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single user'
        },
        {
            'Endpoint': '/users/create',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new user with data sent in post request'
        },
        {
            'Endpoint': '/users/update',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing user with data sent in put request'
        },
        {
            'Endpoint': '/users/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing user'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getItems(request):
    items_ = items_collection.find()
    serializer = ItemSerializer(items_, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getItem(request, pk):
    item_ = items_collection.find_one({"id": pk})
    serializer = ItemSerializer(item_, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createItem(request): 
    data = request.data
    item = Item.objects.create(
        name = data['name'],
        location = data['location'],
        quantity = data['quantity'],
    )
    serializer = ItemSerializer(item, many=False)
    items_collection.insert_one(serializer.data).inserted_id
    return Response(serializer.data) 

@api_view(['PUT'])
def updateItem(request, pk): 
    reqdata = request.data
    item = items_collection.find_one({"id": pk})#change to Id
    for key in reqdata:
        if reqdata[key] != item[key]:
            change = {"$set": {key: reqdata[key]}}
            items_collection.update_one(item, change)

    changedItem = items_collection.find_one({"id": pk})
    serializer = ItemSerializer(changedItem, many=False)
    return Response(serializer.data) 

@api_view(['DELETE'])
def deleteItem(request, pk): 
    item = items_collection.find_one({"id": pk})
    items_collection.delete_one(item)
    return Response('Item was deleted')






@api_view(['GET'])
def getUsers(request):
    users = users_collection.find()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request, pk):
    user = users_collection.find_one({"id": pk})
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

#restrict to admins.
@api_view(['POST'])
def createUser(request): 
    data = request.data
    user = User.objects.create(
        userName = data['userName'],
        password = data['password'], #encrypt password.
        role = data['role'], #lst of choices.
        nbOrdersFilled = data['nbOrdersFilled'],
    )
    serializer = UserSerializer(user, many=False)
    users_collection.insert_one(serializer.data).inserted_id
    return Response(serializer.data) 

@api_view(['PUT'])
def updateUser(request, pk): 
    reqdata = request.data
    user = users_collection.find_one({"id": pk})
    for key in reqdata:
        if reqdata[key] != user[key]:
            change = {"$set": {key: reqdata[key]}}
            users_collection.update_one(user, change)

    changedUser = users_collection.find_one({"id": pk})
    serializer = UserSerializer(changedUser, many=False)
    return Response(serializer.data) 

@api_view(['DELETE'])
def deleteUser(request, pk): 
    user = users_collection.find_one({"id": pk})
    users_collection.delete_one(user)
    return Response('User was deleted')



#try catch user not existing.
@api_view(['POST'])
def authLogin(request):
    data = request.data
    user = users_collection.find_one({"userName": data['userName']})
    #authPwd = base64.b64decode(data['password'] + b'==')
    #userPwd = base64.b64decode(user['password'] + b'==')


    #authPwd = base64.b64decode(encDBpwdStr1 + b'==')
    #userPwd = base64.b64decode(encUserpwdStr + b'==')



    if user["password"] == data["password"]:
        updateUser({"isConnected": True}, user['id'])
        serializer = UserSerializer(data, many=False)
        return Response(serializer.data) 

    return Response(False)


@api_view(['GET'])
def authLogout(request, pk):
    user = users_collection.find_one({"id": pk})
    updateUser({"isConnected": False}, user['id'])
    return Response("disconnected") 



@api_view(['POST'])
def authReg(request):
    valid = False
    data = request.data

    #last = users_collection.find().sort("id", pymongo.ASCENDING)
   # newId = last
    #encPass = data['password'].encode("utf-8")


    user = User.objects.create(
        userName = data['userName'],
        password = data['password'], #encrypt password.
        role = data['role'], #lst of choices.
        nbOrdersFilled = 0,
        isConnected = False,
    )
    serializer = UserSerializer(user, many=False)

    # userdb = {
    #     "id": user.id,
    #     "userName": data['userName'],
    #     "password" : base64.b64encode(encPass),
    #     "role" : data['role'],
    #     "nbOrdersFilled" : 0,
    #     "isConnected" : False
    # }
    users_collection.insert_one(user).inserted_id
    return Response(serializer.data) 

    #return Response("User created.")