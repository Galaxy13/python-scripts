# mini script of comparing values in 2-column csv file
import csv
from prettytable import PrettyTable
from optparse import OptionParser


# adding and initializing option parser
parser = OptionParser()
parser.add_option('--f1', '--file1', dest='path1', type='string', help='gets path of first csv file')
parser.add_option('--f2', '--file2', dest='path2', type='string', help='gets path of second csv file')
(options, args) = parser.parse_args()


# defining class, appending paths of csv files and compare their 'value' column
class CsvCompare:
    def __init__(self, path1, path2):
        self.path1 = path1
        self.path2 = path2
        self.result = {}

    # open files and creating a dict files
    def file(self):
        with open(self.path1) as f1, open(self.path2) as f2:
            csv_1 = dict(csv.reader(f1))
            csv_2 = dict(csv.reader(f2))
        return csv_1, csv_2

    # comparing value column
    def compare(self):
        dict1 = CsvCompare.file(self)[0]
        dict2 = CsvCompare.file(self)[1]
        result_str = []
        for key in dict1:
            try:
                value1 = float(dict1[key])
                value2 = float(dict2[key])
            except:
                print("Error: no name " + key + " in " + self.path2)
                return None
            if value1 < value2:
                diff = round((((value2 - value1) / value1) * 100), 2)
                self.result[key] = diff
            elif value1 > value2:
                diff = round((((value1 - value2) / value2) * 100), 2)
                self.result[key] = diff
        self.result = {key: value for key, value in reversed(sorted(self.result.items(),
                                                           key=lambda item: item[1]))}
        for key, value in self.result.items():
            if value != 0:
                string = [key, dict1[key], dict2[key], str(value) + '%']
                result_str.append(string)
        return result_str


# launch of method csvCompare.compare
result = CsvCompare('files/1.csv', 'files/2.scv')
t = PrettyTable(['ID', 'Value1', 'Value2', 'Diff'])
t.add_rows(result.compare())
print(t)