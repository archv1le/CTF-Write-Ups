# information
- Tags: picoCTF 2021, Forensics
- Author: SUSIE
- Description: Files can always be changed in a secret way. Can you find the flag? cat.jpg
- Link to the question: https://play.picoctf.org/practice/challenge/186

# Solution
- To solve this question you need to download the following file and open it in your Bash, or in the picoCTF's Webshell using the following command. It will help us to find the path to the solution:
```
exiftool cat.jpg
```
- ExifTool is a platform-independent Perl library plus a command-line application for reading, writing and editing meta information in a wide variety of files. To read more about it, link: https://exiftool.org/
- So, after entering this command, we get the following information:
```
ExifTool Version Number         : 12.40
File Name                       : cat.jpg
Directory                       : .
File Size                       : 858 KiB
File Modification Date/Time     : 2021:03:15 18:24:46+00:00
File Access Date/Time           : 2024:02:11 13:18:30+00:00
File Inode Change Date/Time     : 2024:02:11 13:18:30+00:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```
- If we look at the License, we see, that this string is encoded in Base64. So, we can write Python script, or use some of the online decoders, like:
- https://www.base64decode.org/
- https://www.base64decode.net/
- After that we get the flag for the solution.

```
picoCTF{the_m3tadata_1s_modified}
```
