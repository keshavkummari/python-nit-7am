#!/usr/bin/python

guido = {'Name':'Van', 'Age':60, 'Class':'First'}

print(guido,type(guido),id(guido),len(guido),dict(enumerate(guido)))

print ("guido['Name']: ", guido['Name'])  # Calling Keys

print ("guido['Age']: ", guido['Age'])    # Calling Keys

print ("guido['Class']: ", guido['Class'])# Calling Keys

#del guido['Name'] # remove entry with key 'Name'
#del guido

print ("guido['Name']: ", guido['Name'])
print ("guido['Age']: ", guido['Age'])
print ("guido['Class']: ", guido['Class'])

guido.clear()    # remove all entries in dict

print(guido)

print ("guido['Name']: ", guido['Name'])
print ("guido['Age']: ", guido['Age'])
print ("guido['Class']: ", guido['Class'])

#del guido       # delete entire dictionary
#print(guido)
