import csv


class CSVfiles:

    def __init__(self, filename):
        self.filename = filename
        self.list_data = []

    def get_data(self):
        with open(self.filename, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            list_csv = list(reader)
            for element in list_csv:
                self.list_data.append(element[1])
            return self.list_data
