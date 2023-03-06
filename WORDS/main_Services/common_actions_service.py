from time import sleep
# Get the possible password words from the user
def get_words_from_usr():
    try:
        words = input("type your words separated with space:")
        word_list = words.split(' ')
        return word_list
    except:
        print(
            """
            !error!\n
            please follow given structure\n
            type words separated with space
            """
            )
        sleep(2)
        # recall the function
        # تابع بازگشتی
        get_words_from_usr()

# Getting the possible password range from the user
# def get_pass_range_from_user():
#     try:
#         pass_length = input('What is the range length of the password? example 6-12:')
#         pass_length_range = pass_length.split('-')
#         start = int(pass_length_range[0])
#         end = int(pass_length_range[1])
#         if(len(pass_length_range) == 2 and start < end):
#             return start, end
#         print(
#             """
#             !error!\n
#             please follow given structure\n
#             type two number as range numbers with '-' between them\n
#             second number most be bigger than first number
#             """
#             )
#         sleep(2)
#         get_pass_range_from_user()
#     except:
#         print(
#             """
#             !error!\n
#             please follow given structure\n
#             type two number as range numbers with '-' between them\n
#             second number most be bigger than first number\n
#             dont type anything else
#             """
#             )
#         sleep(2)
#         # recall the function
#         # تابع بازگشتی
#         get_pass_range_from_user()

def get_pass_range_from_user():
    while True:
        try:
            pass_length = input('What is the range length of the password? example 6-12:')
            start, end = map(int, pass_length.split('-'))
            if end <= start:
                raise ValueError
            return start, end
        except (ValueError, IndexError):
            print(
                """
                !error!\n
                please follow given structure\n
                type two numbers as range numbers with '-' between them\n
                Second number should be bigger than first number
                """
            )
            sleep(2)



# Get the words or character list and return the list with selected weights of probablity
def get_weight_of_data(data_list):
    data_list_with_wheight = list()

    for data_index in range(len(data_list)):
        data_per_wheight = [str(data_list[data_index])]
        data_wheight = input(f"assaign integer weight to '{data_list[data_index]}' : ")
        data_per_wheight = data_per_wheight * int(data_wheight)
        data_list_with_wheight = data_list_with_wheight + data_per_wheight

