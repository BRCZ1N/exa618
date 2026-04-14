from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# 🔹 Conexão com MongoDB
client = MongoClient("mongodb+srv://Vercel-Admin-atlas_mongo_db:3Yx3PrtwUQA4EFUZ@atlas-mongo-db.n5rdpwr.mongodb.net/?retryWrites=true&w=majority")
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


# ✅ 2) Listar todas as mensagens
@app.route("/", methods=["GET"])
def get_messages():
    mensagens = []

    for msg in collection.find().sort("date", -1):
        mensagens.append({
            "id": str(msg["_id"]),
            "action": msg["action"],
            "message": msg["message"],
            "author": msg["author"],
            "date": msg["date"].strftime("%d/%m/%Y %H:%M:%S")
        })

    return jsonify(mensagens), 200


if __name__ == "__main__":
    app.run(debug=True)