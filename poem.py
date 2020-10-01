"""returns the lines inside the txt file"""
def get_file_lines(filename):
    poem_file = "/Users/merissabridgeman/dev/courses/CS 1.0/poetry/poem.txt" # opens file
    infile =  open(poem_file, "r").readlines() # read
    infile.close()
    return infile
