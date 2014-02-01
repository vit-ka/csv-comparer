import rigla
import codecs
import comparer


def main():
    rigla_parsed_list = parse_file("./data/data1.csv", rigla.Parser())
    other_parsed_list = parse_file("./data/data2.csv", rigla.Parser())

    list_of_compared_results = comparer.Comparer(rigla_parsed_list, other_parsed_list).compare()

    print("The count of lines which are not in the second list: {0}, {1:4.2f}%".format(
          len(list_of_compared_results.one_list), len(list_of_compared_results.one_list) / len(rigla_parsed_list) * 100.0))
    print("The count of lines which are not in the first list: {0}, {1:4.2f}%".format(
          len(list_of_compared_results.two_list), len(list_of_compared_results.two_list) / len(other_parsed_list) * 100.0))

    write_file("./data/out_data.csv", list_of_compared_results.one_list, list_of_compared_results.two_list)


def write_file(filename, one_list, two_list):
    with codecs.open(filename, mode="w", encoding="cp1251") as f:
        f.write("\n\nThe values that are not in the second file but are in the first file.\n")
        for line in one_list:
            f.write(';'.join(line.value.other_values) + '\n')

        f.write("\n\nThe values that are not in the first file but are in the second file.\n")
        for line in two_list:
            f.write(';'.join(line.value.other_values) + '\n')


def parse_file(filename, parser):
    with codecs.open(filename, encoding='cp1251') as f:
        content = f.readlines()

    list_to_return = []

    parsed_counter = 0

    for line in content:
        parsed_value = parser.parse(line)

        parsed_counter += 1
        if parsed_value.arrival_date.year != 1:
            list_to_return.append(parsed_value)

    print('File "{0}" has been processed. Parsed lines: {1}. Parsing success rate: {2:4.2f}%'.
          format(filename, parsed_counter, len(list_to_return)/parsed_counter * 100.0))

    return list_to_return

if __name__ == '__main__':
    main()