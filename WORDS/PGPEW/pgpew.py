# permutations(p[, r]) => r-length tuples, all possible orderings, no repeated elements
# => sample: permutations('ABCD', 2) => result: AB AC AD BA BC BD CA CB CD DA DB DC
#
# add necessaire library to our code
import sys
sys.path.append('WORDS\main_Services')

import WORDS.main_Services.common_actions_service as cas
import pgpew_service as pgpews

def start_calculation():
    word_list = cas.get_words_from_usr()
    start, end = cas.get_pass_range_from_user()
    pgpews.permutations_function(file_path='WORDS\PGPEW\pgpew_pass_list.txt', word_list=word_list, start_range=start, end_range=end)