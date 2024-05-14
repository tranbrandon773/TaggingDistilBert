import matplotlib.pyplot as plt
import os

data = pd.read_csv('final-1-org.csv')
tag_counts_per_org = data.groupby(['Organization ID', 'Tags']).size().unstack(fill_value=0)
colors = ['gold', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightgrey', 'orange', 'purple']
tags = data['Tags'].unique()
color_map = {tag: color for tag, color in zip(tags, colors)}

for org_id, counts in tag_counts_per_org.iterrows():
    chart_colors = [color_map[tag] for tag in counts.index]
    fig, ax = plt.subplots()
    counts.plot(kind='pie', ax=ax, colors=chart_colors, startangle=90, legend=False)
    ax.set_ylabel('')
    ax.set_title(f'{org_id}')
    plt.savefig(f'/pie_chart_{org_id}.png')
    plt.close(fig)

generated_files = [f for f in os.listdir('/') if f.startswith('pie_chart_')]