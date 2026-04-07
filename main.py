from speech import listen
from nlp import get_intent
from tasks import execute
from tts import speak

def main():
    speak("Hello, I am your assistant")

    while True:
        command = listen()

        if command == "":
            continue

        intent = get_intent(command)
        result = execute(intent)

        if result == "exit":
            speak("Goodbye!")
            break

        speak(result)

if __name__ == "__main__":
    main()