import random
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
    lines_list.close()

"""prints the lines of the poem in random order"""
def random_list(lines_list):
   lines_list = open('/Users/merissabridgeman/dev/courses/CS 1.0/poetry/poem.txt').readlines()
   for line in lines_list:
        line = random.randrange(len(lines_list))
        random_order = str(line + 1)+ " " + lines_list[line]
        print (random_order)
   lines_list.close()
        
"""will print the lines in a custom order"""
def even_odd_lines(lines_list):
   lines_list = open('/Users/merissabridgeman/dev/courses/CS 1.0/poetry/poem.txt').readlines()
   print("you're in the custom function")
  
   for line in lines_list:
       if i % 2 == 0:
          print (line)
       i += 1
   lines_list.close()

