import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
 
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=50, marker='.', label='original data')
    
    # Create first line of best fit
    x1 = df['Year']
    y1 = df['CSIRO Adjusted Sea Level']
    years1 = range(1880, 2051)
    res1 = linregress(x1, y1)
    line1 = [res1.slope*i + res1.intercept for i in years1]
    plt.plot(years1, line1, 'r', label='fitted line from 1880 to 2050')
    
    # Create second line of best fit
    x2 = df[df['Year'] >= 2000]['Year']
    y2 = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    years2 = range(2000, 2051)
    res2 = linregress(x2, y2)
    line2 = [res2.slope*i + res2.intercept for i in years2]
    plt.plot(years2, line2, 'g', label='fitted line from 2000 to 2050')
    
    # Add labels and title
    ax.set(xlabel ="Year", ylabel = "Sea Level (inches)", title ='Rise in Sea Level')
    plt.xticks(range(1850, 2076, 25))
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()