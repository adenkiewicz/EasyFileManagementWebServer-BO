# EasyFileManagementWebServer-BO
Exploit for Easy File Management Web Server 5.3 on Win7

Based on:
* pwntools
* msfvenom / reverse\_tcp payload

Vulnerable app available at https://www.exploit-db.com/exploits/10374

The original exploit from https://www.exploit-db.com/exploits/33453 uses stack bruteforce technique (2nd byte), but it makes it less reliable and produces crashes.
Another exploit from https://www.exploit-db.com/exploits/33610 uses pretty much the same technique as me, but it looks like completly different steps were found. I don't have to build anything on the stack, so the flow is much simpler.

Bytes at `0x10018A3C` in ImageLoad.dll are used to jump into pretty harmless code block (`0x1001882B`), that does couple pop's, resulting in RET to controlled trampoline, and then shellcode.
