def detect_intent(command):

    if "hello" in command:
        return "greeting"

    elif "time" in command:
        return "time"

    elif "date" in command:
        return "date"

    elif "weather" in command:
        return "weather"

    elif "youtube" in command:
        return "youtube"

    elif "google" in command:
        return "google"

    elif "email" in command:
        return "email"

    elif "reminder" in command:
        return "reminder"

    elif "custom" in command:
        return "custom"

    else:
        return "chat"