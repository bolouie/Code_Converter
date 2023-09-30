# Conversion Dictionaries

morse_code = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    ' ': '/', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', '!': '-.-.--'
}

# Reverse the morse code dictionary to decode messages
text_code = {v: k for k, v in morse_code.items()}


def text_to_morse(input_text):
    """Converts English text to Morse code"""
    return ' '.join(morse_code.get(i.upper(), '') for i in input_text)


def morse_to_text(code):
    """Converts Morse code to English text"""
    return ' '.join(text_code.get(i, '') for i in code.split(' '))


# Test Conversion Functions
outer_text = "This is cool!"
morse = text_to_morse(outer_text)
print(morse)  # - .... .. ... / .. ... / -.-. --- --- .-.. -.-.--
print(morse_to_text(morse))  # THIS IS COOL!
