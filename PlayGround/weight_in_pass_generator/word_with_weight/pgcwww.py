# permutations(p[, r]) => r-length tuples, all possible orderings, no repeated elements
# => sample: permutations('ABCD', 2) => result: AB AC AD BA BC BD CA CB CD DA DB DC
#
# add necessaire library to our code
import itertools as it
#
# Getting the possible password words from the user
words = input("type your words separated with space:")
word_list = words.split(' ')
word_list_with_wheight = list()

for word in range(len(word_list)):
    words_per_wheight = [str(word_list[word])]
    word_wheight = input(f"assaign integer weight to '{word_list[word]}' : ")
    words_per_wheight = words_per_wheight * int(word_wheight)
    word_list_with_wheight = word_list_with_wheight + words_per_wheight

pass_length = input('What is the range length of the password? example 6-12:')
pass_length_range = pass_length.split('-')

with open('PlayGround\weight_in_pass_generator\word_with_weight\pgcwww.txt', 'w') as f:
    for i in range(int(pass_length_range[0]), int(pass_length_range[1]) + 1):
        prob_pass_list = list(it.combinations(word_list_with_wheight, i))
        for j in range(len(prob_pass_list)):
            prob_pass_string = ''.join(prob_pass_list[j])
            f.write(f"{prob_pass_string} \n")