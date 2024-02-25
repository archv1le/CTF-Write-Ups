def decryptor(key, cipher):
    text = ""
    for character in cipher:
        newCharacter = ord(character) - key
        if newCharacter < ord("a"):
            newCharacter = newCharacter + 26
        text += chr(newCharacter)
    return text

cipher = "ynkooejcpdanqxeykjrbdofgkq"

for index in range(1, 26):
    text = decryptor(index, cipher)
    print("Key is: ", index, "text is: ", text)
