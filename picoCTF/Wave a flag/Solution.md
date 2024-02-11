# Obedient Cat
- Tags: picoCTF 2021, General Skills
- Author: SYREAL
- Description: Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...
- Link to the question: https://play.picoctf.org/practice/challenge/170

# Solution
- To solve this question you need to download the following file and open it. The output will be:
```
Hello user! Pass me a -h to learn what I can do!
```
- So, we use this file with that flag:
```
./warm -h
```
- After that we will get the flag.

```
picoCTF{b1scu1ts_4nd_gr4vy_30e77291}
```
