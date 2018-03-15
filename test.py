list = []

def getInputFromUSer():
    str = raw_input("Enter a string here : ")
    #print str
    ConvertToLowerCase = str.lower()
    #print ConvertToLowerCase
    trimmed = ConvertToLowerCase.replace(" ", "")
    #print trimmed
    for i in trimmed:
        number = ord(i) - 96
        list.append(number)
    print(list)
    sm = sum(list)
    print(sm)

    while sm>9:
        rem = sm % 10
        sm = (sm / 10) + rem
        
    print(sm)

getInputFromUSer()
#def ConvertStringToNumber():

