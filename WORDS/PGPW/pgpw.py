# product(p, q, … [repeat=1]) => cartesian product, equivalent to a nested for-loop
# => sample: product('ABCD', repeat=2) => result: AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
#
# add necessaire library to our code
import sys
sys.path.append('WORDS\main_Services')

import common_actions_service as cas

sys.path.append('WORDS\PGPW')

import pgpw_service as pgpws

import os


def start_calculation():
    word_list = cas.get_words_from_usr()
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

    pgpws.product_function(file_path= file_path, word_list=word_list, start_range=start, end_range=end)

if __name__ == "__main__" :
    start_calculation()