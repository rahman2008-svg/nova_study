import os
import json

DATA_PATH = "data"
CACHE = []


# ---------------------------
# LOAD ALL DATA
# ---------------------------
def load_data():
    all_data = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".json"):
            print("Loading:", file)

            with open(os.path.join(DATA_PATH, file), "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    all_data.extend(data)
                except Exception as e:
                    print("Error in", file, e)

    return all_data


# ---------------------------
# SMART SCORING ENGINE
# ---------------------------
def smart_score(query, text):
    query = query.lower()
    text = text.lower()

    q_words = set(query.split())
    t_words = set(text.split())

    score = len(q_words & t_words)

    # exact phrase boost
    if query in text:
        score += 5

    # word match boost
    for q in q_words:
        if q in text:
            score += 1

    return score


# ---------------------------
# GET BEST ANSWER
# ---------------------------
def get_answer(query):
    global CACHE

    best = None
    best_score = 0

    for item in CACHE:
        question = item.get("question", "")
        score = smart_score(query, question)

        if score > best_score:
            best_score = score
            best = item

    if best:
        return best.get("answer", "No answer found")

    return "এই প্রশ্নের উত্তর পাওয়া যায়নি"


# ---------------------------
# DUPLICATE DETECTION
# ---------------------------
def is_duplicate(new_q):
    new_q = new_q.lower()

    for item in CACHE:
        if item.get("question", "").lower() == new_q:
            return True

    return False


# ---------------------------
# RELOAD BRAIN (AUTO UPDATE)
# ---------------------------
def reload_data():
    global CACHE
    CACHE = load_data()
    print("🧠 Brain loaded:", len(CACHE), "items")
