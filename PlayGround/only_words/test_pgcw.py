# product(p, q, … [repeat=1]) => cartesian product, equivalent to a nested for-loop
# => sample: product('ABCD', repeat=2) => result: AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
#
# add necessaire library to our code
import test_service as ts


word_list = list(ts.get_words_from_usr())

start, end = ts.get_pass_range_from_user()

ts.combinations_functions(file_path='PlayGround\\test.txt',
 start_range=start, end_range=end, word_list=word_list)
