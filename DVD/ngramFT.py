import re
import sys

frequencies = {}
one_occurrence = []

args = sys.argv


def usage():
    print(
        """
        Usage: (python version) ngramFY.py <file>
        Outputs a dictionary with substrings as keys and counts as values, then a list of substrings that occur only once.
        This can generate a lot of output, so feel free to pipe.
        """
    )


if len(args) != 2:
    usage()
    exit()

try:
    fp = open(args[1])  # read mode is default
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

content = content.upper()  # standardize case

half_c_len = c_len // 2

for n_to_count in range(1, half_c_len + 1):
    for ind in range(0, c_len - (n_to_count - 1)):
        string_to_count = content[ind:ind + n_to_count]

        if string_to_count in frequencies:
            continue

        matches = re.findall(string_to_count, content)

        if len(matches) > 1:
            frequencies[string_to_count] = len(matches)
        else:
            one_occurrence.append(string_to_count)

print(frequencies)
print(one_occurrence)