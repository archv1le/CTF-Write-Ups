# find_the_flag3
- Tags: Web
- Description: The continuation of the annual Find the Flag on the web series. There is a flag hidden somewhere, broken into several parts. The task is to find all the parts and put them together.

# Solution
- When we go the website, we see standard React page placeholder. We should go to the Developer Tools and find there a JS script with the link to some strange URL.
- As we can see in description flag divided in to 3 parts. 1 part: we can find in App.js file. We can see array with route /worker11111.js.

![first-part.jpeg](https://github.com/archv1le/CTF-Write-Ups/assets/158765690/1ec4f3d4-ed9b-4c9f-a004-b2fc180a0f76)

- 2 part: we can find in file PartA.jsx. we can see that it send info to backend and gets some info. We can use Postman to send request to WebSocket.

![second-part.jpeg](https://github.com/archv1le/CTF-Write-Ups/assets/158765690/56040961-9190-4664-8bbb-9d49a87d7565)

- 3 part: we can find in PartB.jsx, as we can see in code it send request to :3001/api/code/part3/ and get some function that gives us flag. To get flag we need 2 arrays that located in /workers.js. Write script in JS and get flag.

![third-part.jpeg](https://github.com/archv1le/CTF-Write-Ups/assets/158765690/460d21ba-a4fd-488f-9a3c-28e9dfea10f9)

- The flag is:

```
VolgaCTF{P4R71_71M3_W3850CK_P4RT3_8PTRPSNI8U}
```
