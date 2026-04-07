def get_intent(command):
    if "time" in command:
        return "time"
    elif "date" in command:
        return "date"
    elif "youtube" in command:
        return "youtube"
    elif "exit" in command:
        return "exit"
    else:
        return "unknown"