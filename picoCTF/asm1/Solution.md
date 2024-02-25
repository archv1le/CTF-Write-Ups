# asm1
- Tags: picoCTF 2019, Reverse Engineering
- Author: SANJAY C
- Description: What does asm1(0x2e0) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source
- Link to the question: https://play.picoctf.org/practice/challenge/20

# Solution
- This task requires your basic knowledge of Assembly language. To understand it, we have to read it line by line. Note that all values in assembly are hexadecimal.

```
<+0>: push   ebp
<+1>: mov    ebp, esp
```

- We know that we are putting 0x2e0 into the stack, which gets pushed into "ebp" and then moved into "esp" on lines 0 and 1. This just means that this value is now in the first position in the stack now at "ebp+0x8". We then face our first condition.

```
<+3>:    cmp    DWORD PTR [ebp+0x8], 0x3fb
<+10>:  jg         0x512 <asm1+37>
```

- We see that we are comparing the first value in the stack (which is 0x2e0) to 0x3fb. The next line tells us what they are being compared for. The "jb" means "jump if greater". Since 0x2e0 is not greater than 0x3fb, we do nothing.

```
<+12>:  cmp    DWORD PTR [ebp+0x8], 0x280
<+19>:  jne       0x50a <asm1+29>
```

- Here we have another comparison, this time between the first value in the stack and 0x2e0. The condition "jne" means "jump if not equal". Since 0x2e0 is obviously not equal to 0x3fb, this is true and we jump to line +29.

```
<+29>:  mov    eax, DWORD PTR [ebp+0x8]
<+32>:  sub     eax, 0xa
<+35>:  jmp     0x529 <asm1+60>
```

- These three lines are simple. The value in the stack is moved to the variable that will be returned "eax". We subtract 0xa from it, so now "eax" is equal to 0x2d6. We then unconditionally "jmp" to line +60.

```
<+60>:  pop    ebp
<+61>:  ret
```

- So, the final value is: 0x2d6. This is our flag.

```
0x2b6
```
