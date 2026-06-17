def chatbot():
    print("🤖 Chatbot Started")
    print("Type bye to exit")

    while True:
        user = input("You: ")

        if user.lower() == "hello":
            print("Bot: Hi! Nice to meet you")

        elif user.lower() == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user.lower()=="what is the project title?":
            print("Bot: Basic chatbot")

        elif user.lower() == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand")

chatbot()