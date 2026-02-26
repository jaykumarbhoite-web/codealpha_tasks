def run_basic_chatbot() -> None:
    """
    Initializes and runs a continuous rule-based chatbot session.
    Evaluates user input against predefined conditions and returns mapped responses.
    """
    print("System: Chatbot initialized. Type 'bye' to terminate the session.")
    print("-" * 65)
    
    while True:
        try:
            # Capture and sanitize user input
            user_input = input("User: ").strip().lower()
            
            # Evaluate predefined rules
            if user_input == "hello":
                print("Chatbot: Hi!")
                
            elif user_input == "how are you":
                print("Chatbot: I'm fine, thanks!")
                
            elif user_input == "bye":
                print("Chatbot: Goodbye!")
                break 
                
            else:
                print("Chatbot: Command not recognized. Valid inputs: 'hello', 'how are you', 'bye'.")
                
        # Gracefully handle manual interruptions (Ctrl+C)
        except KeyboardInterrupt:
            print("\nSystem: Session terminated abruptly by user. Goodbye!")
            break

# Entry point for the script
if __name__ == "__main__":
    run_basic_chatbot()