import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    file_name= 'epa-sea-level.csv'
    df = pd.read_csv(file_name)

    x = df.loc[:,'Year']
    y = df.loc[:,'CSIRO Adjusted Sea Level']
    # Create scatter plot
    
    fig,ax = plt.subplots()
    ax.scatter(x, y)
    
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x,y)
    x_2050 = pd.concat([x,pd.Series(range(x.iloc[-1]+1,2051))],ignore_index=True)
    ax.plot(x_2050,x_2050*slope+intercept,color='red')
    
    # Create second line of best fit
    x_new= df.loc[df['Year']>=2000,'Year']
    y_new = df.loc[df['Year']>=2000,'CSIRO Adjusted Sea Level']
    
    slope, intercept, r_value, p_value, std_err = linregress(x_new,y_new)
    x_2050 = pd.concat([x_new,pd.Series(range(x_new.iloc[-1]+1,2051))],ignore_index=True)

    ax.plot(x_2050,x_2050*slope+intercept,color='green')


    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()