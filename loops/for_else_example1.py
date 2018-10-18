
for i in range(3):
    username = input("Enter your UserName : ")
    password = input("Enter your PassWord : ")
    if password == 'redhat@123':
        print("You have entered the correct password : ")
        break
else:
    print("3 Incorrect Password attempts")