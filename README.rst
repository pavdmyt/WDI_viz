World Development Indicators visualizer
=======================================

Set of tools to parse and plot CSV data from WorldBank_ website.

Example
-------

.. code-block:: python

	import viz


	# parse downloaded CSV:
	data = viz.parse('csv_country_data/China/chn_Country_en_csv_v2.csv')

	# get data on 'GDP per capita' (row 818):
	table = viz.get_table(data, 818)

	# visualize graph:
	viz.plot_graph(table)

	# visualize bar graph:
	viz.plot_bar(table)

	# save graph and bar graph into PNG file:
	viz.plot_graph(table, save=True)
	viz.plot_bar(table, save=True)

Requirements
------------

* Python_ 2.7.x
* Matplotlib_

License
-------

The WDI_viz is offered under MIT license.

.. _WorldBank: http://data.worldbank.org/
.. _Python: https://www.python.org/downloads/
.. _Matplotlib: http://matplotlib.org/downloads.html
