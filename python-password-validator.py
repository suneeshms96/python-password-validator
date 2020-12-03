digit_count = 0
alpha_count = 0
char_count = 0
lower_count = 0

#we can change password strength requirement here..!
required_digit_count = 5
required_alpha_count = 2
required_char_count = 4
required_lower_count = 2

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



if digit_count >= required_digit_count and alpha_count >= required_alpha_count and char_count >= required_char_count and lower_count >= required_lower_count :

  print ('The password is successfully added for',uname)

else:
  
  print('The password is not valid')
