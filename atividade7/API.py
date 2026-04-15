from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv


load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

app = Flask(__name__)

client = MongoClient(mongo_uri)
db = client["blog"]
collection = db["messages"]

@app.route("/", methods=["POST"])
def add_message():
    dados = request.get_json()

    action = dados.get("action")
    message = dados.get("message")
    author = dados.get("author")

    if action and message and author:
        collection.insert_one({
            "action": action,
            "message": message,
            "author": author,
            "date": datetime.now()
        })

        return jsonify({"status": "OK"}), 200

    return jsonify({"status": "erro", "mensagem": "Dados inválidos"}), 400


@app.route("/", methods=["GET"])
def get_messages():
    mensagens = []

    for msg in collection.find().sort("date", -1):
        mensagens.append({
            "action": msg["action"],
            "message": msg["message"],
            "author": msg["author"],
            "date": msg["date"].strftime("%d/%m/%Y %H:%M:%S")
        })

    return jsonify(mensagens), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)