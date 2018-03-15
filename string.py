ListOfNumbers = []

def getInputFromUSer(str):
    str = raw_input("Enter a string here : ")
    ConvertToLowerCase = str.lower()
    trimmedString = ConvertToLowerCase.replace(" ", "")
return trimmed

def convertIntoNumber(int)
for i in trimmedString:
    number = ord(i) - 96
    ListOfNumbers.append(number)
    print(ListOfNumbers)
    sumOfAlphabet = sum(ListOfNumbers)
    print(sumOfAlphabet)
return sumOfAlphabet

while sumOfAlphabet>9:
    rem = sumOfAlphabet % 10
    sumOfAlphabet = (sumOfAlphabet / 10) + rem
        
print(sumOfAlphabet)