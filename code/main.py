# Define the Symbolic Code dictionary
symbolic_code_dict = {
    '@': 'A',
    '#': 'B',
    '$': 'C',
    '%': 'D',
    '&': 'E',
    '!': 'F',
    '*': 'G',
    '?': 'H',
    '+': 'I',
    '=': 'J',
    ':': 'K',
    ';': 'L',
    '~': 'M',
    '^': 'N',
    '/': 'O',
    '(': 'P',
    ')': 'Q',
    '[': 'R',
    ']': 'S',
    '{': 'T',
    '}': 'U',
    '|': 'V',
    '<': 'W',
    '>': 'X',
    '1': 'Y',
    '2': 'Z',
    '3': '0',
    '4': '1',
    '5': '2',
    '6': '3',
    '7': '4',
    '8': '5',
    '9': '6'
}

# Function to encode a message
def encode_message(message):
    encoded_message = []
    for char in message:
        if char in symbolic_code_dict:
            encoded_message.append(symbolic_code_dict[char])
        elif char == ' ':
            encoded_message.append(' ')
    return ''.join(encoded_message)

# Function to decode a message
def decode_message(encoded_message):
    decoded_message = []
    encoded_symbols = encoded_message.split()
    for symbol in encoded_symbols:
        if symbol in symbolic_code_dict.values():
            decoded_message.append([k for k, v in symbolic_code_dict.items() if v == symbol][0])
        elif symbol == ' ':
            decoded_message.append(' ')
    return ''.join(decoded_message)

# Example usage
message = "Dinakar"
encoded_message = encode_message(message)
decoded_message = decode_message(encoded_message)

print("Original Message:", message)
print("Encoded Message:", encoded_message)
print("Decoded Message:", decoded_message)
