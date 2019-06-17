import sys

greeting = "Hello,";
punctuation = "!";
arguments = sys.argv;
for kk in range(1, len(arguments)):
    print("%s %s%s"%(greeting, arguments[kk], punctuation))
