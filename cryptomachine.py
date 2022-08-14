def CRYPTOCONVERTER():

    keys = 'abcdefghijklmnopqrstuvwxyz !'
    values = keys[-1] + keys[0:-1]
    encrytDict = dict(zip(keys, values))
    decryptDict = dict(zip(values, keys))
    message = input("Enter your secret message: ")
    mode = input("Crypto Mode : Encode(E) OR Decode(D)")
    if mode.upper() == 'E':
        nMessage = ''.join([encrytDict[letter]
                              for letter in message.lower()])
    elif mode.upper() == 'D':
        nMessage = ''.join([decryptDict[letter]
                              for letter in message.lower()])
    else:
        print("Please try again, wrong choice entered")

    return nMessage.capitalize()


print(machine())

def write():
     file=open('MSG.txt','w')
     file.write(message)
     file.close()
def read():
     file=open('MSG.txt','r')
     newmsg=file.readlines()
     print("The message is :",newmsg)
