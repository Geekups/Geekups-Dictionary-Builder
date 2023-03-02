import sys
sys.path.append('WORDS\main_Services')
# from WORDS.PGCW import pgcw
# from WORDS.PGCWRW import pgcwrw
# from WORDS.PGPEW import pgpew
# from WORDS.PGPW import pgpw
import argparse

if __name__ == "__main__":
    # todo ::::: colorize the banner
    print("""
            ================       =======================
            ================       =======================
            ====        ====       ====
            ====        ====       ====
            ================       ====        ============
            ================       ====        ============
            ====                   ====                ====
            ====                   ====                ====
            ====                   ========================
           ======                  ========================

           auther: illegible, dayana, Mohammad Javad Tabari
    """)

    # first we define argument parser as you see, to define and pass our tool args to it
    parser = argparse.ArgumentParser(description="password generator command")
    parser.add_argument("pgcw", help="generating password file using combinations of words (with out replacement)")
    parser.add_argument("pgcwrw", help="generating password file using combinations of words with out replacement")
    parser.add_argument("pgpew", help="generating password file using permutations, all possible orderings, no repeated elements")
    parser.add_argument("pgpw", help="""
    this is a little different look its function, and pass -repeat instead of -range arg when use it
    product(p, q, …. [repeat=1]) => cartesian product, equivalent to a nested for-loop
    => sample: product('ABCD', repeat=2) => result: AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
    """)
    args = parser.parse_args()
    print(args.pgcw)
    print(args.pgcwrw)
    input("press any key to exit ...")