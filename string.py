ListOfNumbers = []
sumOfAlphabet
def getInputFromUSer():
    str = raw_input("Enter a string here : ")
    ConvertToLowerCase = str.lower()
    trimmedString = ConvertToLowerCase.replace(" ", "")

def convertIntoNumber():
    for i in trimmedString:
        number = ord(i) - 96
        ListOfNumbers.append(number)
        print(ListOfNumbers)
        sumOfAlphabet = 0
        sumOfAlphabet = sum(ListOfNumbers)
        print(sumOfAlphabet)
    while sumOfAlphabet>9:
        rem = sumOfAlphabet % 10
        sumOfAlphabet = (sumOfAlphabet / 10) + rem    
        print(sumOfAlphabet)
