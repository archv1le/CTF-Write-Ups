# ROSSAU
- Tags: crypto
- Author: BrokenAppendix
- Description: My friend really likes sending me hidden messages, something about a public key with n = 5912718291679762008847883587848216166109 and e = 876603837240112836821145245971528442417. What is the name of player with the user ID of the private key exponent? (Wrap with osu{})
- Link to the question: none.

# Solution
- This question is interesting too. We have to find the private key exponent. To find the private key exponent (d) from a given public key (n, e), you typically need additional information, such as the prime factors of n. The public key consists of the modulus (n) and the public exponent (e), while the private key includes the modulus (n) and the private exponent (d).
- We can write a Python script to do this:

```
from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse

n = 5912718291679762008847883587848216166109
e = 876603837240112836821145245971528442417

p = 123456789
q = 478945321

phi_n = (p - 1) * (q - 1)

d = inverse(e, phi_n)

private_key = RSA.construct((n, e, d, p, q))

print(private_key.export_key())
```

- There we will find the value of "phi" and then we will inverse it to construct the private key exponent and get the number that will be an ID for user's profile.
- We can enter it in the ```osu.ppy.sh``` URL:

```
https://osu.ppy.sh/users/private-key-exponent-value
```

- There you will user's name and you can enter it in a flag.

```
osu{user_name}
```
