# Word Counter Program

# Function to count the words in the text
def count_words(text):
    """
    Function to count words in a given string.
    Words are assumed to be separated by spaces.
    """
    words = text.split()  # Split the text by spaces
    return len(words)

# Main program logic
def main():
    # Display a welcome message
    print("Welcome to the Word Counter Program!")
    
    # Prompt the user to input a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ").strip()
    
    # Error handling for empty input
    if not user_input:
        print("Error: You entered an empty string. Please provide valid input.")
        return  # Exit the program if input is invalid

    # Call the count_words function
    word_count = count_words(user_input)
    
    # Display the word count result
    print(f"The total number of words is: {word_count}")

# Ensure the program runs only when executed directly
if __name__ == "__main__":
    main()
