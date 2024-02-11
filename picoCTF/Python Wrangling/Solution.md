# Python Wrangling
- Tags: picoCTF 2021, General Skills
- Author: SYREAL
- Description: Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?
- Link to the question: https://play.picoctf.org/practice/challenge/166

# Solution
- To solve this question you need to download Python script, password and file with the encrypted flag.
- After that, run the Python script and enter the following:
```
# To run the script
python ende.py
```
- You will see the following message:
```
Usage: ende.py (-e/-d) [file]
```
- Then, run the script again, but now with obtained knowledge about the file usage:
```
python ende.py -d flag.txt.en
```
- Enter password from the downloaded file and get the flag for the solution.

```
picoCTF{4p0110_1n_7h3_h0us3_67c6cc96}
```
