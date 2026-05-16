from modules.speech_to_text import listen
from modules.text_to_speech import speak
from modules.chatbot import chatbot_response

USER_NAME = "Kavya"


def main():
    speak(f"Hello {USER_NAME}, how can I help you?")

    while True:
        print("Listening...")

        text = listen()

        if not text:
            continue

        print("You said:", text)

        text = text.lower()

        if (
    "stop" in text
    or "exit" in text
    or "quit" in text
    or "bye" in text
):
            speak(f"Goodbye {USER_NAME}")
            break

        response = chatbot_response(text)

        print("Assistant:", response)

        speak(response)


if __name__ == "__main__":
    main()