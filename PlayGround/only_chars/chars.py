# permutations(p[, r]) => r-length tuples, all possible orderings, no repeated elements
# => sample: permutations('ABCD', 2) => result: AB AC AD BA BC BD CA CB CD DA DB DC
#
# add necessaire library to our code
import itertools as it
#
# Getting the possible password words from the user
words = input("type your characters and words separated with space:")
chars = words.replace(' ', '')
chars_list = list(chars)
#
# Getting the possible password range from the user
pass_length = input('What is the range length of the password? example 6-12:')
pass_length_range = pass_length.split('-')
#
# open the pass-list file after the loops to avoide of repetitive action => reduce cpu usage
with open('PlayGround\\test.txt', 'w') as f:
    for i in range(int(pass_length_range[0]), int(pass_length_range[1]) + 1):
#        
# get possible passwords by using itter.permutations function 
        prob_pass_list = list(it.combinations(chars_list, i))
#
# iterate over each pass-list built by 'permutations' function
        for j in range(len(prob_pass_list)):
#
# building our string password by joining probable words in [j] index
            prob_pass_string = ''.join(prob_pass_list[j])
#
# finally should write the password in specific file
            f.write(f"{prob_pass_string} \n")