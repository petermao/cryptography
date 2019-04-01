import datetime
import re
import sys

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

frequencies = {}

args = sys.argv

def usage():
    print("Usage: (python version) ngramFY.py <file>")

if len(args) != 2:
    usage()
    exit()

try:
    fp = open(args[1]) # read mode is default
except FileNotFoundError:
    print("Invalid file!")
    usage()
    exit()

content = fp.read()
fp.close()

# perhaps somewhat crude method of stripping newlines and spaces
content = content.replace("\n", "").replace("\r", "").replace(" ", "")

if not content.isalpha():
    print("Your file must contain only alphabetical characters.")
    exit()

c_len = len(content)

content = content.upper() # standardize case

for letter in abc:
    frequencies[letter] = 0

for char in content:
    ind = abc.find(char)

    frequencies[abc[ind]] += 1

half_c_len = c_len // 2

for n_to_count in range(0, half_c_len + 1):
    print("Counting strings of length", n_to_count)
    for ind in range(0, c_len - (n_to_count - 1)):
        string_to_count = content[ind:ind + n_to_count + 1]

        matches = re.findall(string_to_count, content)
    
        frequencies[string_to_count] = len(matches)

fname = "ngram-results-"

date = datetime.date.today()
fname += str(date.year) + "-" + str(date.month) + "-" + str(date.day)

t = datetime.datetime.time(datetime.datetime.now())
fname += "-" + str(t.hour) + "-" + str(t.minute) + "-" + str(t.second)

fname += ".txt"

try:
    fp = open(fname, "x")
    fp.close()
except FileExistsError:
    print("Output file", fname, "already exisits.")
    exit()

with open(fname, "w") as fp:
    fp.write(str(frequencies))

print("Output written to", fname, "in JSON/Python dictionary format.")
