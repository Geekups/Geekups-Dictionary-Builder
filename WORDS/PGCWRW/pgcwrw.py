# combinations_with_replacement(p, r) => r-length tuples, in sorted order, with repeated elements
# this file generate passwords by user words combinations with replacement
# => sample:combinations_with_replacement('ABCD', 2) => result: AA AB AC AD BB BC BD CC CD DD
#
# add necessaire library to our code
import sys
sys.path.append('WORDS\main_Services')

import common_actions_service as cas

sys.path.append('WORDS\PGCWRW')

import pgcwrw_service as pgcwrws

def start_calculation():
    word_list = cas.get_words_from_usr()
    start, end = cas.get_pass_range_from_user()
    pgcwrws.combinations_with_replacement_function(word_list=word_list, end_range=end, start_range=start, file_path="WORDS\pass_list.txt")

if __name__ == "__main__" :
    start_calculation()