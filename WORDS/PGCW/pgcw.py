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


def start_calculation():
    word_list = list(cas.get_words_from_usr())
    start, end = cas.get_pass_range_from_user()
    pgcwms.combinations_functions(file_path="WORDS\pass_list.txt" ,
    start_range=start, end_range=end, word_list=word_list)
