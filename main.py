import base64
import codecs
import math
import socket
import zlib
import binascii
channel = "#root-me_challenge"
port = 6667
server = "irc.root-me.org"
nickname = "xtz1"
num = ""
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def con():
    global irc
    irc.connect((server, port))
    irc.send(bytes("NICK " + nickname + "\n", "UTF-8"))
    print(irc.recv(4096).decode("UTF8"))
    irc.send(bytes("USER " + nickname + "  0 * :...", "UTF-8"))
    print(irc.recv(4096).decode("UTF8"))
    irc.send(bytes("MODE " + channel + "+i\n", "UTF8"))
    print(irc.recv(4096).decode("UTF8"))
    irc.send(bytes("JOIN " + channel + "\n", "UTF-8"))
    print(irc.recv(4096).decode("UTF8"))


def ch1():
    global irc
    irc.send(bytes("PRIVMSG Candy :!ep1\n", "UTF8"))
    print(irc.recv(4096).decode("UTF8"))
    while 1:
        str = irc.recv(4096).decode("UTF8")
        print(str, "")
        i = str.find('PRIVMSG xtz1')
        if i != -1:
            # found
            num = str[i + 14:]
            break
    lst = [int(s) for s in num.split() if s.isdigit()]
    result = round(math.sqrt(lst[0]) * lst[1], 2)
    ans = "PRIVMSG Candy :!ep1 -rep " + repr(result) + "\n"
    irc.send(bytes(ans, "UTF8"))
    str = irc.recv(4096).decode("UTF8")
    print(str)


def ch2():
    global irc
    irc.send(bytes("PRIVMSG Candy :!ep2\n", "UTF8"))
    str = irc.recv(4096).decode("UTF8")
    print(str)
    i = str.find('PRIVMSG xtz1')
    i = i + 14
    result = ""
    while 1:
        if str[i] == '\n':
            break
        result += str[i]
        i += 1
    ans = "PRIVMSG Candy :!ep2 -rep "
    result1 = base64.b64decode(result)
    print(result1.decode("UTF8"))
    irc.send(bytes(ans, "UTF8") + result1 + bytes("\n", "UTF8"))
    print(irc.recv(4096).decode("UTF8"))


def ch3():
    global irc
    irc.send(bytes("PRIVMSG Candy :!ep3\n", "UTF8"))
    result = ''
    while 1:
        str = irc.recv(4096).decode("UTF8")
        i = str.find('PRIVMSG xtz1 :')
        print(str, "")
        if i != -1:
            # found
            str = str[i + 14:]
            i = 0
            while 1:
                if str[i] == '\n' or str[i] == '\r':
                    break
                result += str[i]
                i = i + 1
            print(result)
            break
    irc.send(bytes("PRIVMSG Candy :!ep3 -rep " + codecs.decode(result, 'rot_13') + "\n", "UTF8"))
    while 1:
        print(irc.recv(4096).decode("UTF8"), "")


def ch4():
    global irc
    irc.send(bytes("PRIVMSG Candy :!ep4\n", "UTF8"))
    result = ''
    while 1:
        str = irc.recv(4096).decode("UTF8")
        i = str.find('PRIVMSG xtz1 :')
        print(str, "")
        if i != -1:
            # found
            str = str[i + 14:]
            i = 0
            while 1:
                if str[i] == '\n' or str[i] == '\r':
                    break
                result += str[i]
                i = i + 1
            print(result)
            break
    result = base64.b64decode(result)
    result = zlib.decompress(result)
    print(result.decode("UTF8"), "")
    irc.send(bytes("PRIVMSG Candy :!ep4 -rep ", "UTF8") + result + bytes("\n", "UTF8"))
    while 1:
        print(irc.recv(4096).decode("UTF8"), "")


if __name__ == "__main__":
    con()
    ch4()
