import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from calendar import month_name

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
# Convert the date column to datetime
df['date'] = pd.to_datetime(df['date'])
# Set date column to be index
df.set_index('date', inplace=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & 
    (df['value'] <= df['value'].quantile(0.975)) ]


def draw_line_plot():
    # Draw line plot
    df_line = df.copy()
    fig = plt.figure(figsize=(15, 5))
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.plot(df_line, "r-");

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # create the month column
    months = month_name[1:]

    # create column that has the month name to match the date
    df_bar['months'] = pd.Categorical(df_bar.index.strftime('%B'), categories=months, ordered=True)

    # pivot the dataframe into the correct shape
    df_bar_pivot = pd.pivot_table(data=df_bar, index=df_bar.index.year, columns='months', values='value', aggfunc='mean', observed=True)
     
    # Draw bar plot 
    ax = df_bar_pivot.plot(kind='bar', figsize=(8, 7))
    ax.legend(loc='upper left', title='Months')
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    fig = ax.get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(20,8))
    fig.tight_layout(pad=5)

    Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.set_style("whitegrid")
    sns.set_style("ticks")
    
    sns.boxplot(data=df_box, x='year', y='value', palette="tab10", hue='year', fliersize=1, ax=ax[0])
    ax[0].set(xlabel ="Year", ylabel = "Page Views", title ='Year-wise Box Plot (Trend)')
    ax[0].get_legend().remove()
    
    sns.boxplot(data=df_box, x='month', y='value', palette="rainbow", hue='month', fliersize=1, order=Months, ax=ax[1])
    ax[1].set(xlabel ="Month", ylabel = "Page Views", title ='Month-wise Box Plot (Seasonality)')
      
    plt.show()
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
