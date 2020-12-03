##For loop
digit_count = 0
alpha_count = 0
char_count = 0
lower_count = 0

uname = input('Enter your username: ')

word = input('Enter a password : ')

for w in str(word):

  if w.isdigit():

    digit_count = digit_count + 1
  
  elif w.isalpha():

    alpha_count = alpha_count + 1

    if w.islower():

      lower_count = lower_count + 1
  
  else:

    char_count = char_count + 1



if digit_count >= 3 and alpha_count >= 2 and char_count >= 4 and lower_count >= 2 :

  print ('The password is successfully added for',uname)

else:
  
  print('The password is not valid')
