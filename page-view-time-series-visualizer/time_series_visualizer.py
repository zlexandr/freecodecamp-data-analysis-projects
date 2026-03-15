import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('page-view-time-series-visualizer/fcc-forum-pageviews.csv', index_col=0, parse_dates=True)

# Clean data
df = df.loc[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975)), :
]

# It's a surprise tool that will help us later
month_mapping = {}
for n in range(12):
    month_name = pd.to_datetime(f'{n+1}/1/1').month_name()
    month_mapping[month_name] = n


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()

    ax.plot(df, color="#E80000")

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    fig.set_size_inches(15, 4)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar = df_bar.reset_index()

    df_bar['month'] = df_bar['date'].dt.month_name()
    df_bar['year'] = df_bar['date'].dt.year

    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()

    df_bar = df_bar.unstack().sort_index(axis=1, key=lambda x: x.map(month_mapping))

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 6))
    df_bar.plot.bar(ax=ax)

    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part ~~is done!~~ was done but I changed it a bit)
    df_box = df.copy()
    df_box.reset_index(inplace=True)

    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.month_name()

    df_box.sort_values('month', key=lambda x: x.map(month_mapping), inplace=True)
    df_box['month'] = df_box['month'].str[:3]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2)
    fig.set_size_inches(18, 5)

    ax1 = sns.boxplot(df_box, x='year', y='value', ax=axes[0], hue='year', legend=False)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    ax2 = sns.boxplot(df_box, x='month', y='value', ax=axes[1], hue='month', legend=False)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
