# Lab 08
# Ha Linh Tang Tran 

# This program decodes the cypher text given in lab 08

# import module to define string 'cyphertext.cyphertext'
import cyphertext

# create alphabet lists
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
            "J", "K", "L", "M", "N", "O", "P", "Q", "R",
            "S", "T", "U", "V", "W", "X", "Y", "Z", "a",
            "b", "c", "d", "e", 'f', "g", "h", "i", "j",
            "k", "l", "m", "n", "o","p", "q", "r","s",
            "t", "u", "v", "w", "x", "y", "z"]

# make an empty list for all possible shifts
all_possible_shifts = []

# create a for loop to run all possible shifts
for num_shift in range(1, len(alphabet)):

  # make an empty string for shifted text
  s_shifted = ""

  for chr in cyphertext.cyphertext:

    # check if character is in the alphbet lists
    # find chacracter position in alphabet list
    # create new position
    if (chr in alphabet):
      for i in range(len(alphabet)):
        if chr == alphabet[i]:
          new_pos = (i + num_shift) % len(alphabet)
          chr = alphabet[new_pos]
          break

    # add new character to string    
    s_shifted += chr

  # add string to list  
  all_possible_shifts.append(s_shifted)

  # print a sample (10 characters) of all possible shifts
  print("\nSample no.", num_shift,":", s_shifted[0:10])

# ask for choice of shift
user_choice = int(input("\nEnter the shift of your choice (number only): "))

# find the shift chosen in list
s_decoded = all_possible_shifts[user_choice - 1]

# print result coressponding to user's choice
print(s_decoded)
