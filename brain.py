import os
import json
import re

DATA_PATH = "data"
CACHE = []


def normalize(text):
    text = text.lower()
    text = re.sub(r"[^\u0980-\u09FFa-zA-Z0-9 ]", "", text)
    return text


def load_data():
    all_data = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".json"):
            try:
                with open(os.path.join(DATA_PATH, file), "r", encoding="utf-8") as f:
                    data = json.load(f)

                    if isinstance(data, list):
                        all_data.extend(data)
            except:
                pass

    return all_data


def reload_data():
    global CACHE
    CACHE = load_data()
    print("🧠 Brain reloaded! Total:", len(CACHE))


def score(q, a):
    q = normalize(q)
    a = normalize(a)

    q_words = set(q.split())
    a_words = set(a.split())

    score = len(q_words & a_words)

    if q in a:
        score += 5

    return score


def get_answer(query):
    global CACHE

    best = None
    best_score = 0

    for item in CACHE:
        s = score(query, item.get("question", ""))

        if s > best_score:
            best_score = s
            best = item

    if best:
        return f"{best.get('subject','')}\n{best['question']}\n{best['answer']}"

    return "এই প্রশ্নের উত্তর পাওয়া যায়নি"
