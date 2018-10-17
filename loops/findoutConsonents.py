#!/usr/bin/python

count=0

name=input("Enter your name to find out No.Of Consonants in your name : ")

for letter in name:
    if (letter in ['B','C','D','F','G','H']):
        count=count+1
print ("Your name contains",count,"Consonants in your name")

"""
#!/usr/bin/python

count=0

name=input("Enter your name to find out No.Of Consonants in your name : ")

for letter in name:
    if (letter in ['B','b','C','c','D','d','F','f','G','g','H','h','J','j','K','k','L','l','M','m','N','n','P','p',
'Q','q','R','r','S','s','T','t','V','v','W','w','X','x','Y','y','Z','z']):
        count=count+1
print ("Your name contains",count,"Consonants in your name")
"""