import pandas
from pandas import DataFrame
from pandas import concat
from pandas.plotting import lag_plot
from matplotlib import pyplot

series = pandas.read_csv(
    'E:\Anil Das\KnowledgeBase\Machine Learning\PycharmProjects\Timeseries\daily-min-temperatures.csv',
    index_col=0)
values = DataFrame(series.values)
print(values)
dataframe = concat([values.shift(301), values], axis=1)
dataframe.columns = ['t-1', 't+1']
print(dataframe.to_string())
# lag_plot(dataframe,1)
# pyplot.show()
result = dataframe.corr()

print(result)
