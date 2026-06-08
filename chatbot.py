def chatbot():
    print("Welcome to basic chatbot")
    print("Type 'bye' to exit")

    while True:
        user = input("You:").lower()
        if user=="hello":
            print("Bot: Hi!")
        elif user == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user == "what is your name":
            print("Bot: I am a simple chatbot.")
        elif user == "age":
            print("Bot: I don't have an age. I am a computer program.")
        elif user== "who created you":
            print("Bot: I was created by Swathi as a python internship  project.")
        elif user == "what can you do":
            print("Bot: I can answer a simple predefined questions.")
        elif user == "thank you":
            print("Bot: You're welcome!")
        elif user == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand.")
chatbot()