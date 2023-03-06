import itertools as it
def combinations_with_replacement_function(*,file_path, start_range, end_range, word_list):
    try:
         # open the pass-list file after the loops to avoide of repetitive action => reduce cpu usage
        with open(file_path, 'w') as file:
            for i in range(start_range, end_range + 1):
                # get possible passwords by using itter.product function 
                prob_pass_list = list(it.combinations_with_replacement(word_list, i))
                # iterate over each pass-list built by 'product' function
                for j in range(len(prob_pass_list)):
                    # building our string password by joining probable words in [j] index
                    prob_pass_string = ''.join(prob_pass_list[j])
                    # finally should write the password in specific file
                    file.write(f"{prob_pass_string} \n")
    except:
        print("Something get fucked! Try again or try another service") 


