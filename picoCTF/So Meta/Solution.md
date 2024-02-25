# So Meta
- Tags: picoCTF 2019, Forensics
- Author: KEVIN COOPER/DANNY
- Description: Find the flag in this picture.
- Link to the question: https://play.picoctf.org/practice/challenge/19

# Solution
- This task requires you to get the flag, which is hidden inside the picture. Download it and then use the tool named "exiftool" to get the metadata from the image.
- "ExifTool is a platform-independent Perl library plus a command-line application for reading, writing and editing meta information in a wide variety of files."

```
exiftool pico_img.png
```

- Then you will see a lot of metadata. Try to look for "author" row and there will be the flag.

```
picoCTF{s0_m3ta_eb36bf44}
```
