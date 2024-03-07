'''
#reading files
from sys import argv
script, filename = argv
txt = filename
print("here's your file %r:" % filename)
print (txt)
print ("type the filename again:")
file_again = input(">")
txt_again = file_again
print (txt_again)
'''

#reading and writing files
from sys import argv
script, filename = argv
print("we are going to arase %r." % filename)
print("if you dont want, hit CTRL-c)(^c).")
print("if you do want that, hit Return.")
input("?")
print("opening the file...")
target = filename,'w'
print("truncating the file.goodbye")

print("now im goung to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("im going to write these to the file.")


