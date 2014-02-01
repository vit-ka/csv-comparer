import rigla
import codecs

__author__ = 'lattyf'


def main():
    riglaParser = rigla.Parser()

    with codecs.open("./data/data1.csv", encoding='cp1251') as f:
        content = f.readlines()

    parsed_counter = 0
    correctly_parsed_counter = 0

    for line in content:
        parsed_value = riglaParser.parse(line)
        parsed_counter += 1
        if parsed_value.arrival_date.year != 1:
            correctly_parsed_counter += 1

    print('File "{0}" has been processed. Parsed lines: {1}. Parsing success rate: {2:4.2f}%'.
          format("./data/data1.csv", parsed_counter, correctly_parsed_counter/parsed_counter * 100.0))

if __name__ == '__main__':
    main()