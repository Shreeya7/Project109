import statistics
import random
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"]

mean = sum(data)/len(data)

median = statistics.median(data)

mode = statistics.mode(data)

std_dev = statistics.stdev(data)

# Finding first standard deviation start and end values and second standard deviation start and end values
first_stdev_start,first_stdev_end = mean - std_dev,mean + std_dev
second_stdev_start,second_stdev_end = mean - (2*std_dev),mean + (2*std_dev)
third_stdev_start,third_stdev_end = mean - (3*std_dev),mean + (3*std_dev)



# Ploting a distribution plot
fig = ff.create_distplot([data],["Result"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17],mode = "lines",name = "Mean"))
fig.add_trace(go.Scatter(x = [first_stdev_start,first_stdev_start],y = [0,0.17],mode = "lines",name = "Standard Deviation 1"))
fig.add_trace(go.Scatter(x = [first_stdev_end,first_stdev_end],y = [0,0.17],mode = "lines",name = "Standard Deviation 1"))

fig.add_trace(go.Scatter(x = [second_stdev_start,second_stdev_start],y = [0,0.17],mode = "lines",name = "Standard Deviation 2"))
fig.add_trace(go.Scatter(x = [second_stdev_end,second_stdev_end],y = [0,0.17],mode = "lines",name = "Standard Deviation 2"))

fig.add_trace(go.Scatter(x = [third_stdev_start,third_stdev_start],y = [0,0.17],mode = "lines",name = "Standard Deviation 3"))
fig.add_trace(go.Scatter(x = [third_stdev_end,third_stdev_end],y = [0,0.17],mode = "lines",name = "Standard Deviation 3"))
fig.show()


# Printing the findings
data_within_first_stdev = [result for result in data if result > first_stdev_start and result < first_stdev_end]
data_within_second_stdev = [result for result in data if result > second_stdev_start and result < second_stdev_end]
data_within_third_stdev = [result for result in data if result > third_stdev_start and result < third_stdev_end]

print("Mean of this data is : {}".format(mean))
print("Median of this data is : {}".format(median))
print("Mode of this data is : {}".format(mode))
print("Standard deviation of this data is {}".format(std_dev))
print("{} % of data lies within the first standard deviation".format(len(data_within_first_stdev)*100/len(data)))
print("{} % of data lies within the second standard deviation".format(len(data_within_second_stdev)*100/len(data)))
print("{} % of data lies within the third standard deviation".format(len(data_within_third_stdev)*100/len(data)))