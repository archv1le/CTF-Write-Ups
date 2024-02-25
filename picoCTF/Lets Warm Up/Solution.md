# Lets Warm Up
- Tags: picoCTF 2019, General Skills
- Author: SANJAY C/DANNY TUNITIS
- Description: If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?
- Link to the question: https://play.picoctf.org/practice/challenge/22

# Solution
- This task is very basic, you just need to use embedded in Linux OS terminal, or use web shell inside the picoCTF website. Type in "python3" and you will see welcome message. Then you can type following command and get the flag.

```
chr(0x70)
```

- The output will be "p", which is the answer to the question.

```
picoCTF{p}
```
