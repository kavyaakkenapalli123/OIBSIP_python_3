import speech_recognition as sr


def listen():

    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 300
    recognizer.pause_threshold = 1

    with sr.Microphone() as source:

        print("Speak now...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=8
            )

            text = recognizer.recognize_google(audio)

            return text.lower()

        except sr.WaitTimeoutError:
            print("Listening timeout")
            return ""

        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""

        except sr.RequestError:
            print("Internet connection issue")
            return ""

        except Exception as e:
            print("Speech Recognition Error:", e)
            return ""