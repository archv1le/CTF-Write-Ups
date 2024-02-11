# ARMssembly 0
- Tags: picoCTF 2021, Reverse Engineering
- Author: DYLAN MCGUIRE
- Description: What integer does this program print with arguments 4112417903 and 1169092511? File: chall.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
- Link to the question: https://play.picoctf.org/practice/challenge/160

# Solution
- To solve this question you need to download the following file and open it. There you will see this code:
```
.arch armv8-a
        .file   "chall.c"
        .text
        .align  2
        .global func1
        .type   func1, %function
func1:
        sub     sp, sp, #16
        str     w0, [sp, 12]
        str     w1, [sp, 8]
        ldr     w1, [sp, 12]
        ldr     w0, [sp, 8]
        cmp     w1, w0
        bls     .L2
        ldr     w0, [sp, 12]
        b       .L3
.L2:
        ldr     w0, [sp, 8]
.L3:
        add     sp, sp, 16
        ret
        .size   func1, .-func1
        .section        .rodata
        .align  3
.LC0:
        .string "Result: %ld\n"
        .text
        .align  2
        .global main
        .type   main, %function
main:
        stp     x29, x30, [sp, -48]!
        add     x29, sp, 0
        str     x19, [sp, 16]
        str     w0, [x29, 44]
        str     x1, [x29, 32]
        ldr     x0, [x29, 32]
        add     x0, x0, 8
        ldr     x0, [x0]
        bl      atoi
        mov     w19, w0
        ldr     x0, [x29, 32]
        add     x0, x0, 16
        ldr     x0, [x0]
        bl      atoi
        mov     w1, w0
        mov     w0, w19
        bl      func1
        mov     w1, w0
        adrp    x0, .LC0
        add     x0, x0, :lo12:.LC0
        bl      printf
        mov     w0, 0
        ldr     x19, [sp, 16]
        ldp     x29, x30, [sp], 48
        ret
        .size   main, .-main
        .ident  "GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
        .section        .note.GNU-stack,"",@progbits
```
- This is the Assembly code. We can see there many things going on, like function call, C funtions and many other. We need to translate this code into C programming language to understand it better. So, you can use some online tools to convert ASM code to C, link:
- https://www.codeconvert.ai/assembly-to-c-converter
- Result is:
```
#include <stdio.h>
#include <stdlib.h>

long func1(int a, int b) {
    if (a <= b) {
        return b;
    } else {
        return a;
    }
}

int main(int argc, char *argv[]) {
    int arg1 = atoi(argv[1]);
    int arg2 = atoi(argv[2]);

    int result = func1(arg1 + 8, arg2 + 16);

    printf("Result: %d\n", result);

    return 0;
}
```
- From this code we can obtain the path to solution. If we look at "func1" we can see, that this function takes two integers and compare them. After this, it returns the number. We need this number to get the flag. Now let's convert it to the desired format.
- After it, we get the flag.

```
picoCTF{f66b01ec}
```
