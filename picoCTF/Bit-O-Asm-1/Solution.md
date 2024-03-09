# Bit-O-Asm-1
- Tags: picoGym Exclusive, Reverse Engineering, x86_64
- Author: LT 'SYREAL' JONES
- Description: Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}. Download the assembly dump here.
- Link to the question: https://play.picoctf.org/practice/challenge/391

# Solution
- To solve this question you need to download the following file and open it. In there you will find the following Assembly code.

```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x4],edi
<+11>:    mov    QWORD PTR [rbp-0x10],rsi
<+15>:    mov    eax,0x30
<+20>:    pop    rbp
<+21>:    ret
```

- We have to find the value of the "eax" register. We see that it contains 0x30 hexadecimal value. Convert it and submit to picoCTF.

```
picoCTF{48}
```
