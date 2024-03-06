# base727
- Tags: crypto
- Author: quin, chatgpt
- Description: none.
- Link to the question: none.

![image](https://github.com/archv1le/CTF-Write-Ups/assets/158765690/ee0cdb66-d1d0-46c9-92d8-325ee849fb6b)
![image](https://github.com/archv1le/CTF-Write-Ups/assets/158765690/536e6cb5-ad25-4929-a591-84f283c25891)

# Solution
- This is a pretty fun challenge that tells you about encryption with 727'th base. There are two files, you should open them. One contains source code, another contains encrypted flag.

```
import binascii

flag = open('flag.txt').read()

def encode_base_727(string):
    base = 727
    encoded_value = 0

    for char in string:
        encoded_value = encoded_value * 256 + ord(char)

    encoded_string = ""
    while encoded_value > 0:
        encoded_string = chr(encoded_value % base) + encoded_string
        encoded_value //= base

    return encoded_string

encoded_string = encode_base_727(flag)
print(binascii.hexlify(encoded_string.encode()))
```

- We have to write an algorithm that will decode encrypted flag. The script will look like that:

```
import binascii

def decode_base_727(encoded_string):
    base = 727
    decoded_value = 0

    for char in encoded_string:
        decoded_value = decoded_value * base + ord(char)

    decoded_string = ""
    while decoded_value > 0:
        decoded_string = chr(decoded_value % 256) + decoded_string
        decoded_value //= 256

    return decoded_string

hex_encoded_string = b'06c3abc49dc4b443ca9d65c8b0c386c4b0c99fc798c2bdc5bccb94c68c37c296ca9ac29ac790c4af7bc585c59d'
encoded_string = binascii.unhexlify(hex_encoded_string).decode()

decoded_string = decode_base_727(encoded_string)
print(decoded_string)
```

- After decoding the string, you will get the flag:

```
osu{wysiwysiwysiywsywiwywsi}
```
