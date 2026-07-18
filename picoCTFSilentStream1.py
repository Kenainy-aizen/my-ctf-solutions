with open("captured_data.bin","rb") as encode_data:
    encoded_data = encode_data.read()
decoded_data = bytearray()

for i in encoded_data:
    decoded_data.append((i-42)%256)

with open("output_data","wb") as decode_data:

    decode_data.write(decoded_data)


