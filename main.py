import os
import json
import time
import pyttsx3
import speech_recognition as sr
import requests
import datetime

# ========== CONFIG ==========
MEMORY_FILE = "jarvis_memory.json"
OLLAMA_MODEL = "llama3"
WAKE_WORD = "hey jarvis"

# ========== SETUP ==========
engine = pyttsx3.init()
engine.setProperty('rate', 175)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)

recognizer = sr.Recognizer()

# ========== MEMORY ==========
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
else:
    memory = []

def save_memory(prompt, response):
    memory.append({"prompt": prompt, "response": response})
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory[-50:], f, indent=2)

# ========== SPEAK ==========
def speak(text):
    print(f"\n🧠 Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

# ========== LISTEN ==========
def listen():
    with sr.Microphone() as source:
        print("🎧 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            command = recognizer.recognize_google(audio).lower()
            print(f"🗣️ You said: {command}")
            return command
        except:
            return ""

# ========== ASK OLLAMA with STREAMING ==========
def ask_ollama(prompt):
    try:
        url = "http://localhost:11434/api/chat"
        headers = {"Content-Type": "application/json"}
        payload = {
            "model": OLLAMA_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": True
        }

        print("\n🧠 Jarvis (thinking): ", end="", flush=True)
        response = requests.post(url, headers=headers, json=payload, stream=True)

        full_reply = ""
        for line in response.iter_lines():
            if line:
                try:
                    json_data = json.loads(line.decode("utf-8").replace("data: ", ""))
                    token = json_data.get("message", {}).get("content", "")
                    print(token, end="", flush=True)
                    full_reply += token
                except:
                    continue
        print()  # newline after streaming
        save_memory(prompt, full_reply)
        return full_reply
    except Exception as e:
        return f"Error from Ollama: {str(e)}"

# ========== DOCUMENTATION ==========
def write_documentation():
    speak("What topic do you want documentation for?")
    topic = listen()
    if topic:
        prompt = f"Write detailed technical documentation about {topic}."
        result = ask_ollama(prompt)
        with open("documentation.txt", "w", encoding="utf-8") as f:
            f.write(result)
        speak("Documentation saved to documentation.txt")

# ========== WAKE + HANDLE ==========
def wait_for_wake_word():
    while True:
        print("⏳ Waiting for 'hey jarvis'...")
        said = listen()
        if WAKE_WORD in said:
            speak("Yes, I'm listening!")
            return

def handle_command(command):
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today is {today}")
    elif "remember" in command:
        speak("What should I remember?")
        note = listen()
        if note:
            memory.append({"type": "note", "content": note})
            with open(MEMORY_FILE, "w") as f:
                json.dump(memory, f, indent=2)
            speak("Got it. Saved to memory.")
    elif "what do you remember" in command:
        notes = [m['content'] for m in memory if m.get("type") == "note"]
        if notes:
            speak("Here are your saved notes:")
            for n in notes:
                speak(n)
        else:
            speak("You haven't asked me to remember anything yet.")
    elif "write documentation" in command:
        write_documentation()
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    else:
        result = ask_ollama(command)
        speak(result)

# ========== MAIN ==========
if __name__ == "__main__":
    speak("Jarvis is now online and ready to assist you.")
    while True:
        wait_for_wake_word()
        user_command = listen()
        if user_command:
            handle_command(user_command)
