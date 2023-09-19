# 20/09/2023 00.31
# I wrote a simple program that converts morse-to-text and text-to-morse out of boredom
# "morse_reversed_dict = {value: key for key, value in morse_code_dict.items()}" this line is new for me
# didn't know how to swap key and values but this simple half an hour project taught me that
# Author: Mustafa Osman Dilmaç 


morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '
}

def text_to_morse(text_input):
    converted_text = ""

    for char in text_input.upper():
        if char in morse_code_dict:
            converted_text +=morse_code_dict[char] + " "
        else:
            converted_text += " "
    return converted_text

def morse_to_text(morse_input):
    converted_morse = ""
    morse_reversed_dict = {value: key for key, value in morse_code_dict.items()}
    morse_input = morse_input.split(" ")

    for morse in morse_input:
        if morse in morse_reversed_dict:
            converted_morse += morse_reversed_dict[morse]
    return converted_morse

def main():
    while 1:
        try:
            choose = int(input("1: Text-to-Morse || 2: Morse-to-Text || 3: Quit\n >> "))
            
            if choose == 1:
                ttm_convert = input("Please provide the text that you want to be converted to Morse Code\n >> ")
                result = text_to_morse(ttm_convert)
                print(f"Morse Code: {result}")
            elif choose == 2:
                mtt_convert = input("Please provide the Morse Code that you want to be converted to Text. \n >> ")
                result = morse_to_text(mtt_convert)
                print(f"Text: {result}")
            elif choose == 3:
                break
            else:
                print("Wrong input.")
        except ValueError as e:
            print("Please provide integer value.")
if __name__ == "__main__":
    main()