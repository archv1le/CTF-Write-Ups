# ASCII FTW
- Tags: picoGym Exclusive, Reverse Engineering
- Author: ABHISHEK AGARWAL
- Description: This program has constructed the flag using hex ascii values. Identify the flag text by disassembling the program. You can download the file from here.
- Link to the question: https://play.picoctf.org/practice/challenge/389

# Solution
- To solve this question you need to download the following file and open it using Ghidra or any other tool you can find.
- Here we can see a call to "main" function:
```
                             //
                             // .text 
                             // SHT_PROGBITS  [0x1080 - 0x12b4]
                             // ram:00101080-ram:001012b4
                             //
                             **************************************************************
                             *                          FUNCTION                          *
                             **************************************************************
                             undefined processEntry _start(undefined8 param_1, undefi
             undefined         AL:1           <RETURN>
             undefined8        RDX:8          param_1
             undefined8        Stack[0x0]:8   param_2
             undefined8        Stack[-0x10]:8 local_10                                XREF[1]:     00101092(*)  
                             _start                                          XREF[5]:     Entry Point(*), 00100018(*), 
                                                                                          00102044, 00102088(*), 
                                                                                          _elfSectionHeaders::00000410(*)  
        00101080 f3 0f 1e fa     ENDBR64
        00101084 31 ed           XOR        EBP,EBP
        00101086 49 89 d1        MOV        R9,param_1
        00101089 5e              POP        RSI
        0010108a 48 89 e2        MOV        param_1,RSP
        0010108d 48 83 e4 f0     AND        RSP,-0x10
        00101091 50              PUSH       RAX
        00101092 54              PUSH       RSP=>local_10
        00101093 4c 8d 05        LEA        R8,[__libc_csu_fini]
                 16 02 00 00
        0010109a 48 8d 0d        LEA        RCX,[__libc_csu_init]
                 9f 01 00 00
        001010a1 48 8d 3d        LEA        RDI,[main]
                 c1 00 00 00
```
- If we go further, we can find multiple calls to "main" function and a lot move statements with the "printf" function.
```
                             **************************************************************
                             *                          FUNCTION                          *
                             **************************************************************
                             undefined __stdcall main(void)
             undefined         AL:1           <RETURN>
             undefined8        Stack[-0x10]:8 local_10                                XREF[2]:     0010117e(W), 
                                                                                                   0010121b(R)  
             undefined1        Stack[-0x1a]:1 local_1a                                XREF[1]:     001011fc(W)  
             undefined1        Stack[-0x1b]:1 local_1b                                XREF[1]:     001011f8(W)  
             undefined1        Stack[-0x1c]:1 local_1c                                XREF[1]:     001011f4(W)  
             undefined1        Stack[-0x1d]:1 local_1d                                XREF[1]:     001011f0(W)  
             undefined1        Stack[-0x1e]:1 local_1e                                XREF[1]:     001011ec(W)  
             undefined1        Stack[-0x1f]:1 local_1f                                XREF[1]:     001011e8(W)  
             undefined1        Stack[-0x20]:1 local_20                                XREF[1]:     001011e4(W)  
             undefined1        Stack[-0x21]:1 local_21                                XREF[1]:     001011e0(W)  
             undefined1        Stack[-0x22]:1 local_22                                XREF[1]:     001011dc(W)  
             undefined1        Stack[-0x23]:1 local_23                                XREF[1]:     001011d8(W)  
             undefined1        Stack[-0x24]:1 local_24                                XREF[1]:     001011d4(W)  
             undefined1        Stack[-0x25]:1 local_25                                XREF[1]:     001011d0(W)  
             undefined1        Stack[-0x26]:1 local_26                                XREF[1]:     001011cc(W)  
             undefined1        Stack[-0x27]:1 local_27                                XREF[1]:     001011c8(W)  
             undefined1        Stack[-0x28]:1 local_28                                XREF[1]:     001011c4(W)  
             undefined1        Stack[-0x29]:1 local_29                                XREF[1]:     001011c0(W)  
             undefined1        Stack[-0x2a]:1 local_2a                                XREF[1]:     001011bc(W)  
             undefined1        Stack[-0x2b]:1 local_2b                                XREF[1]:     001011b8(W)  
             undefined1        Stack[-0x2c]:1 local_2c                                XREF[1]:     001011b4(W)  
             undefined1        Stack[-0x2d]:1 local_2d                                XREF[1]:     001011b0(W)  
             undefined1        Stack[-0x2e]:1 local_2e                                XREF[1]:     001011ac(W)  
             undefined1        Stack[-0x2f]:1 local_2f                                XREF[1]:     001011a8(W)  
             undefined1        Stack[-0x30]:1 local_30                                XREF[1]:     001011a4(W)  
             undefined1        Stack[-0x31]:1 local_31                                XREF[1]:     001011a0(W)  
             undefined1        Stack[-0x32]:1 local_32                                XREF[1]:     0010119c(W)  
             undefined1        Stack[-0x33]:1 local_33                                XREF[1]:     00101198(W)  
             undefined1        Stack[-0x34]:1 local_34                                XREF[1]:     00101194(W)  
             undefined1        Stack[-0x35]:1 local_35                                XREF[1]:     00101190(W)  
             undefined1        Stack[-0x36]:1 local_36                                XREF[1]:     0010118c(W)  
             undefined1        Stack[-0x37]:1 local_37                                XREF[1]:     00101188(W)  
             undefined1        Stack[-0x38]:1 local_38                                XREF[2]:     00101184(W), 
                                                                                                   00101200(R)  
                             main                                            XREF[4]:     Entry Point(*), 
                                                                                          _start:001010a1(*), 0010204c, 
                                                                                          001020f8(*)  
        00101169 f3 0f 1e fa     ENDBR64
        0010116d 55              PUSH       RBP
        0010116e 48 89 e5        MOV        RBP,RSP
        00101171 48 83 ec 30     SUB        RSP,0x30
        00101175 64 48 8b        MOV        RAX,qword ptr FS:[0x28]
                 04 25 28 
                 00 00 00
        0010117e 48 89 45 f8     MOV        qword ptr [RBP + local_10],RAX
        00101182 31 c0           XOR        EAX,EAX
        00101184 c6 45 d0 70     MOV        byte ptr [RBP + local_38],0x70
        00101188 c6 45 d1 69     MOV        byte ptr [RBP + local_37],0x69
        0010118c c6 45 d2 63     MOV        byte ptr [RBP + local_36],0x63
        00101190 c6 45 d3 6f     MOV        byte ptr [RBP + local_35],0x6f
        00101194 c6 45 d4 43     MOV        byte ptr [RBP + local_34],0x43
        00101198 c6 45 d5 54     MOV        byte ptr [RBP + local_33],0x54
        0010119c c6 45 d6 46     MOV        byte ptr [RBP + local_32],0x46
        001011a0 c6 45 d7 7b     MOV        byte ptr [RBP + local_31],0x7b
        001011a4 c6 45 d8 41     MOV        byte ptr [RBP + local_30],0x41
        001011a8 c6 45 d9 53     MOV        byte ptr [RBP + local_2f],0x53
        001011ac c6 45 da 43     MOV        byte ptr [RBP + local_2e],0x43
        001011b0 c6 45 db 49     MOV        byte ptr [RBP + local_2d],0x49
        001011b4 c6 45 dc 49     MOV        byte ptr [RBP + local_2c],0x49
        001011b8 c6 45 dd 5f     MOV        byte ptr [RBP + local_2b],0x5f
        001011bc c6 45 de 49     MOV        byte ptr [RBP + local_2a],0x49
        001011c0 c6 45 df 53     MOV        byte ptr [RBP + local_29],0x53
        001011c4 c6 45 e0 5f     MOV        byte ptr [RBP + local_28],0x5f
        001011c8 c6 45 e1 45     MOV        byte ptr [RBP + local_27],0x45
        001011cc c6 45 e2 41     MOV        byte ptr [RBP + local_26],0x41
        001011d0 c6 45 e3 53     MOV        byte ptr [RBP + local_25],0x53
        001011d4 c6 45 e4 59     MOV        byte ptr [RBP + local_24],0x59
        001011d8 c6 45 e5 5f     MOV        byte ptr [RBP + local_23],0x5f
        001011dc c6 45 e6 38     MOV        byte ptr [RBP + local_22],0x38
        001011e0 c6 45 e7 39     MOV        byte ptr [RBP + local_21],0x39
        001011e4 c6 45 e8 36     MOV        byte ptr [RBP + local_20],0x36
        001011e8 c6 45 e9 30     MOV        byte ptr [RBP + local_1f],0x30
        001011ec c6 45 ea 46     MOV        byte ptr [RBP + local_1e],0x46
        001011f0 c6 45 eb 30     MOV        byte ptr [RBP + local_1d],0x30
        001011f4 c6 45 ec 41     MOV        byte ptr [RBP + local_1c],0x41
        001011f8 c6 45 ed 46     MOV        byte ptr [RBP + local_1b],0x46
        001011fc c6 45 ee 7d     MOV        byte ptr [RBP + local_1a],0x7d
        00101200 0f b6 45 d0     MOVZX      EAX,byte ptr [RBP + local_38]
        00101204 0f be c0        MOVSX      EAX,AL
        00101207 89 c6           MOV        ESI,EAX
        00101209 48 8d 3d        LEA        RDI,[s_The_flag_starts_with_%x_00102004]         = "The flag starts with %x\n"
                 f4 0d 00 00
```
- We can automate the process using Ghidra's script manager. Let's write some code on Python:
```
from ghidra.program.model.mem import MemoryAccessException

start_addr = currentProgram.getAddressFactory().getAddress("00101184")
end_addr = currentProgram.getAddressFactory().getAddress("001011fc")

byte_list = []


current_addr = start_addr
while current_addr <= end_addr:
	instruction = getInstructionAt(current_addr)
	if instruction is not None:
		
		operand = instruction.getOpObjects(1)[0] # get second operand
		byte_val = operand.getValue() & 0xFF # convert to unsigned byte
		byte_list.append(byte_val)
                
       
        current_addr = current_addr.next()

flag = list(map(chr, byte_list))
print("Flag:", "".join(flag))
```
- After that, we will see our flag for the solution below the decompiled code.

```
picoCTF{ASCII_IS_EASY_8960F0AF}
```
