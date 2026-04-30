from brain import load_data, get_answer
from voice import speak, listen

print("📚 NOVA STUDY ASSISTANT STARTED")

data = load_data()

while True:
    print("\nPress ENTER to speak (or type 'exit')...")
    cmd = input()

    if cmd == "exit":
        break

    print("🎤 Speak now...")
    query = listen()

    if not query:
        print("❌ No valid input")
        continue

    print("You:", query)

    answer = get_answer(query, data)

    print("AI:", answer)
    speak(answer)
