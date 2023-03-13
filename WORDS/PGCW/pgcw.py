# # combinations(p, r) => r-length tuples, in sorted order, no repeated elements
# # this file generate passwords by user words combinations with out replacement
# # => sample:combinations('ABCD', 2) => result: AB AC AD BC BD CD
#
# add necessaire library to our code

import sys

sys.path.append('WORDS\main_Services')

import common_actions_service as cas

sys.path.append('WORDS\PGCW')

import pgcw_service as pgcwms

import os


def start_calculation():
    word_list = list(cas.get_words_from_usr())
    start, end = cas.get_pass_range_from_user()

    default_path = "WORDS\pass_list.txt"
    
    path = r"{}".format(input("please enter a path to save the result (default : WORDS\pass_list.txt ) :"))

    # Use replace() method to remove the double quotes (When there are double quotes, the input is not recognized as a path)
    new_path = path.replace('"', "")

    # Checking the correctness of the entered path

    if os.path.exists(new_path) == True :
        file_path = new_path

    else :
        file_path = default_path
    pgcwms.combinations_functions(file_path=file_path ,
    start_range=start, end_range=end, word_list=word_list)

if __name__ == "__main__" :
    start_calculation()
