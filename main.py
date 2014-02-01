import rigla
import comparer
import sys
import common


def main():
    if len(sys.argv) < 3:
        print("Usage: main.py <first_file> <second_file> <output_file> [-e]")
        print("       Use a -e parameter to print errors during parsing.")
        sys.exit(1)

    print_errors = len(sys.argv) > 4 and sys.argv[4] == '-e'

    first_list = common.parse_file(sys.argv[1], rigla.Parser(), print_errors)
    second_list = common.parse_file(sys.argv[2], rigla.Parser(), print_errors)

    list_of_compared_results = comparer.Comparer(first_list, second_list).compare()

    common.write_file(sys.argv[3], list_of_compared_results.not_in_first_list,
                      list_of_compared_results.not_in_second_list, list_of_compared_results.in_both_lists)


if __name__ == '__main__':
    main()