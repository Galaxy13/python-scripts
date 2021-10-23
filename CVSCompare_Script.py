# mini script of comparing values in 2-column csv file
import csv
from optparse import OptionParser

# adding and initializing option parser
parser = OptionParser
parser.add_option('-f1', '--file1', dest='path1',
                  help='gets path of first csv file', metavar='FILEPATH')
parser.add_option('-f2', '--file2', dest='path2',
                  help='gets path of second csv file', metavar='FILEPATH')
(options, args) = parser.parse_args()


# defining class, appending paths of csv files and compare their 'value' column
class CsvCompare:
    def __init__(self, path1, path2):
        self.path1 = path1
        self.path2 = path2
        self.result = []

    # open files and creating a dict files
    def file(self):
        # results1, results2 = {}, {}
        csv_1 = dict(csv.reader(open(self.path1)))
        csv_2 = dict(csv.reader(open(self.path2)))
        return csv_1, csv_2

    # comparing value column
    def compare(self):
        dict1 = CsvCompare.file(self)[0]
        dict2 = CsvCompare.file(self)[1]
        for key1 in dict1:
            for key2 in dict2:
                if key1 == key2:
                    try:
                        value1 = float(dict1[key1])
                        value2 = float(dict2[key2])
                    except:
                        continue
                    if dict1[key1] < dict2[key2]:
                        self.result.append(
                            str(key1) + ',' + dict1[key1] + ',' + dict2[key2] + ', ' + str(value1 / value2 * 100))
                    elif dict1[key1] > dict2[key2]:
                        self.result.append(
                            str(key1) + ',' + dict1[key1] + ',' + dict2[key2] + ', ' + str(value2 / value1 * 100))
        return self.result


# example launch of method csvCompare.compare
result = CsvCompare(options.path1, options.path2)
print(result.compare())
