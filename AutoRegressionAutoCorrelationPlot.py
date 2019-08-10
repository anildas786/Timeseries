import pandas
from matplotlib import pyplot
from pandas.plotting import autocorrelation_plot

series = pandas.read_csv(
    'E:\Anil Das\KnowledgeBase\Machine Learning\PycharmProjects\Timeseries\daily-min-temperatures.csv',
    index_col=0)

autocorrelation_plot(series)
pyplot.show()
