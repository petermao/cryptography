#Input Field
a = raw_input('Input text: ')
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Ceaser Cipher
shift = lambda txt,sft=1:''.join([[ch,chr((ord(ch) - ord(['A','a'][ch.islower()]) + sft)%26+ord(['A','a'][ch.islower()]))][ch.isalpha()] for ch in txt])
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Substitution Cipher

#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Vigenere Cipher

#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Hill Cipher

#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Autokey Cipher

#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Transposition Cipher

#-------------------------------------------------------------------------------------------------------------------------------------------------------
#One Time Pad

#-------------------------------------------------------------------------------------------------------------------------------------------------------
b = raw_input('Encryption or decryption? ')
c = raw_input('What kind of cipher? ')



if b == "encryption":
  if c == "ceaser":
    d = raw_input('What is the shift? ')
    print(shift(a, d))
  else:
    if c == "substitution":
      set
    else:
      if c == "vigenere":
        set
      else:
        if c == "hill":
          set
        else:
          if c == "autokey":
            set
          else:
            if c == "transposition":
              set
            else:
              if c == "one time pad":
                set
else:
  if c == "ceaser":
    for i in range(26):print(shift(a,i))
  else:
    if c == "substitution":
      set
    else:
      if c == "vigenere":
        set
      else:
        if c == "hill":
          set
        else:
          if c == "autokey":
            set
          else:
            if c == "transposition":
              set
            else:
              if c == "one time pad":
                set




