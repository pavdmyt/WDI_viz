"""
Provides a set of tools to parse and plot CSV data from worldbank.org

Usage Example:
>>> data = parse('ukr_Country_en_csv_v2.csv')  # parse downloaded CSV

# plot table from row 42 in CSV file:

>>> table = get_table(data, 42)
>>> plot_graph(table)
"""


import csv
import matplotlib.pyplot as plt


class TableDict(dict):
    """Dict subclass for simplified access to parsed data."""

    def get_country_name(self):
        return self['Country Name']

    def get_country_code(self):
        return self['Country Code']

    def get_indicator_name(self):
        return self['Indicator Name']

    def get_indicator_code(self):
        return self['Indicator Code']

    def get_plot_data(self):
        """Fill this."""
        # get years:
        year_lst = []
        for key in self.keys():
            if key.isdigit() and self.get(key) != '':
                year_lst.append(int(key))

        year_lst.sort()

        # get values:
        values = [float(self.get(str(year))) for year in year_lst]

        # aggregate years and values (sorting by year):
        return year_lst, values


def parse(file_name, delimiter=','):
    """Fill this."""
    with open(file_name, 'r') as f:
        csv_data = csv.reader(f, delimiter=delimiter)
        parsed_data = []

        # skip over the first 3 lines of the file for the headers:
        for i in range(3):
            fields = next(csv_data)

        # fill parsed_data with tables:
        for row in csv_data:
            parsed_data.append(TableDict(zip(fields, row)))

    return parsed_data


def get_table(parsed_data, index):
    return parsed_data[index - 4]


def plot_graph(table, line_format='b-'):
    """Fill this."""
    years, values = table.get_plot_data()
    plt.plot(years, values, line_format)

    # plot appearance:
    plt.xlabel('years')
    plt.ylabel('values')
    plt.title(table.get_indicator_name())
    plt.grid(True)
    plt.show()
