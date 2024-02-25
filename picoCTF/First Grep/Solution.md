# First Grep
- Tags: picoCTF 2019, General Skills
- Author: ALEX FULTON/DANNY TUNITIS
- Description: Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way.
- Link to the question: https://play.picoctf.org/practice/challenge/85

# Solution
- This task teaches you how to use "grep" command in Linux to get string from the binary file, for example, or something else. So, you need to enter the following command to get the flag from the file. And also, before that you have to download the file first, using "wget" command. Forgot to tell about that earlier.

```
grep -i "picoCTF" file
```

- "-i" is used to ignore case distinctions in patterns and data, second parameter is the string, that we need to get, third is the file, in which "grep" will try to find your entered string. After that, you will get the flag.

```
picoCTF{grep_is_good_to_find_things_f77e0797}
```
