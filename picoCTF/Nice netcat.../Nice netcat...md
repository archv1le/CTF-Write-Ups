# Nice netcat...
- Tags: picoCTF 2021, General Skills
- Author: SYREAL
- Description: There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 49039, but it doesn't speak English...
- Link to the question: https://play.picoctf.org/practice/challenge/156

# Solution
- To solve this question you need to went through the link and see the following numbers:
```
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
51 
100 
56 
52 
101 
100 
99 
56 
125 
10
```
- This is the ASCII symbols, which contains our flag to solve the question. Decode it using Python script, or use some online resources:
- https://www.duplichecker.com/ascii-to-text.php
- https://codebeautify.org/ascii-to-text
- After this we will get the flag for the solution.

```
picoCTF{g00d_k1tty!_n1c3_k1tty!_9b3b7392}
```
