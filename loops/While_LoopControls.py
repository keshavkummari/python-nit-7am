#valid=True

while True:
    num=input("Enter a digit : ")
    var=str(num)
    if(ord(var) in range(48,58)):
        #valid = False
        #continue
        break
print ("We are out of the while loop")

# range(48,58-1=57)
#0   1   2  3 4 5 6 7 8   9
#48  49  50               57