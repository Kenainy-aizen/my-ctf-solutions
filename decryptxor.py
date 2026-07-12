import sys
#clair=b'picoCTF{fake_flag}'
#resultCypher = bytes.fromhex('235a201d70201548251358110c552f135409')
#print(resultCypher)
#key = bytearray()
#Afor i in range(len(clair)):
#    key.append( clair[i] ^ resultCypher[i % len(resultCypher)])
#print(key.decode())

key = bytearray()

cipherText=sys.argv[1]
secretKey = sys.argv[2].encode()
cipherBytes = bytes.fromhex(cipherText)

for i in range(len(cipherBytes)):
    key.append( cipherBytes[i] ^ secretKey[i % len(secretKey)])

print(key.decode())

