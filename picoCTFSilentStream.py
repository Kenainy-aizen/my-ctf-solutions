import struct
payload_data = b""
with open("packets.pcap", "rb") as f:
    f.read(24)
    while True:
        header = f.read(16)
        if len(header) < 16 :
            break
        included_length = struct.unpack("<I", header[8:12])[0]
        packet = f.read(included_length)
        if len(packet) > 54:
            payload_data += packet[54:]
decoded = bytes([ (c - 42)%256 for c in payload_data])
with open("recovered_file.jpg", "wb") as out:
    out.write(decoded)
