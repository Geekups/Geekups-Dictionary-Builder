# import itertools as it

# def combinations_functions(*,file_path, start_range, end_range, word_list):
#     try:
#          # open the pass-list file after the loops to avoide of repetitive action => reduce cpu usage
#         with open(file_path, 'w') as file:
#             for i in range(start_range, end_range + 1):
#                 # get possible passwords by using itter.product function 
#                 prob_pass_list = list(it.combinations(word_list, i))
#                 # iterate over each pass-list built by 'product' function
#                 for j in range(len(prob_pass_list)):
#                     # building our string password by joining probable words in [j] index
#                     prob_pass_string = ''.join(prob_pass_list[j])
#                     # finally should write the password in specific file
#                     file.write(f"{prob_pass_string} \n")
#     except:
#         print("something get fucked! try again or try another service")

import itertools as it

def combinations_functions(*, file_path, start_range, end_range, word_list):
    try:
        # open the pass-list file after the loops to avoid repetitive action => reduce cpu usage
        with open(file_path, 'w') as file:
            # loop over range of lengths
            for i in range(start_range, end_range + 1):
                # use generator expression to build all combinations of length i
                prob_pass_list = (''.join(combination) for combination in it.combinations(word_list, i))
                # write to file in chunks of 1000 lines at a time
                chunk_size = 1000
                for chunk in iter(lambda: list(it.islice(prob_pass_list,chunk_size)), []):
                    file.write('\n'.join(chunk) + '\n')
    except Exception as e:
        print(f"Error: {e}")
        print("Something went wrong! Try again or try another service.")