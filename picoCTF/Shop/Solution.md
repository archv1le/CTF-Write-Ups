# Shop
- Tags: picoCTF 2021, Reverse Engineering
- Author: THELSHELL
- Description: Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: source. The shop is open for business at nc mercury.picoctf.net 24851.
- Link to the question: https://play.picoctf.org/practice/challenge/134

# Solution
- To solve this question we have to download the file which we have to decompile. But first of all, we can check what the program contains.

```
Welcome to the market!
=====================
You have 40 coins
        Item            Price   Count
(0) Quiet Quiches       10      12
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option: 
```

- We have to obtain to the "Fruitful Flag", which, obviously, contains the flag for the solution. When we try access it, we get a message that we don't have enough money to buy it.

```
Not enough money.
```

- Let's decompile it using Reverse Engineering tools like Ghidra or other. There is a lot of code, I will display the information which is only needed. This is all in "main.menu" function:

```
*(int *)(param_1 + 0xc + iVar3) = iVar2 - *local_70;
uVar1 = *local_6c;
if (param_2 <= uVar1) {
  runtime.panicindex();
  do {
    invalidInstructionException();
  } while( true );
}
iVar2 = uVar1 * 0x10;
param_7 = param_7 - *(int *)(param_1 + 8 + iVar2) * *local_70; // this function is not checking the negative value, so we can exploit it
if (param_5 <= uVar1) {
  runtime.panicindex();
  do {
    invalidInstructionException();
  } while( true );
}
*(int *)(param_4 + 0xc + iVar2) = *local_70 + *(int *)(param_4 + 0xc + iVar2);
if (param_2 < 3) {
  runtime.panicindex();
  do {
    invalidInstructionException();
  } while( true );
}
if (*(int *)(param_1 + 0x2c) != 1) { // here we are getting the flag using the function below which retrieves it
   main.get_flag();
}
```

- After obtaining that information, let's come back to our program and exploit it.

```
Welcome to the market!
=====================
You have 40 coins
        Item            Price   Count
(0) Quiet Quiches       10      12
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option: 
0
How many do you want to buy?
-10
You have 140 coins
        Item            Price   Count
(0) Quiet Quiches       10      22
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option: 
2
How many do you want to buy?
1
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 53 51 50 98 99 100 57 56 125]
```

- After retrieving encoded flag, we have to decode it. This is decimal ASCII values, so, after decoding them we get the flag.

```
picoCTF{b4d_brogrammer_532bcd98}
```
