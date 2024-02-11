import base64

def base64_decode(encoded_text):
    padding = '=' * (4 - len(encoded_text) % 4)
    encoded_text += padding
    try:
        decoded_bytes = base64.b64decode(encoded_text)
        return decoded_bytes
    except Exception as e:
        print(f"Error decoding Base64: {e}")
        return None

def bytes_to_text(decoded_bytes, encodings=['utf-8', 'latin-1']):
    for encoding in encodings:
        try:
            text = decoded_bytes.decode(encoding)
            return text
        except Exception as e:
            print(f"Failed to decode using {encoding}: {e}")
            continue
    print("Failed to decode using any specified encoding")
    return None

encoded_text = "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9"
decoded_bytes = base64_decode(encoded_text)

if decoded_bytes is not None:
    print(f"Encoded Text: {encoded_text}")
    print(f"Decoded Bytes: {decoded_bytes}")
    
    decoded_text = bytes_to_text(decoded_bytes)
    
    if decoded_text is not None:
        print(f"Decoded Text: {decoded_text}")
