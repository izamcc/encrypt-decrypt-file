import cryptography
from cryptography.fernet import Fernet


k = Fernet.generate_key()
f = open('key.txt' , 'wb' )
f.write(k)
f.close()

def enc():
    datafile = open('data.txt', 'rb')
    data = datafile.read()

    u = Fernet(k)
    x = u.encrypt(data)

    cipher = open('encdata.txt' , 'wb')
    cipher.write(x)

    datafile.close()
    cipher.close()

def dec():
    cipherfile = open('encdata.txt', 'rb')
    cipher = cipherfile.read()

    u = Fernet(k)
    x = u.decrypt(cipher)

    data = open('decdata.txt' , 'wb')
    data.write(x)

    cipherfile.close()
    data.close()

def insert():
    print('Type Your Data in the data.txt File ')
    print('Answar Y for Yes')
    s= 0
    while s<1:
        x = input('- Done ? : ')
        if x == "Y" or x == 'y':
            enc()
            s=2

i = 0
while i < 1:
    print('Do You Want To :')
    print('     1. Encrypt File')
    print('     2. Decrypt File')
    print('     3. Close The Program')
    choice = input('- ')
    if choice == '1':
        insert()
    elif choice == '2':
        dec()
        print('Your data is at file decdata.txt')
    elif choice == '1':
        print('Thank You & come back soon ')
        i = 2
