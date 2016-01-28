def encrypt():
        plainText=pairPlainText()
        keyMatrix=generateKeyMatrix()
        cipher=[]
        print("\nPlainText after pairing:\n"+str(plainText))
        print("\nKey Matrix:\n"+str(keyMatrix))
        for i in plainText:
                m1,n1=findPosition(keyMatrix,i[0])
                m2,n2=findPosition(keyMatrix,i[1])
                if(m1==m2):
                        if n1==4:
                                n1=-1
                        if n2==4:
                                n2=-1
                        cipher.append(keyMatrix[m1][n1+1])
                        cipher.append(keyMatrix[m1][n2+1])             
                elif(n1==n2):
                        if m1==4:
                                m1=-1;
                        if m2==4:
                                m2=-1;
                        cipher.append(keyMatrix[m1+1][n1])
                        cipher.append(keyMatrix[m2+1][n2])
                else:
                        cipher.append(keyMatrix[m1][n2])
                        cipher.append(keyMatrix[m2][n1])
        return cipher


def decrypt():    
        cipherText=pairCipherText()
        keyMatrix=generateKeyMatrix()
        plainText=[]
        for i in cipherText:
                m1,n1=findPosition(keyMatrix,i[0])
                m2,n2=findPosition(keyMatrix,i[1])
                if m1==m2:
                        if n1==4:
                                n1=-1
                        if n2==4:
                                n2=-1
                        plainText.append(keyMatrix[m1][n1-1])
                        plainText.append(keyMatrix[m1][n2-1])          
                elif n1==n2:
                        if m1==4:
                                m1=-1
                        if m2==4:
                                m2=-1
                        plainText.append(keyMatrix[m1-1][n1])
                        plainText.append(keyMatrix[m2-1][n2])
                else:
                        plainText.append(keyMatrix[m1][n2])
                        plainText.append(keyMatrix[m2][n1])

        for XVar in range(len(plainText)):
                if "X" in plainText:
                        plainText.remove("X")
        
        output=""
        for i in plainText:
                output+=i
        return output.lower()

def generateKeyMatrix():
        matrix=[]
        for i in key.upper():
                if i not in matrix:
                        matrix.append(i)
        alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ" #omit J
        
        for i in alphabet:
                if i not in matrix:
                        matrix.append(i)        
        

        matrixGroup=[]
        for i in range(5):
                matrixGroup.append('')

        #Divide into 5*5
        matrixGroup[0]=matrix[0:5]
        matrixGroup[1]=matrix[5:10]
        matrixGroup[2]=matrix[10:15]
        matrixGroup[3]=matrix[15:20]
        matrixGroup[4]=matrix[20:25]
        return matrixGroup

#Divide plain text in pairs
def pairPlainText():
        message=[]
        for i in plainText:
                message.append(i)

        #remove extra spces and punctuation marks
        for extraCharacter in range(len(message)):
                if " " in message:
                        message.remove(" ")

                if "." in message:
                        message.remove(".")
  
        #if there is any double letter then replace next letter by 'X'
        position=0
        for i in range(len(message)//2):
                if message[position]==message[position+1]:
                        message.insert(position+1,'X')
                position=position+2

        #If it is odd digit, add an "X" at the end
        if len(message)%2==1:
                message.append("X")

        #Pair Message
        position=0
        pairedMessage=[]
        for i in range(1,len(message)//2+1):
                pairedMessage.append(message[position:position+2])
                position=position+2
        return pairedMessage

#finding position of plain text alphabet in key matrix
def findPosition(keyMatrix,alphabet):
        x=y=0
        for i in range(5):
                for j in range(5):
                        if keyMatrix[i][j]==alphabet.upper():
                                x=i
                                y=j

        return x,y

def createMessage(cipherTextArray):
        cipherText=""
        for i in range(len(cipherTextArray)):
             cipherText=cipherText+cipherTextArray[i]
        return cipherText

def pairCipherText():
        i=0
        newCipherText=[]
        for x in range(len(cipherText)//2):
                newCipherText.append(cipherText[i:i+2])
                i=i+2
        return newCipherText




choice = input('Enter your choice:\n1. Encryption\n2. Decryption\n')
choice=int(choice)

if(choice==1):
        key=input("Please input the key : ")
        plainText=input("Please input the plain text : ")
        encryptedMsg=encrypt()
        print("\nCipher Text:\n"+createMessage(encryptedMsg))
elif(choice==2):
        key=input("Please input the key : ")
        cipherText=input("Please input the cipher text : ")
        decryptedMsg=decrypt()
        print("\nPlain Text:\n"+createMessage(decryptedMsg))
        
