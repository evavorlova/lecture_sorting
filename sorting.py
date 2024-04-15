import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data

def selection_sort(number_array, direction="ascending"):
    for index in value:
        print(index)
        hodnota = min(value)

    for hodnota in value:
        hodnota.index(0)
        print(hodnota.index)
        if index < hodnota.index:


def main():
    pass


if __name__ == '__main__':
    main()
