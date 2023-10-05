import datetime

# Define a function for the chatbot's responses
def ai_assistant_bot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Greet the user
    if any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
        return "Hello! How can I assist you today?"

    # Respond to weather-related queries
    elif "weather" in user_input:
        return "I'm sorry, I don't have access to real-time weather information."

    # Provide the current time
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."

    # Respond to user emotions
    elif any(emotion in user_input for emotion in ["sad", "happy"]):
        return "I'm here to chat and support you."

    # Handle farewell
    elif any(farewell in user_input for farewell in ["bye", "goodbye", "see you"]):
        return "Goodbye! Feel free to come back anytime."

    # If none of the predefined rules match, provide a generic response
    else:
        return "I'm not sure how to respond to that. Please ask me something else."

# Main loop for the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("AIAssistantBot: Goodbye!")
        break
    response = ai_assistant_bot(user_input)
    print("AIAssistantBot:", response)
