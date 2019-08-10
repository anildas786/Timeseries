import pandas
from matplotlib import pyplot

series = pandas.read_csv(
    "E:\Anil Das\KnowledgeBase\Machine Learning\PycharmProjects\Timeseries\daily-min-temperatures.csv",
    index_col=0)
print(series.head())

series.plot()
pyplot.show()
