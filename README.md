# 🎙️ AI Voice Assistant using Python

## 📌 Project Overview

AI Voice Assistant is a Python-based desktop voice assistant that can understand voice commands and perform various tasks such as answering questions, opening applications, searching the web, converting speech to text, and generating intelligent responses using AI APIs.

The project combines Speech Recognition, Text-to-Speech, and Natural Language Processing to create an interactive assistant similar to virtual assistants like Siri, Alexa, or Google Assistant.

---

# 🚀 Features

- 🎤 Speech Recognition
- 🔊 Text-to-Speech Conversion
- 🤖 AI Chatbot Integration
- 🌐 Web Searching
- 📂 Open Applications
- 🗣️ Voice-Based Interaction
- 🧠 Intent Recognition
- ⚡ Real-Time Responses
- ❌ Error Handling

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| SpeechRecognition | Speech-to-Text |
| pyttsx3 | Text-to-Speech |
| OpenAI / OpenRouter API | AI Responses |
| PyAudio | Microphone Input |
| NLP | Intent Recognition |

---

# 📁 Project Structure

```bash
voice_assistant/
│
├── main.py
├── settings.py
├── requirements.txt
│
├── modules/
│   ├── chatbot.py
│   ├── speech_to_text.py
│   └── text_to_speech.py
│
├── nlp/
│   └── intent_recognition.py
│
├── speech/
│   ├── recognizer.py
│   └── tts.py
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/voice_assistant.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd voice_assistant
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Configuration

Create a `.env` file in the root directory.

```env
API_KEY=your_api_key_here
```

---

# ▶️ Run the Project

```bash
python main.py
```

---

# 🧠 Working Principle

1. User speaks through microphone.
2. Speech Recognition converts voice into text.
3. NLP identifies user intent.
4. Assistant processes request.
5. AI API generates response.
6. Text-to-Speech converts output into voice.

---

# 📚 Modules Explanation

## 🎤 Speech Recognition
Converts human speech into text using microphone input.

## 🔊 Text-to-Speech
Converts assistant responses into audible voice.

## 🤖 Chatbot Module
Communicates with AI APIs to generate smart responses.

## 🧠 Intent Recognition
Identifies what the user wants based on voice command.

---

# 🎯 Sample Commands

- "Open YouTube"
- "Search Python tutorials"
- "What is Artificial Intelligence?"
- "Tell me today's weather"
- "Open Calculator"

---

# 📦 Requirements

```txt
speechrecognition
pyttsx3
pyaudio
requests
python-dotenv
```

---

# ⚠️ Error Handling

The application handles:
- Invalid voice input
- Network errors
- API failures
- Microphone issues

---

# 🔒 Security

- API keys are stored securely using `.env`
- `.gitignore` prevents secrets from uploading to GitHub

---

# 📈 Future Enhancements

- GUI Interface
- Wake Word Detection
- Multi-language Support
- AI Memory System
- Face Recognition
- Mobile App Version

---

# 🎓 Learning Outcomes

This project helps understand:
- Python Programming
- APIs Integration
- NLP Basics
- Voice Processing
- AI Application Development

---

# 📷 Output 
<img width="1889" height="1033" alt="Screenshot 2026-05-25 091606" src="https://github.com/user-attachments/assets/c6d83496-2a5d-416e-b801-21cdfa32b381" />

<img width="1911" height="1025" alt="Screenshot 2026-05-25 091720" src="https://github.com/user-attachments/assets/a3fb3b70-259a-48e0-93d2-ab2a046d22de" />



```bash
User: What is Python?

Assistant:
Python is a high-level programming language used for web development,
AI, automation, and more.
```

---

# 👩‍💻 Author

Kavya Akkenapalli

---

# 🌟 Conclusion

The AI Voice Assistant project demonstrates how Artificial Intelligence,
Speech Recognition, and NLP can be integrated to create an interactive
voice-controlled system capable of assisting users in daily tasks.
