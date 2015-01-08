"""
Provides a set of tools to parse and plot CSV data from worldbank.org

Usage Example
-------------
# parse downloaded CSV:
>>> data = parse('ukr_Country_en_csv_v2.csv')

# get table from row 42 in CSV file:
>>> table = get_table(data, 42)

# visualize graph:
>>> plot_graph(table)

# visualize bar graph:
>>> plot_bar(table)

# save graph and bar graph into PNG file:
>>> plot_graph(table, save=True)
>>> plot_bar(table, save=True)
"""


import csv
import matplotlib.pyplot as plt


class TableDict(dict):
    """Dict subclass for simplified access to the parsed data."""

    def get_country_name(self):
        return self['Country Name']

    def get_country_code(self):
        return self['Country Code']

    def get_indicator_name(self):
        return self['Indicator Name']

    def get_indicator_code(self):
        return self['Indicator Code']

    def get_plot_data(self):
        """Fetch years list with corresponding values list.

        :return: ``tuple`` years list and values list.
        """
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
    """Parses CSV file.

    Each TableDict stores table headers as ``table.keys()``
    and appropriate values as ``table.values()``

    :param file_name: ``str`` CSV file to parse.
    :param delimiter: ``str`` CSV file delimiter.
    :return: ``list``
    """
    with open(file_name, 'r') as f:
        csv_data = csv.reader(f, delimiter=delimiter)
        parsed_data = []

        # skip over the first 3 lines of the file for the headers:
        for i in range(3):
            fields = next(csv_data)

        # fill parsed_data with TableDict objects:
        for row in csv_data:
            parsed_data.append(TableDict(zip(fields, row)))

    return parsed_data


def get_table(parsed_data, index):
    """Fetch a table corresponding to specified row # in CSV file.

    :param parsed_data: ``list`` of ``TableDict`` objects.
    :param index: ``int`` row number in CSV file.
    :return: ``TableDict``
    """
    return parsed_data[index - 4]


def plot_save(table, plot_type):
    """Wrapper around plt.savefig().

    :param table: ``TableDict`` data to plot.
    :param plot_type: ``str`` specifies in a filename whether it's
        graph or a bar plot.
    """
    country_code = table.get_country_code() + '_'
    indicator = table.get_indicator_code()

    # Save and close figure:
    plt.savefig(country_code + indicator + plot_type + '.png')
    plt.clf()


def plot_graph(table, line_format='b-', save=False):
    """Shows/saves graph.

    :param table: ``TableDict`` data to plot.
    :param line_format: ``str`` line style and color abbreviation
        same as in ``plt.plot()``
    :param save: ``bool`` saves graph as PNG if ``save=True``
    """
    years, values = table.get_plot_data()
    plt.plot(years, values, line_format)

    # Set appearance:
    plt.xlabel('years')
    plt.ylabel('values')
    plt.title(table.get_indicator_name())
    plt.grid(True)

    if save:
        plot_save(table, '_graph')
    else:
        plt.show()


def plot_bar(table, color='b', width=0.5, save=False):
    """Shows/saves bar plot.

    :param table: ``TableDict`` data to plot.
    :param color: ``str`` the colors of the bar faces
        same as in ``plt.bar()``
    :param width: ``float`` the width(s) of the bars
        same as in ``plt.bar()``
    :param save: ``bool`` saves bar plot as PNG if ``save=True``
    """
    years, values = table.get_plot_data()

    # Set where the labels hit the x-axis:
    xloc = [_ + 0.5 for _ in xrange(len(years))]

    # Make a bar plot:
    plt.bar(xloc, values, color=color, width=width)

    # Tick labels location to x-axis:
    plt.xticks([_ + width / 2 for _ in xloc], years, rotation=90)

    # Set appearance:
    plt.ylabel('values')
    plt.title(table.get_indicator_name())
    plt.grid(True)

    if save:
        plot_save(table, '_barplot')
    else:
        plt.show()
