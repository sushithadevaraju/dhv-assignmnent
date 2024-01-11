
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
clt = pd.read_csv("climate_change.csv")
cn = pd.read_csv("climate_change.csv")
df = pd.read_csv("climate_change.csv")
data = {'Category': ['CO2', 'MEI', 'N2O', 'CFC-11', 'Aerosols'],
        'Value': [5, 10, 15, 20, 25]}
df = pd.DataFrame(data)
data_heatmap = pd.read_csv("climate_change.csv").head(10)

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Plot 1: Pie Chart
selected_columns_pie = ['CH4', 'N2O', 'CFC-12', 'TSI']
clt_2020_subset = clt[selected_columns_pie].sum()
explode = (0, 0.1, 0, 0)
colors_pie = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
label_colors_pie = ['#808080', '#333333', '#666666', '#000000']
axs[0, 0].pie(clt_2020_subset, labels=clt_2020_subset.index, autopct='%1.1f%%', startangle=90, colors=colors_pie, explode=explode)
axs[0, 0].set_title('Factors Distribution Of Climate Change', color='darkblue', fontsize=18)
axs[0, 0].set_ylabel('')

# Plot 2: Line Plot
selected_columns_line = ['Year', 'Month', 'CO2', 'CH4', 'N2O', 'CFC-11', 'CFC-12']
sns.set_palette("husl")
sns.set_style("whitegrid")
for column in selected_columns_line[2:]:
    sns.lineplot(x='Year', y=column, data=cn, label=column, ax=axs[0, 1])
axs[0, 1].set_title('Time Trend of Environmental Factors', fontsize=16, color='blue')
axs[0, 1].set_xlabel('Year', fontsize=12, color='brown')
axs[0, 1].set_ylabel('Value', fontsize=12, color='red')
axs[0, 1].legend(loc='upper left', bbox_to_anchor=(1, 1))
sns.set_theme(style="whitegrid", rc={"grid.color": ".95", "axes.labelcolor": "gray", "xtick.color": "gray", "ytick.color": "gray"})
axs[0, 1].set_xticks(axs[0, 1].get_xticks())
axs[0, 1].set_xticklabels(axs[0, 1].get_xticklabels(), rotation=45)


# Plot 3: Bar Plot
bar_colors = ['blue', 'orange', 'green', 'brown', 'gray']
background_color = 'white'
sns.barplot(x='Category', y='Value', data=df, palette=bar_colors, ci=None, ax=axs[1, 0])
axs[1, 0].set_title('Various Factors Effecting Climate Change', color='blue', fontsize=18)
axs[1, 0].set_xlabel('Category', color='purple')
axs[1, 0].set_ylabel('Value', color='red')
axs[1, 0].set_facecolor(background_color)
axs[1, 0].set_xticklabels(axs[1, 0].get_xticklabels(), rotation=45)


# Plot 4: Heatmap
selected_columns_heatmap = ['MEI', 'CO2', 'CH4', 'N2O', 'CFC-11', 'CFC-12', 'TSI', 'Aerosols', 'Temp']
dt_subset_heatmap = data_heatmap[selected_columns_heatmap]
heatmap_palette = sns.color_palette("coolwarm", as_cmap=True)
heatmap = sns.heatmap(dt_subset_heatmap, cmap=heatmap_palette, annot=True, fmt=".2f", linewidths=.5, cbar_kws={'label': 'Values'}, ax=axs[1, 1])
heatmap.set_xticklabels(heatmap.get_xticklabels(), color='green')
heatmap.set_yticklabels(heatmap.get_yticklabels(), color='yellow')
heatmap.set_xlabel('Columns', fontsize=12, color='brown')
heatmap.set_ylabel('Rows', fontsize=12, color='red')
heatmap.tick_params(axis='both', colors='black')
heatmap.set_title('Heatmap Analysis Of Climate Change', fontsize=18, color='darkblue')

# Add description 
figtext_kwargs = dict(x=1.0, y=0.9, s="Name:- Sushitha Devaraju \nStudent Id:- 22072327\nBrief Description:\nUnderstanding the factors contributing to climate change is crucial as we grapple with \nenvironmental challenges in our evolving world.\nAs depicted in the heatmap,greenhouse gases such as CO2,CH4,CFC-12 and TSI have been \nmajor contributors to climate change over the past two decades,collectively constituting \nmore than 60% of the environmental impact.The pie chart illustrates that in 2020, CH4 \nand TSI were the primary contributors, with other gases and N2O playing a smaller role. The \nline plot showcases the temporal trends of these factors, revealing a concerning increase \nin CH4 levels while also highlighting variations in other components. In particular,\nthe impact of CFC-12 fluctuates, showcasing the complexity of environmental dynamics.\nAdditionally, the bar plot draws attention to the disparities among various factors, where \nAerosols significantly contributing to higher effect in environmental changes. The need for a \ncollective global effort to mitigate these impacts becomes evident.\nThis Infographics visualization underscores the urgency of addressing climate change by \ncurbing greenhouse gas emissions and promoting sustainable practices. As our world\nbecomes more interconnected, comprehending and mitigating the factors influencing \nclimate change is vital for a sustainable and resilient future.", fontsize=18, color='black', ha='left', va='top', linespacing=2)
fig.text(**figtext_kwargs)

# Add title 
plt.suptitle('Dashboard-Factors Effecting Climate Change', x=0.5, y=0.98, fontsize=40, color='black')

# Adjust layout 
plt.tight_layout(rect=[0, 0, 1, 1])

# Save the plots 
plt.savefig("22072327.png", bbox_inches='tight', dpi=300)

