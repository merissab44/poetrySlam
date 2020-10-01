import random
from random import choice
"""returns the lines inside the txt file"""
def get_file_lines(filename):
    poem_file = "/Users/merissabridgeman/dev/courses/CS 1.0/poetry/poem.txt" # opens file
    infile =  open(poem_file, "r").readlines() # read
    infile.close()
    return infile

"""prints the line number and lines backwards"""
def lines_printed_backwards(lines_list):
    lines_list = open('/Users/merissabridgeman/dev/courses/CS 1.0/poetry/poem.txt').readlines()
    num_lines = len(lines_list) # gets the length of the list
    lines_list = lines_list[:: -1] # reverses the list

    #for loop for the range of lines in the poem list
    for line in range(len(lines_list)):
        reverse = str(num_lines - line) + " " + lines_list[line] #beginning reverses the line numbers
        print (reverse)

"""prints the lines of the poem in random order"""
def random_list(lines_list):
   lines_list = open('/Users/merissabridgeman/dev/courses/CS 1.0/poetry/poem.txt').readlines()
   for line in lines_list:
        line = random.randrange(len(lines_list))
        random_order = str(line + 1)+ " " + lines_list[line]
        print (random_order)
        
"""will print the lines in a custom order"""
def even_lines(lines_list):
   lines_list = open('/Users/merissabridgeman/dev/courses/CS 1.0/poetry/poem.txt').readlines()
      lines_list = open('/Users/merissabridgeman/dev/courses/CS 1.0/poetry/poem.txt').readlines()
   for i in range(len(lines_list)):
      if i % 2 == 0:
         print(i,lines_list[i])

choice = input(""" Please enter from the options below:
               1: read poem backwards
               2: read poem randomly
               3: read even lines then odd """)
if choice == "1":
   print(lines_printed_backwards("poem.txt"))
elif choice == "2":
   random_list("poem.txt")
elif choice == "3":
   even_lines("poem.txt")
 
