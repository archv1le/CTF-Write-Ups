# caesar
- Tags: picoCTF 2019, Cryptography
- Author: SANJAY C/DANIEL TUNITIS
- Description: Decrypt this message.
- Link to the question: https://play.picoctf.org/practice/challenge/64

# Solution
- To solve this task, firstly, you need to download the file and open it. Inside you will find the following string:

```
picoCTF{ynkooejcpdanqxeykjrbdofgkq}
```

- Since we don't have any idea what is the shift value, we will use a brute-force approach and go for every possible character in the alphabet. Let's use this Python script:

```
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
```

- There will be a lot of strings that will make no sense to you, so try and find that one, that will have some meaningful words in it. After searching, you will get the flag.

```
picoCTF{crossingtherubiconvfhsjkou}
```
