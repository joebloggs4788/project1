import base64


def base64_1():
    # Example binary data (a simple string encoded to bytes)
    data = b"Hello, World!"

    # Encoding the binary data to Base64
    encoded_data = base64.b64encode(data)
    print("Encoded:", encoded_data)
    # data_seq = [ord(x) for x in data]
    # print(" ".join(data_seq))
    # byte_values = [x for x in data]
    # print(byte_values)

    # Decoding the Base64 data back to binary
    decoded_data = base64.b64decode(encoded_data)
    print("Decoded:", decoded_data.decode('utf-8'))

def unicode_1():
    u1 = '\u2598'
    code_point_decimal = ord(u1)
    code_point_hex = hex(ord(u1))
    print(u1,f"{code_point_decimal:06}",code_point_hex,sep='  ')

if __name__ == '__main__':
    unicode_1()

