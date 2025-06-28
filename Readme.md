# 🧠 Jarvis AI - Offline Voice Assistant using Ollama + LLaMA3

Jarvis is a fully offline, voice-activated AI assistant that uses **Ollama** and **LLaMA3** for local language understanding, supports memory, wake-word activation (`Hey Jarvis`), and documentation writing – all with voice interaction!

---

## 🚀 Features

- 🎙️ Wake-word activation: Just say "Hey Jarvis"
- 🧠 Offline intelligent replies using [Ollama](https://ollama.com/) + LLaMA3
- 🗣️ Voice recognition via `speech_recognition`
- 🧏‍♂️ Text-to-speech response using `pyttsx3`
- 📝 Memory system: Save & recall notes
- 📄 Generate technical documentation via voice
- 💾 All data stored locally – no internet needed!

---

## 🛠️ Requirements

Install the dependencies:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
pyttsx3
speechrecognition
requests
```

You also need to install:

- Python 3.8+
- [Ollama](https://ollama.com/) with the `llama3` model:
    ```bash
    ollama run llama3
    ```

---

## 🧠 How It Works

1. Start the assistant:
   ```bash
   python jarvis.py
   ```

2. Wait for:
   ```
   ⏳ Waiting for 'hey jarvis'...
   ```

3. Say:
   ```
   Hey Jarvis
   ```

4. Then ask:
   ```
   What time is it?
   Remember I have a meeting at 5 PM.
   What do you remember?
   Write documentation about Docker.
   ```

Jarvis will respond via voice and show replies in the terminal.

---

## 📁 Project Structure

```
.
├── jarvis.py              # Main script
├── jarvis_memory.json     # Memory file (auto-created)
├── documentation.txt      # Output file for generated documentation
├── requirements.txt       # Python dependencies
```

---

## 📄 Example Commands

| Command                        | Action                          |
|-------------------------------|---------------------------------|
| "Hey Jarvis, what time is it" | Tells current time              |
| "Remember I have a call"      | Saves note                      |
| "What do you remember?"       | Recalls saved notes             |
| "Write documentation on AI"   | Creates AI doc in `.txt` file   |
| "Stop" or "Exit"              | Ends the program                |

---

## 🔐 Local & Secure

- No data is sent over the internet
- All AI processing is done locally via Ollama
- All memory is saved in `jarvis_memory.json`

---

## 🧪 Troubleshooting

- Make sure **Ollama** is running:
  ```bash
  ollama run llama3
  ```

- If mic input doesn't work:
  - Check that your microphone is set as **default input**
  - Run the Python file as Administrator or use a virtual environment

---

## 💡 Future Features (You Can Contribute!)

- GUI with `Tkinter` or `PyQt`
- File summarization
- Real-time Whisper transcription
- Document export (PDF, Markdown)
- Multilingual support

---

## 🤝 Contributing

1. Fork the repo
2. Create a new branch
3. Add your changes
4. Submit a pull request

---

## ⚖️ License

This project is open source under the MIT License.

---

## 💬 Credits

Built with 💙 by [sivaaditya]. Powered by:
- Python
- Ollama
- Meta's LLaMA3
- Google Speech Recognition
- pyttsx3
