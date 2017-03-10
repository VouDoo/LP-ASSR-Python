import os

print("Please, enter following data to process to 'AsciiArt' :")
t = input("String to transform : ").upper()

chrArray = []
for char in t :
    charAscii = ord(char)
    if charAscii in range(65, 90) :
        chrArray.append(charAscii - 65)
    elif charAscii == 32:
        chrArray.append(None)
    else : 
        chrArray.append(26)

os.chdir("./.")
strArt_file = open(input("'StringArt' file name : "), "r")
l = int(strArt_file.readline())
h = int(strArt_file.readline())

linesResult = []
for i in range(h):
    row = strArt_file.readline()
    line = ''
    for i in chrArray :
        if i is None :
            line += chr(32) * l
        else :
            char_pos = i * l
            line += row[char_pos : char_pos + l]
    linesResult.append(line)

strArt_file.close()

for line in linesResult :
    print(line)

