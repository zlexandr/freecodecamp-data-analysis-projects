import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# 1
df = pd.read_csv('medical-data-visualizer/medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3
df['gluc'] = df['gluc'].transform(lambda x: 0 if x == 1 else 1)
df['cholesterol'] = df['cholesterol'].transform(lambda x: 0 if x == 1 else 1)


# 4
def draw_cat_plot():
    # 5-7
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=[
        'cholesterol',
        'gluc',
        'smoke',
        'alco',
        'active',
        'overweight'
    ])

    # 8
    fig = sns.catplot(df_cat, kind='count', x='variable', hue='value', col='cardio')
    fig.set_axis_labels('variable', 'total')

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975)), :
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots()

    # 15
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    sns.heatmap(corr, mask=mask, cmap=cmap, linewidths=0.5, annot=True, fmt='.1f', annot_kws={'size': 8})

    # 16
    fig.savefig('heatmap.png')
    return fig
