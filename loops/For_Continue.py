
var=input("Enter a string: ")

for letter in var:

    if(letter==' '):
        #continue
        break
        print("Condition Met")
    else:
        print(letter)

print("I am outside of For Loop")