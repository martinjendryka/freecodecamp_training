import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
file_name = 'medical_examination.csv'
df = pd.read_csv(file_name)

# Add 'overweight' column
df['height']=df.loc[:,'height']*0.01
df['BMI'] = df.loc[:,'weight']/(df.loc[:,'height']**2)
df['overweight'] = 0
df.loc[df['BMI']>25,'overweight'] = 1 

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['cholesterol']==1,'cholesterol'] = 0
df.loc[df['gluc']==1,'gluc'] = 0
df.loc[df['cholesterol']>1,'cholesterol'] = 1
df.loc[df['gluc']>1,'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,id_vars = ['cardio'],value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable'])['value'].value_counts()
    df_cat = df_cat.reset_index()
    df_cat.rename(columns={'count': 'total'}, inplace=True)
    # Draw the catplot with 'sns.catplot()'
    sns.catplot(data= df_cat, x='variable', y = 'total',hue='value',col='cardio',kind='bar')

    fig = plt.gcf()
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.copy()
    df_heat =df_heat.loc[(df_heat['ap_lo'] <= df_heat['ap_hi']) &
                        (df_heat['height'] >= df_heat['height'].quantile(0.025)) &
                         (df_heat['height'] <= df_heat['height'].quantile(0.975)) &
                         (df_heat['weight'] >= df_heat['weight'].quantile(0.025)) &
                        (df_heat['weight'] <= df_heat['weight'].quantile(0.975)),:]
    
    new_order = ['id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']
    df_heat = df_heat.loc[:,new_order]
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = corr.copy()

    for i in range(int(corr.shape[0])):
        mask.iloc[i,i:] = np.nan
    
    # Set up the matplotlib figure
    fig,ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(mask,ax=ax,annot=True, fmt=".1f")

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig