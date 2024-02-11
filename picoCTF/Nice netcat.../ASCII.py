def ascii_to_text(ascii_string):
    try:
        # Split the string into a list of integers
        ascii_values = list(map(int, ascii_string.split()))
        text = ''.join(chr(value) for value in ascii_values)
        
        return text
    except Exception as e:
        print(f"Error decoding ASCII to text: {e}")
        return None

ascii_string = "112 105 99 111 67 84 70 123 10348 48 100 95 107 49 116 116 121 33 95 110 49 99 51 95 107 49 116 116 121 33 95 51 100 56 52 101 100 99 56 125 10"
decoded_text = ascii_to_text(ascii_string)

if decoded_text is not None:
    print(f"ASCII String: {ascii_string}")
    print(f"Decoded Text: {decoded_text}")
