# cryptography

to get an initial copy of these files, run this on your terminal command line:

$ git clone https://github.com/petermao/cryptography.git

or

$ git clone git@github.com:petermao/cryptography.git

Afterwards, you can update the files by running this command from the 
cryptography directory created by the last command:

$ git pull

# make a subdirectory for yourself

For now, to make git easy, don't alter any of these files until you
have copied them into your own subdirectory

In the 'cryptography' directory on your computer (check with the shell
command "pwd"), make a directory for yourself using the "mkdir"
command (or '+' from emacs dired).

For example, I would do:
$ mkdir PHM

then copy the files you need into the subdirectory with "cp"

$ cp *cipher.txt PHM/

move into your subdirectory with "cd"

$ cd PHM
$ pwd
/home/peterm/cryptography/PHM

and back up by cd'ing to ..

$ cd ..
$ pwd
/home/peterm/cryptography

