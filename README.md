### Python Portfolio Project 00

# Code_Converter

Code_Converter is a Python-based tool designed to enable seamless conversions between English text and Morse code. It supports conversions for English alphabets, digits, and some basic punctuation, facilitating a wide range of text to be accurately converted.

## Features

- **Bi-Directional Conversion**: Convert English to Morse code and Morse code to English.
- **Support for Alphabets and Digits**: Handles English alphabets, digits, and selected punctuation.
- **Graceful Error Handling**: If a character or symbol is not present in the dictionary during conversion, the function will not crash but will return an empty string for that symbol.
- **Maintain Word Separation**: When converting back from Morse code to English, the separation between words is maintained.

## How to Use

### Text to Morse Code Conversion

1. **Function**: `text_to_morse(input_text)`
2. Replace `"This is cool!"` with your desired text to test different cases.
3. Ensure the text only includes characters that are keys in the dictionary to avoid errors.

#### Example

```python
print(text_to_morse("This is cool!"))  # - .... .. ... / .. ... / -.-. --- --- .-.. -.-.--
```

### Morse Code to Text Conversion

1. **Function**: `morse_to_text(code)`
2. Separate different letters by a space and different words by ' / '.
3. Only use symbols present in the Morse code dictionary to ensure accurate conversion.

#### Example

```python
print(morse_to_text("- .... .. ... / .. ... / -.-. --- --- .-.. -.-.--"))  # THIS IS COOL!
```

## Dictionaries

This project utilizes two dictionaries to facilitate conversions:

1. `morse_code` for converting English characters to Morse code.
2. `text_code` for converting Morse code to English characters.

Ensure the integrity of these dictionaries for accurate conversion operations.

## Testing

Test the conversion functions with different cases by replacing "This is cool!" with your text or Morse code, ensuring they only contain symbols present in the dictionaries.

### Additional Information
- The conversion from text to Morse code is case-insensitive, and the output from Morse code to text will be in uppercase.
- The `.gitignore` file is set up to avoid committing unnecessary files, enhancing the project's maintainability.
