import os
import json

INPUT_FILE = "raw_data.txt"
OUTPUT_DIR = "data"

os.makedirs(OUTPUT_DIR, exist_ok=True)

BATCH_SIZE = 500  # প্রতি ফাইলে 500 প্রশ্ন


def parse_line(line):
    # format: question || answer
    parts = line.split("||")

    if len(parts) != 2:
        return None

    return {
        "type": "qa",
        "subject": "Auto",
        "question": parts[0].strip(),
        "answer": parts[1].strip()
    }


def build():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

    data = []
    file_index = 1

    for line in lines:
        item = parse_line(line)
        if item:
            data.append(item)

        if len(data) == BATCH_SIZE:
            save_file(data, file_index)
            data = []
            file_index += 1

    if data:
        save_file(data, file_index)


def save_file(data, index):
    file_path = os.path.join(OUTPUT_DIR, f"auto_{index}.json")

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Saved:", file_path, "Items:", len(data))


if __name__ == "__main__":
    build()
