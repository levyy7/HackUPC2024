from flask import Flask, request
from computeDistanceFromRouterStrength import computeDistanceFromRouter1Strength, computeDistanceFromRouter2Strength, computeDistanceFromRouter3Strength

app = Flask(__name__)

r1X, r1Y = 0, 0

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#http://192.168.137.1:5000/prueba?router1=uno&router2=dos&router3=tres
@app.get("/test")
def data_get():
    routers_strength = [
        float(request.args.get('router1')), 
        float(request.args.get('router2')), 
        float(request.args.get('router3'))
    ]

    routers_distance = [
        computeDistanceFromRouter1Strength(routers_strength[0]),
        computeDistanceFromRouter2Strength(routers_strength[1]),
        computeDistanceFromRouter3Strength(routers_strength[2])
    ]

    #circles = [
    #    Circle(r1X, r1Y, routers_distance[0]),
    #    Circle(r2X, r2Y, routers_distance[1]), 
    #    Circle(r3X, r3Y, routers_distance[2])
    #]

    #posX, posY = triangulatePosition(routers_distance)

    return str(routers_strength[1])