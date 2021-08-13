# Python script to clean unnecessary data from Zoom log files

##Steps-
##01. Install Pandas using pip
##02. Identify the columns to be removed and read the data to a data frame
##03. Write the modified data frame to a new csv file





##import pandas as pd
##
##columns_to_be_removed = ['User Email']
##data = pd.read_csv("participants_93924757878.csv").drop(columns_to_be_removed, axis = 'columns')
##
##data.to_csv('masked.csv', index=False)


#Python script to mask a particular field

##Steps-
##01. Install cryptography using pip
##02. Identify the columns to be encrypted and read the data to a data frame
##03. Write the modified data frame to a new csv file

from cryptography.fernet import Fernet
import pandas as pd

data = pd.read_csv("participants_96141800381.csv")
print(data.columns[0], data.columns[1])

##for i in range (len(data.index)):
##    print(data[data.columns[0]][i], data[data.columns[1]][i])
##
data = data.fillna(" ")    
##
##for i in range (len(data.index)):
##    print(data[data.columns[0]][i], data[data.columns[1]][i])
    
key = Fernet.generate_key()
print(key)
fernet = Fernet(key)
print(fernet)
for i in range (len(data.index)):
    data[data.columns[0]][i] = fernet.encrypt(data[data.columns[0]][i].encode())
    data[data.columns[0]][i] = data[data.columns[0]][i].decode()

    data[data.columns[1]][i] = fernet.encrypt(data[data.columns[1]][i].encode())
    data[data.columns[1]][i] = data[data.columns[1]][i].decode()
print(data)    
data.to_csv('encrypted_01.csv', index=False)

data_encrypted = pd.read_csv("encrypted_01.csv")
print(data_encrypted.columns[0], data_encrypted.columns[1])
for i in range (len(data_encrypted.index)):
    data_encrypted[data_encrypted.columns[0]][i] = fernet.decrypt(data_encrypted[data_encrypted.columns[0]][i].encode())
    data_encrypted[data_encrypted.columns[0]][i] = data_encrypted[data_encrypted.columns[0]][i].decode()

    data_encrypted[data_encrypted.columns[1]][i] = fernet.decrypt(data_encrypted[data_encrypted.columns[1]][i].encode())
    data_encrypted[data_encrypted.columns[1]][i] = data_encrypted[data_encrypted.columns[1]][i].decode()
print(data_encrypted)    
data_encrypted.to_csv('decrypted_01.csv', index=False)


### generate a key for encryptio and decryption
### You can use fernet to generate
### the key or use random key generator
### here I'm using fernet to generate key
##
##key = Fernet.generate_key()
##
### Instance the Fernet class with the key
##
##fernet = Fernet(key)
##
### then use the Fernet class instance
### to encrypt the string string must must
### be encoded to byte string before encryption
##encMessage = fernet.encrypt(message.encode())
##
##print("original string: ", message)
##print("encrypted string: ", encMessage)
##
### decrypt the encrypted string with the
### Fernet instance of the key,
### that was used for encrypting the string
### encoded byte string is returned by decrypt method,
### so decode it to string with decode methos
##decMessage = fernet.decrypt(encMessage).decode()
##
##print("decrypted string: ", decMessage)
##
