from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os, json

app = Flask(__name__, static_folder="web")
CORS(app)

DATA_PATH = "data"
CACHE = []


def load_data():
    global CACHE
    CACHE = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".json"):
            with open(os.path.join(DATA_PATH, file), "r", encoding="utf-8") as f:
                try:
                    CACHE.extend(json.load(f))
                except:
                    pass

load_data()


def search(q):
    q = q.lower()

    best = None
    score_max = 0

    for item in CACHE:
        qq = item["question"].lower()

        score = sum(1 for w in q.split() if w in qq)

        if score > score_max:
            score_max = score
            best = item

    if best:
        return best["answer"]

    return "এই প্রশ্নের উত্তর পাওয়া যায়নি"


@app.route("/")
def home():
    return send_from_directory("web", "index.html")


@app.route("/ask", methods=["POST"])
def ask():
    q = request.json["question"]
    ans = search(q)

    return jsonify({"answer": ans})


app.run(host="0.0.0.0", port=5000)
