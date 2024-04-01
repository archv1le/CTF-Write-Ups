# Compiled
- Tags: Reverse Engineering, "strings"
- Authors: tryhackme, nerrorsec
- Description: Strings can only help you so far.
- Link to the question: https://tryhackme.com/r/room/compiled

# Solution
- To solve this question you need to download the following file and try to run it.
- First of all, give permission to file to open it. ```chmod``` stands for "change mode", which gives you the ability to give/deny permissions to files. ```+x``` stands for "executable". So when we run this command, the file now can be opened for use.

```
chmod +x ./Compiled-1688545393558.Compiled
./Compiled-1688545393558.Compiled

Password:
```

- Since we do not know the password, we have to somehow find it and bypass the authentication. Let's use "strings" extension in Linux to get all of the meaningful strings in the executable file.

```
strings ./Compiled-1688545393558.Compiled
```

- We will see this:

![strings-compiled.png](https://github.com/archv1le/CTF-Write-Ups/assets/158765690/972db327-2706-48e0-b691-ec6a638386bb)

- Here we see that it has a lot of different strings that comes from the C. Most importantly, we see lines:

```
Password:
DoYouEven%sCTF
__dso_handle
_init
Correct!
Try again!
```

- "_init" is an initialization function that is called when "main()" is called. "$s" is a parameter for "scanf()" C's function to scan user's input. We will see right now, when we reverse engineer a file using Ghidra.

![strings-reversed.png](https://github.com/archv1le/CTF-Write-Ups/assets/158765690/f79fcf60-c1f6-4403-8ceb-a89948959ab5)

- So, we can see that "scanf()" function prints "DoYouEven" and waits for the string to concatinate it. So, it waits for something like:

```
DoYouEvenHello
DoYouEvenWorld
```

- So, down below we see, that the comparison between two strings is used, and if the entered string is equal to "_init", we will get the "Correct!" message.
- When we entered it in the program, we indeed get the success message. This is a password and the answer to the question.

```
DoYouEven_init
```
