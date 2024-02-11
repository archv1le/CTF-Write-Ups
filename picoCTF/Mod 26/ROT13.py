def rot13_decode(text):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 13 if char.islower() else -13
            result += chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
        else:
            result += char
    return result

encoded_text = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}"
decoded_text = rot13_decode(encoded_text)
print(f"Encoded Text: {encoded_text}")
print(f"Decoded Text: {decoded_text}")
