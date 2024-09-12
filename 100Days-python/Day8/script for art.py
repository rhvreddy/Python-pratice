def get_letter_art(letter):
    # Define the block letters as dictionaries
    letters = {
        'H': ["H   H", "H   H", "HHHHH", "H   H", "H   H"],
        'A': [" AAAAA", "A   A", "AAAAA", "A   A", "A   A"],
        'R': ["RRRR", "R   R", "RRRR", "R  R", "R   R"],
        'S': ["SSSSS", "S", "SSSSS", "    S", "SSSSS"],
        'D': ["DDDD", "D   D", "D   D", "D   D", "DDDD"],
        'Y': ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  "],
        'E': ["EEEEE", "E", "EEE", "E", "EEEEE"],
        'L': ["L", "L", "L", "L", "LLLLL"],
        # Add more letters as needed
    }

    # Return the letter art if it exists, otherwise return blank spaces
    return letters.get(letter.upper(), ["     ", "     ", "     ", "     ", "     "])


def generate_art(name):
    # Split the name into its characters
    name = name.upper()

    # Initialize a list to hold the rows of the ASCII art
    art_rows = ["", "", "", "", ""]

    # Iterate over each character and add its ASCII art to the appropriate row
    for char in name:
        char_art = get_letter_art(char)
        for i in range(5):  # Each letter has 5 rows
            art_rows[i] += char_art[i] + "  "  # Add spacing between letters

    # Print the final ASCII art
    for row in art_rows:
        print(row)


# Get input from the user
name_input = input("Enter a name: ")

# Generate and display the ASCII art
generate_art(name_input)
