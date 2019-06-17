import sys;

print(sys.argv); # prints all of the arguments on the cmd line, each argumant is separated by a space
if (len(sys.argv) > 1):
    print(sys.argv[1]); # prints the FIRST optional argumant
print(len(sys.argv))
