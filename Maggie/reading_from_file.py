fid = open('deleteme.txt', 'r');
data1 = fid.read();
fid.seek(0); # "rewinds" the file
data2 = fid.read().replace(' ','') # removes spaces  from the read-in text.
fid.close();
