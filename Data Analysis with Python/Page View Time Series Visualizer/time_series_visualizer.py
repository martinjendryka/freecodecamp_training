import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
file_name = 'fcc-forum-pageviews.csv'
df = pd.read_csv(file_name)
df.index = pd.date_range(start="2016-05-09",end = "2019-12-03")
df= df.drop("date",axis=1)
# Clean data
df = df.loc[(df['value']>df['value'].quantile(0.025)) & (df['value']<df['value'].quantile(0.975)),:]


def draw_line_plot():
    # Draw line plot
    fig,ax = plt.subplots()
    ax.plot(df.loc[:,'value'],color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
# function start
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df_bar.index.strftime('%B')
    df_bar['year'] = df_bar.index.year
    df_bar = df_bar.groupby(['year', 'month']).mean().reset_index()
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=month_order, ordered=True)
    
    # Draw bar plot
    width = 0.25
    years = df_bar['year'].unique().tolist()
    x = np.arange(1, 1 + len(years) * 5, step=5)
    multiplier= 0
    fig,ax = plt.subplots()

    for thismonth in month_order:
        offset = width* multiplier
        y =df_bar.loc[df_bar['month']==thismonth,'value']
        if len(y)<len(years):
            xnew = x[1:]
            ax.bar(xnew+offset,list(y),width,label=thismonth)
        else:
            ax.bar(x+offset,y,width,label=thismonth)
        multiplier += 1

  #  fig= sns.barplot(data= df_bar,x='year', y = 'value',hue='month',legend=True)
   
    ax.set_xticks([2.5, 7.5, 12.5, 17.5])
    ax.set_xticklabels(years,rotation=90)
   
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(loc='upper left',title='Months')
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    #df_box.reset_index(inplace=True)
    df_box['month'] = df_box.index.strftime('%B')
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    df_box['month'] = pd.Categorical(df_box['month'], categories=month_order, ordered=True)
    df_box['year'] = df_box.index.year
    
    # Draw box plots (using Seaborn)
    fig,axs = plt.subplots(nrows=1,ncols=2)
    sns.boxplot(data= df_box,x='year', y = 'value',ax=axs[0])
    axs[0].set_title('Year-wise Box Plot (Trend)')
    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Page Views')

    sns.boxplot(data= df_box,x='month', y = 'value',ax=axs[1])
    axs[1].set_title('Month-wise Box Plot (Seasonality)')
    axs[1].set_xlabel('Month')
    axs[1].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    axs[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig