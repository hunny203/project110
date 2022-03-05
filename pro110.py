import csv
import plotly.figure_factory as ff
import pandas as pd
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv("med.csv")

data=df["reading_time"].tolist()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
        
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(1000)
        mean_list.append(set_of_means)

    show_fig(mean_list)
    mean=statistics.mean(mean_list)
    print("mean is: ",mean)

setup()

def standard_deviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(1000)
        mean_list.append(set_of_means)
    temp_sd=statistics.stdev(mean_list)
    print("standard deviation is : ", temp_sd)

standard_deviation()



