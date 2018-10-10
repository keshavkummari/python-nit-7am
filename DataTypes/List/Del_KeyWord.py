
#!/usr/bin/python

list1 = ['python', 'linux', 1997, 2000]

print (list1)

print(list(enumerate(list1)))

del list1[2]

print ("After deleting value at index 2 : ", list1)

print(list(enumerate(list1)))


