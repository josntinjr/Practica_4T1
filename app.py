import os
import requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("submit vote")
def vote(data):
    selection = data["selection"]
    emit("announce vote", {"selection": selection}, broadcast=True)

@ socketio.on('saludar')
def saludar(mensaje, user, fecha):

    print("fecha: ", fecha)

    data = {"message": mensaje, "username": user, "fecha": fecha}
    # Emitir a todos con el argumento broadcast
    emit('general', data,
         broadcast=True, include_self=False)

    # Enviar respuesta de evento emit al cliente
    return (f'{mensaje}')
