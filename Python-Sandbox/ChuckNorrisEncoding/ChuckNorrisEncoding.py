def encodeMessage(char):
    charEncoded =  bin(ord(char))[2:]
    if len(charEncoded) < 7:
        charEncoded = '0' * (7 - len(charEncoded)) + charEncoded
    return charEncoded

# Initial message
message = input()

# Message to binary format
binToConvert = ''.join(map(encodeMessage, message))

# Message to Chuck Norris encoding
CHUCK_NORRIS_DAT_FUCKIN_ENCODED_MSG = str()
i = 0
while i < len(binToConvert):
    bin = binToConvert[i]
    if bin == '1':
        CHUCK_NORRIS_DAT_FUCKIN_ENCODED_MSG += '0 '
    else:
        CHUCK_NORRIS_DAT_FUCKIN_ENCODED_MSG += '00 '
    while i < len(binToConvert):
        if binToConvert[i] == bin:
            CHUCK_NORRIS_DAT_FUCKIN_ENCODED_MSG += '0'
            i += 1
        else:
            CHUCK_NORRIS_DAT_FUCKIN_ENCODED_MSG += ' '
            break

# Print result
print(CHUCK_NORRIS_DAT_FUCKIN_ENCODED_MSG)
