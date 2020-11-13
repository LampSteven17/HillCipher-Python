# STEVEN LAMP
# MATH369 FINAL PROJECT
# HILL CIPHER PROGRAM


def main():
    printHeader()

    cipherMatrix = [[0,0],[0,0]]
    cipherText = getCipherTextFromUser()

    getCipherFromUser(cipherMatrix)

    print("ENCRYPTING WITH MATRIX:")
    for i in cipherMatrix:
        print(i)

    encryption = getNewCharsFromHillCipher(cipherMatrix, cipherText)
    print("\nCIPHERTEXT: ",encryption)


    inverseMatrix = inverse(cipherMatrix)

    if (inverseMatrix==cipherMatrix):
        return

    print("\n\n\nDECRYPTING WITH MATRIX:")
    for i in inverseMatrix:
        print(i)

    decryption = getNewCharsFromHillCipher(inverseMatrix,encryption);

    print("\nDECRYPTED MESSAGE: ",decryption)


def inverse(mtx):
    mtr = [[0,0],[0,0]]

    denom = (mtx[0][0]*mtx[1][1]-mtx[0][1]*mtx[1][0])*-1

    mtr[0][0] = (mtx[1][1]*denom)%26
    mtr[1][1] = (mtx[0][0]*denom)%26
    mtr[0][1] = (-1*mtx[0][1]*denom)%26
    mtr[1][0] = (-1*mtx[1][0]*denom)%26

    if(mtr==[[0,0],[0,0]]):
        print("NO INVERSE POSSIBLE CANNOT DECRYPT")
        return mtx

    return mtr



def printHeader():
    print("/**********************************\\")
    print("|HAPPY HARRYS 2x2 HILL CIPHER PRGRM|")
    print("\\**********************************/")
    print("\n")


def getCipherFromUser(mtx):
    validInput = False
    badInput = False

    while(not validInput):
        print("\n(DIGITS 1-26)")
        inputNums = input("Enter 4 NUMS for CIPHER MATRIX: ").split(' ')

        for i in inputNums:
            if(i== '0' or i == ' ' or i == '' or not i.isdigit()):
                badInput=True


        if(len(inputNums)==4 and not badInput):
            validInput = True

        else:
            badInput = False
            print("RECIEVED INVALID INPUT(S): ",inputNums,"\n\n")

    mtx[0][0]=int(inputNums[0])
    mtx[0][1]=int(inputNums[1])
    mtx[1][0]=int(inputNums[2])
    mtx[1][1]=int(inputNums[3])


def getCipherTextFromUser():
    inputText = input("ENTER TEXT TO ENCRYPT: ")

    badChars = ['!','@','#','$','%','^','&','*',' ',';',':','>',',']
    for i in badChars:
        inputText = inputText.replace(i,'')

    inputText = inputText.lower()
    return [inputText[i:i+2] for i in range(0, len(inputText), 2)]



def getNewCharsFromHillCipher(mtx,txt):
    numbers = charsToNums(txt)
    newNums = []

    for i in numbers:
        newNums.append([
        ((mtx[0][0] * i[0]) + (mtx[0][1] * i[1])) % 26,
        ((mtx[1][0] * i[0]) + (mtx[1][1] * i[1])) % 26
        ])

    return numsToChars(newNums)



def charsToNums(txt):
    numArr = []
    numsFormat = []
    for i in txt:
        for j in [char for char in (''.join(i))]:
            numArr.append(ord(j)-96)

    for i in range(0,len(numArr),2):
        try:
            numsFormat.append([numArr[i],numArr[i+1]])
        except IndexError:
            numsFormat.append([numArr[i],numArr[i]])


    return numsFormat


def numsToChars(nums):
    stringy = ""

    for i in nums:
        for j in i:
            stringy+=chr(j+96)



    return stringy.replace('`','z')

if __name__ =="__main__":
    main()
