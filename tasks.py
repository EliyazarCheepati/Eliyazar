import datetime
import webbrowser

def execute(intent):
    if intent == "time":
        return datetime.datetime.now().strftime("%H:%M")
    
    elif intent == "date":
        return str(datetime.date.today())
    
    elif intent == "youtube":
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"
    
    elif intent == "exit":
        return "exit"
    
    else:
        return "Sorry, I didn't understand"