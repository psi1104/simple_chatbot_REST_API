def chatbot(sentence):
    reply = ""

    if sentence == "Hello":
        reply = "Hi!"

    elif sentence == "What is your name?":
        reply = "My name is chatbot!"

    elif sentence == "Where are you located?":
        reply = "I located seoul!"

    else:
        reply = "Sorry, I don't understand..."
    sentence_reply = {
                        "sentence":sentence,
                        "reply":reply
                    }
                    
    return sentence_reply