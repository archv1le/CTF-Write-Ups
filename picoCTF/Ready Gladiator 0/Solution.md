# Ready Gladiator 0
- Tags: picoCTF 2021, Reverse Engineering, CoreWars
- Author: LT 'SYREAL' JONES
- Description: Can you make a CoreWars warrior that always loses, no ties? Additional details will be available after launching your challenge instance.
- After launching the instance: Can you make a CoreWars warrior that always loses, no ties?Your opponent is the Imp. The source is available here. If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this: nc saturn.picoctf.net 58330 < imp.red
- Link to the question: https://play.picoctf.org/practice/challenge/368

# Solution
- To solve this question you need to launch the instance and download a file.
- Then you need to enter the link and start to write your character's statistics to win Imp.
```
nc saturn.picoctf.net 57711

Submit your warrior: (enter 'end' when done)

Warrior1:
Warrior1:
;redcode
;redcode
;name archv1le
;name archv1le
;assert 2
;assert 2
mov 0, 2
mov 0, 2
end
end
Warrior1:
Warrior1:
;redcode
;name archv1le
;assert 2
mov 0, 2
end

Rounds: 100
Warrior 1 wins: 0
Warrior 2 wins: 100
Ties: 0
You did it!
```
- Then you will instantly get the flag for the solution.

```
picoCTF{h3r0_t0_z3r0_4m1r1gh7_7c030e56}
```
