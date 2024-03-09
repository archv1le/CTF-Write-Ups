# unpackme.py
- Tags: picoCTF 2022, Reverse Engineering, packing
- Author: LT 'SYREAL' JONES
- Description: Can you get the flag? Reverse engineer this Python program.
- Link to the question: https://play.picoctf.org/practice/challenge/314

# Solution
- To solve this task we have to download the Python script that will contain the following code:

```
import base64
from cryptography.fernet import Fernet

payload = b'gAAAAABkzWGO_8MlYpNM0n0o718LL-w9m3rzXvCMRFghMRl6CSZwRD5DJOvN_jc8TFHmHmfiI8HWSu49MyoYKvb5mOGm_Jn4kkhC5fuRiGgmwEpxjh0z72dpi6TaPO2TorksAd2bNLemfTaYPf9qiTn_z9mvCQYV9cFKK9m1SqCSr4qDwHXgkQpm7IJAmtEJqyVUfteFLszyxv5-KXJin5BWf9aDPIskp4AztjsBH1_q9e5FIwIq48H7AaHmR8bdvjcW_ZrvhAIOInm1oM-8DjamKvhh7u3-lA=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
exec(plain.decode())
```

- We see that it encodes the payload with the following key, whuch is a string. We have to decode it and get the flag. For that, let's write a basic Python script to do so:

```
import base64
from cryptography.fernet import Fernet

def decode_payload(payload, key_str):
    key_base64 = base64.b64encode(key_str.encode())
    f = Fernet(key_base64)
    try:
        plain = f.decrypt(payload)
        return plain.decode()
    except Exception as e:
        print(f"Error decoding payload: {e}")
        return None

payload = b'gAAAAABkzWGO_8MlYpNM0n0o718LL-w9m3rzXvCMRFghMRl6CSZwRD5DJOvN_jc8TFHmHmfiI8HWSu49MyoYKvb5mOGm_Jn4kkhC5fuRiGgmwEpxjh0z72dpi6TaPO2TorksAd2bNLemfTaYPf9qiTn_z9mvCQYV9cFKK9m1SqCSr4qDwHXgkQpm7IJAmtEJqyVUfteFLszyxv5-KXJin5BWf9aDPIskp4AztjsBH1_q9e5FIwIq48H7AaHmR8bdvjcW_ZrvhAIOInm1oM-8DjamKvhh7u3-lA=='
key_str = 'correctstaplecorrectstaplecorrec'

result = decode_payload(payload, key_str)
if result:
    print(result)
```

- After executing this code we get this:

```
pw = input('What\'s the password? ')

if pw == 'batteryhorse':
  print('picoCTF{175_chr157m45_5274ff21}')
else:
  print('That password is incorrect.')
``` 

- The flag is above.

```
picoCTF{175_chr157m45_5274ff21}
```
