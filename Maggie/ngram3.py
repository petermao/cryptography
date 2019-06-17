import sys;



fid = open(sys.argv[1], 'r'); #opens whatever sys.argv[1] is. So, if you make sys.argv[1] a file name, that file gets opened. sys.argv[1] is the first hing you write on the command line after the filename.
text = fid.read() #reads the file, so that you can get ngram frequencies
fid.seek(0); # "rewinds" the file
fid.close();


text = text.replace("'", "") #    this section deletes punctuation/
text = text.replace(".", "") # replaces it with nothing, however, does 
text = text.replace(",", "") # not include all punctuation, maybe fix 
text = text.replace("?", "") # that later? (by adding more punctuation)
text = text.replace("!", "")
text = text.replace(" ", "")

print(text) #prints the whole file

definition={} #creates dictionary

for i in range(0,len(text)-1): 
    idx = text[i]+text[i+1]
    definition[idx]=0 #sets dictionary thing count to 0

for i in range(0,len(text)-1):
    idx = text[i]+text[i+1]
    definition[idx]=definition[idx]+1 #adds 1 each time it sees the bigram

for idx in definition.keys():
    print(idx, definition[idx])

idx.sort(reverse = True) #supposed to make frequency of ngrams in descending order (most to least)

#print(idx) #supposed to print that

numbers = [1,3,4,2] #code for reversing number order

numbers.sort(reverse = True) #number.sort - sorting of var number. reverse - reverse order. True - rverse order is true

print(numbers) #now that numbers is reversed, print it
