def Basicchatbot (input):
        if input =="hello":
            return "Hi !"
        elif input =="how are you":
            return "I'm fine,thanks !"
        elif input =="bye":
            return "Goodbye !"
        else :
            return("sorry, I don't understand")
       
print ("chatbot: Hi ! I am rule based chatbot")
while True :
    user = input("You:  ").lower()
    output = Basicchatbot( user)
    print("chatbot:",output)
    if user == "bye":
        break