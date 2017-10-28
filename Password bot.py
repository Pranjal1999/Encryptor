import string
print "Welcome to the Password bot. This script is written by Pranjal Shinde."
print  string.punctuation + string.ascii_letters + string.digits
na = raw_input("Please enter a word that is 8 characters long: ")
number = raw_input("Please enter a numerical value here: ")
chars =  string.punctuation
def string_repetition():
  x = 1 
  while x < 11:
    print "Generating password. Please be patient...."
    x += 1
if len(number) > 0 and len(na) > 0:
  print "Everything is correct. Working...."
  first_letter = na[0]
  third_letter = na[2]
  third_letter = third_letter.upper()
  rest = na[1:len(na)]
  string_punc = string.punctuation
  string_punc = string_punc[4]
  string_punc1 = string.punctuation[5]
  generatedpassword = number + string_punc1 + first_letter + string_punc + rest + third_letter
  string_repetition()
  print generatedpassword

else:
  print "Something was wrong. Please try again. Peace!!"
