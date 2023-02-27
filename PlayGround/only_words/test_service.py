import itertools as it

# Get the possible password words from the user
def get_words_from_usr():
    words = input("type your words separated with space:")
    word_list = words.split(' ')
    return word_list

# Getting the possible password range from the user
def get_pass_range_from_user():
    pass_length = input('What is the range length of the password? example 6-12:')
    pass_length_range = pass_length.split('-')
    start = int(pass_length_range[0])
    end = int(pass_length_range[1])
    return start, end

def combinations_functions(*,file_path, start_range, end_range, word_list):
    # open the pass-list file after the loops to avoide of repetitive action => reduce cpu usage
    with open(file_path, 'w') as file:
        for i in range(start_range, end_range + 1):
            # get possible passwords by using itter.product function 
            prob_pass_list = list(it.combinations(word_list, i))
    #
            # iterate over each pass-list built by 'product' function
            for j in range(len(prob_pass_list)):
    #
                # building our string password by joining probable words in [j] index
                prob_pass_string = ''.join(prob_pass_list[j])
    #
                # finally should write the password in specific file
                file.write(f"{prob_pass_string} \n")
    #