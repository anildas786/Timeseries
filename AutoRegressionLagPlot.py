import pandas
from matplotlib import pyplot
from pandas.plotting import lag_plot

series = pandas.read_csv(
    "E:\Anil Das\KnowledgeBase\Machine Learning\PycharmProjects\Timeseries\daily-min-temperatures.csv",
    index_col=0)
print(series.head())

lag_plot(series)
pyplot.show()
