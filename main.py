import socket
import math
import base64
import time

dict1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
         'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
         'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
         'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
         'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

# Dictionary to lookup alphabets
# corresponding to the index after shift
dict2 = {0: 'Z', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
         6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
         11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
         16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
         21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y'}
def encrypt(message, shift):
    cipher = ''
    for letter in message:
        # checking for space
        if (letter != ' '):
            # looks up the dictionary and
            # adds the shift to the index
            num = (dict1[letter] + shift) % 26
            # looks up the second dictionary for
            # the shifted alphabets and adds them
            cipher += dict2[num]
        else:
            # adds space
            cipher += ' '

    return cipher


# Function to decrypt the string
# according to the shift provided
def decrypt(message, shift):
    decipher = ''
    for letter in message:
        # checks for space
        if (letter != ' '):
            # looks up the dictionary and
            # subtracts the shift to the index
            num = (dict1[letter] - shift + 26) % 26
            # looks up the second dictionary for the
            # shifted alphabets and adds them
            decipher += dict2[num]
        else:
            # adds space
            decipher += ' '

    return decipher
channel = "#root-me_challenge"
port = 6667
server = "irc.root-me.org"
nickname = "xtz1"
num = ""
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))
irc.send(bytes("NICK " + nickname + "\n", "UTF-8"))
print(irc.recv(4096).decode("UTF8"))
irc.send(bytes("USER " + nickname + "  0 * :...", "UTF-8"))
print(irc.recv(4096).decode("UTF8"))
irc.send(bytes("MODE "+channel+"+i\n","UTF8"))
print(irc.recv(4096).decode("UTF8"))
irc.send(bytes("JOIN " + channel + "\n", "UTF-8"))
print(irc.recv(4096).decode("UTF8"))
irc.send(bytes("PRIVMSG Candy :!ep1\n","UTF8"))
print(irc.recv(4096).decode("UTF8"))
while 1:
    str=irc.recv(4096).decode("UTF8")
    print(str,"")
    i=str.find('PRIVMSG xtz1')
    if i != -1:
        #found
        num = str[i+14:]
        break
lst = [int(s) for s in num.split() if s.isdigit()]
result = round(math.sqrt(lst[0])*lst[1], 2)
ans = "PRIVMSG Candy :!ep1 -rep "+repr(result)+"\n"
irc.send(bytes(ans,"UTF8"))
str = irc.recv(4096).decode("UTF8")
print(str)
irc.send(bytes("PRIVMSG Candy :!ep2\n","UTF8"))
str = irc.recv(4096).decode("UTF8")
print(str)
i=str.find('PRIVMSG xtz1')
i=i+14
result = ""
while 1:
    if str[i] == '\n':
        break
    result += str[i]
    i+=1
ans = "PRIVMSG Candy :!ep2 -rep "
result1 = base64.b64decode(result)
print(result1.decode("UTF8"))
irc.send(bytes(ans,"UTF8")+result1+bytes("\n","UTF8"))
print(irc.recv(4096).decode("UTF8"))
irc.send(bytes("PRIVMSG Candy :!ep3\n","UTF8"))
result = ''
while 1:
    str=irc.recv(4096).decode("UTF8")
    i = str.find('PRIVMSG xtz1')
    print(str,"")