def chatbot():
    print("Chatbot: Hey! I am your chatbot. You can type 'exit' anytime to quit.")

    while True:
        user_input = input("You: ").lower().strip()

        # Exit condition
        if user_input == "exit" or user_input == "quit" or user_input == "bye" or user_input == "goodbye":
            print("Chatbot: Bye! Have a nice day :)")
            break

        # Greetings
        elif user_input == "hello" or user_input == "hi" or user_input == "hey":
            print("Chatbot: Hello! How can I help you?")

        # Farewell phrases
        elif user_input == "see you later" or user_input == "see ya" or user_input == "catch you later":
            print("Chatbot: Okay, see you later!")

        # Common questions
        elif user_input == "how are you?":
            print("Chatbot: I am fine, thank you! What about you?")

        elif user_input == "what can you do?":
            print("Chatbot: I can chat with you and answer some simple questions about technology and weather.")

        # Technology topic
        elif "technology" in user_input:
            print("Chatbot: Technology is growing fast. AI and computers are very interesting fields.")

        # Weather topic
        elif "weather" in user_input:
            print("Chatbot: I don't have live weather info, but I hope it's good where you are!")

        # Help or options
        elif user_input == "help" or user_input == "what can i say?" or user_input == "options":
            print("Chatbot: You can say hi, ask about technology or weather, or say goodbye to end.")

        # Thank you responses
        elif user_input == "thank you" or user_input == "thanks":
            print("Chatbot: You are welcome!")

        # If input not recognized
        else:
            # Apologize and mention limited capabilities
            print("Chatbot: Sorry, I am not that advanced yet, but I can help you with greetings, technology, weather, and some common questions.")
            print("Chatbot: (For example, you can say 'hello', ask 'how are you?', or ask about 'technology' or 'weather'.)")

if __name__ == "__main__":
    chatbot()
