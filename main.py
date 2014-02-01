import rigla
import katren
import eclif
import rosta
import comparer
import sys
import common
#import argparse


def main():
    #argparser = argparse.ArgumentParser(description="Compares two csv files and produces a result file.")
    #argparser.add_argument("files", metavar="F", type=open, nargs="+", help="files to process")
    #args = argparser.parse_args()
    #print(args)

    print(sys.argv)

    if len(sys.argv) < 5:
        print("Usage: main.py <first_file> <second_file> <output_file> <second_file_format> [-e]")
        print("       Use a -e parameter to print errors during parsing.")
        sys.exit(1)

    second_file_parser = get_parser(sys.argv[4])

    print("The '{0}' parser has been selected for the second file by format '{1}'".
          format(second_file_parser.type, sys.argv[4]))

    print_errors = len(sys.argv) > 5 and sys.argv[5] == '-e'

    first_list = common.parse_file(sys.argv[1], rigla.Parser(), print_errors)
    second_list = common.parse_file(sys.argv[2], second_file_parser, print_errors)

    list_of_compared_results = comparer.Comparer(first_list, second_list).compare()

    common.write_file(sys.argv[3], list_of_compared_results.not_in_first_list,
                      list_of_compared_results.not_in_second_list, list_of_compared_results.in_both_lists)


def get_parser(parser_desc):
    return {
        'rigla': rigla.Parser(),
        'katren': katren.Parser(),
        'eclif': eclif.Parser(),
        'rosta': rosta.Parser()
    }.get(parser_desc, rigla.Parser())

if __name__ == '__main__':
    main()