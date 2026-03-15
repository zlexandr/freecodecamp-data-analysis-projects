import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv('sea-level-predictor/epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(15, 8))

    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    regr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    year_span = np.arange(df['Year'].min(), 2051)
    ax.plot(year_span, regr.slope * year_span + regr.intercept, 'r')

    # Create second line of best fit
    df_newer = df[df['Year'] >= 2000]
    year_span_newer = np.arange(2000, 2051)

    regr_newer = linregress(df_newer['Year'], df_newer['CSIRO Adjusted Sea Level'])
    ax.plot(year_span_newer, regr_newer.slope * year_span_newer + regr_newer.intercept, 'r')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
