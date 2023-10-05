# 字节串数据类型 binary
# 字符串转换为字节串：encode() 字节串转换为字符串：decode();

byte01 = b"hello"
print(type(byte01))
print(byte01)

# byte02 = b"非英文字符"
# print(type(byte02))
# print(byte02)

byte03 = "非英文字符".encode()
print(type(byte03))
print(byte03)
print(byte03.decode())

