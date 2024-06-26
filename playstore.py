# -*- coding: utf-8 -*-
"""Playstore.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lHpXmWGX0NlzfS48e2GBtRlV8-wAxrUk

# EDA of Google Playstore Applications
 ![playstore_banner.webp](data:image/webp;base64,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)

# Objective
The primary aim of this project is to conduct a thorough analysis of the dataset to identify significant insights. The ultimate goal is to project and emphasize customer dynamics and demands to developers and other relevant stakeholders. This will assist in driving more business towards their upcoming applications.

#      Dataset Descriptions
**App**: Name of the mobile application.

**Category**: Category or genre to which the app belongs.

**Rating**: User rating score of the app.

**Reviews**: Number of user reviews/ratings for the app.

**Size**: Size of the app installation package.

**Installs**: Number of times the app has been installed.

**Type**: Whether the app is free or paid.

**Price**: Price of the app if it's paid; otherwise, '0' or 'Free'.

**Content** **Rating**: Content rating indicating suitability for different age groups.

**Genres**: Specific genres or themes associated with the app.

**Last Updated**: Date when the app was last updated.

**Current Ver**: Current version of the app.

**Android Ver**: Minimum required Android version to run the app.
"""

pip install tabulate

!pip install plotly_express

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from tabulate import tabulate
from wordcloud import WordCloud
import plotly.graph_objects as go

Playstore="/content/drive/MyDrive/Analysis/googleplaystore.csv"

df1=pd.read_csv(Playstore)

df1.head(10)

df1.describe()

df1.info()

"""# Data Cleaning"""

null_value=df1.isnull()

nullvalue_count=null_value.sum()
nullvalue_count

#Here it shows the rows which is having the NaN value in the column called Current Ver
null_indices = df1[df1['Current Ver'].isnull()].index

# Display the row indices and corresponding rows
for index in null_indices:
    print("Row index:", index)
    print(df1.loc[index])
    print()

#Here it shows the rows which is having the NaN value in the column called Type
null_indices = df1[df1['Type'].isnull()].index

# Display the row indices and corresponding rows
for index in null_indices:
    print("Row index:", index)
    print(df1.loc[index])
    print()

#Here it shows the rows which is having the NaN value in the column called Content Rating
null_indices = df1[df1['Content Rating'].isnull()].index

# Display the row indices and corresponding rows
for index in null_indices:
    print("Row index:", index)
    print(df1.loc[index])
    print()

#Here it shows the rows which is having the NaN value in the column called Android Ver
null_indices = df1[df1['Android Ver'].isnull()].index

# Display the row indices and corresponding rows
for index in null_indices:
    print("Row index:", index)
    print(df1.loc[index])
    print()

# Find row indices with NaN values in a Rating column
nan_indices = df1[df1['Rating'].isnull()].index

# Print the row indices horizontally
print("Row indices with NaN values in column 'Rating':")
for index in nan_indices:
    print(index, end=', ')

df= df1.dropna()

# Display the cleaned DataFrame
print(df)

df.head()

null_varify=df.isnull()
nullverify_count=null_varify.sum()
nullverify_count



# Remove '+' and ',' characters from the 'Installs' column
df['Installs'] = df['Installs'].str.replace('+', '').str.replace(',', '')

# Convert the 'Installs' column to integer type
df['Installs'] = df['Installs'].astype(int)

df.head()

df.shape

df.duplicated()

"""Cleaning"""

df.duplicated().value_counts()

df.head()

data = {'count': [8886, 474]}
index = ['Unique Rows', 'Duplicate Rows']
df2 = pd.Series(data['count'], index=index)

# Plot the pie chart
plt.figure(figsize=(6, 6))
plt.pie(df2, labels=df2.index, autopct='%1.1f%%', colors=['lime', 'red'], startangle=140)

# Add title
plt.title('Percentage of Duplicate Rows')

# Show the plot
plt.axis('equal')
plt.show()

# sns.countplot(df.duplicated())

df.head()

df.info()



"""# Exploratory Data Analysis

# Analyzing 'Price' column
"""

df['Price'].value_counts()

df['Price'].loc[df['Price'].str.contains('\$')].value_counts().sum()

df['Price'] = df['Price'].apply(lambda x : x.replace('$',"") if '$' in str(x) else x)

df['Price'].value_counts()

df['Price'] = df['Price'].apply(lambda x: float(x))

"""# Analyzing 'Size' column"""

df['Size'].unique()

"""Observations:

Varies with device

M

k
"""

df[df['Size'] == 'Varies with device'].shape

df['Size'].isnull().sum()



"""There are no missing values in size column

Finding the values having M in them
"""

df['Size'].loc[df['Size'].str.contains('M')].value_counts().sum()



"""Finding the values having k in them"""

df['Size'].loc[df['Size'].str.contains('k')].value_counts().sum()

"""Finding the values having Varies with device in them"""

df['Size'].loc[df['Size'].str.contains('Varies with device')].value_counts().sum()

"""Converting the whole size column into bytes"""

def convert_size_to_bytes(size_str):
    if size_str == 'Varies with device':
        return np.nan
    elif size_str.endswith('M'):
        return float(size_str[:-1]) * 1024 * 1024
    elif size_str.endswith('k'):
        return float(size_str[:-1]) * 1024
    elif size_str.endswith('k'):
        return float(size_str[:-1])
    else:
        return np.nan

df['Size'] = df['Size'].apply(convert_size_to_bytes)

df.rename(columns = {'Size': 'Size_in_Bytes'}, inplace=True)

df['Size_in_Bytes'].dtype

df['Size_in_Bytes'].unique()

df.head(10)

plt.subplots(figsize=(20,12))
wordcloud = WordCloud(
                          background_color='black',
                          width=1920,
                          height=1080
                         ).generate(" ".join(df.App))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

"""# Correlation Analysis"""

cols = ['Rating','Reviews','Size_in_Bytes','Installs','Price']
sns.heatmap(df[cols].corr(), annot = True)

"""From the above Matrix, We can see that the reviews column has the higher correlation with Installs"""

# Convert columns to numeric if applicable
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Remove non-numeric columns
df_numeric = df[numeric_columns]

# Plot pairplot
sns.pairplot(df_numeric)
plt.suptitle('Pairplot of Numeric Columns', y=1.02)
plt.show()

"""# 1) How many different kind of apps are there in the playstore ?"""

Category = df['Category'].value_counts()
print(Category)

"""Plotting the number of different categories of application of the Google play store.

Multicolored plotting using Random
"""

Category_plotting = df['Category'].value_counts()

# Generate random colors for each category
num_categories = len(Category_plotting)
colors = [plt.cm.tab10(random.randint(0, 9)) for _ in range(num_categories)]

# Plotting
plt.figure(figsize=(20, 10))  # Adjust the figure size as needed
sns.barplot(x=Category_plotting.index, y=Category_plotting.values, palette=colors)
plt.title('Count of Categories')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

"""Muticolored plotting using Seaborn."""

Category_plotting = df['Category'].value_counts()

# Generate a list of unique colors based on the number of categories
num_categories = len(Category_plotting)
colors = sns.color_palette('viridis', n_colors=num_categories)

# Plotting
plt.figure(figsize=(20, 10))  # Adjust the figure size as needed
sns.barplot(x=Category_plotting.index, y=Category_plotting.values, palette=colors)
plt.title('Count of Categories')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()



"""# 2) How many apps are free and how many apps are pain on Playstore"""

Type_plotting = df['Type'].value_counts()
print(Type_plotting)

Type_plotting = df['Type'].value_counts()
# Plotting
plt.figure(figsize=(8, 8))  # Adjust the figure size as needed
plt.pie(Type_plotting.values, labels=Type_plotting.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of App Types')
plt.show()

# Filter out only the paid apps
paid_apps = df[df['Type'] == 'Paid']

# Display the filtered DataFrame with the prices of paid apps
paid_apps_with_prices = paid_apps[['App', 'Price']]
print(paid_apps_with_prices)

plt.figure(figsize=(15, 6))
plt.scatter(paid_apps_with_prices.index, paid_apps_with_prices['Price'], color='blue')
plt.title('Prices of Paid Apps')
plt.xlabel('App Index')
plt.ylabel('Price')
plt.show()

df.head()

"""# 3) Define the Genre of different application available on the Google Playstore"""

Genres=df['Genres'].unique()
Genres

"""# 4) Display the app count of each Genre ."""

# Assuming df is your DataFrame and 'Genres' is the name of the column

# Group by 'Genres' column and count occurrences
genre_count = df.groupby('Genres')['Genres'].agg({'count'}).reset_index()

# Display the counts of each genre
print(genre_count)

# Assuming df is your DataFrame and 'Genres' is the name of the column

# Group by 'Genres' column and count occurrences
genre_count = df.groupby('Genres')['Genres'].agg({'count'}).reset_index()

# Add an index starting from 1
genre_count.index = genre_count.index + 1
genre_count.index.name = 'Sl.No'

# Split the DataFrame into two equal halves
half_length = len(genre_count) // 2
first_half = genre_count.iloc[:half_length]
second_half = genre_count.iloc[half_length:]

# Convert halves to tabular format
first_half_tabular = tabulate(first_half, headers='keys', tablefmt='psql')
second_half_tabular = tabulate(second_half, headers='keys', tablefmt='psql')

# Print the aligned output
print(tabulate([[first_half_tabular, '', second_half_tabular]], headers=['1st Half', '', '2nd Half'], tablefmt='psql'))

df.head()

"""# 5) Which category have how many downloads ?"""

Categorywise_download = df.groupby('Category')['Installs'].agg('sum').reset_index()
print(Categorywise_download)

import matplotlib.pyplot as plt

# Plotting
plt.figure(figsize=(10, 8))
bars = plt.barh(Categorywise_download['Category'], Categorywise_download['Installs'], color='skyblue')

# Add install values directly on the bars
for bar, installs in zip(bars, Categorywise_download['Installs']):
    plt.text(bar.get_width() + 0.5e9, bar.get_y() + bar.get_height()/2, f'{installs}', va='center', fontsize=8)

plt.title('Total Installs by Category')
plt.xlabel('Total Installs')
plt.ylabel('Category')
plt.grid(axis='x', linestyle='--', alpha=0.7)  # Add grid lines for better readability
plt.tight_layout()  # Ensure labels do not overlap
plt.show()



"""**Dropping the unwanted Columns**"""

df.drop("Current Ver", axis=1, inplace=True)
df.drop("Android Ver", axis=1, inplace=True)

df.drop("Last Updated", axis=1, inplace=True)

df.head()

"""# 6) Find the of the row with the maximum number of reviews

"""

# Convert the "Reviews" column to numeric data type
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

# Find the index of the row with the maximum number of reviews
max_review_index = df['Rating'].idxmax()

# Get the corresponding row
app_with_max_reviews = df.loc[max_review_index]

print("App with Maximum Rating:")
print(app_with_max_reviews)

"""# 7) Find top 20 max rated apps which have maximum number of installation"""

max_rating = df['Rating'].max()
max_rating_apps = df[df['Rating'] == max_rating]

top_20_max_rating_apps = max_rating_apps.nlargest(20, 'Installs')

top_20_max_rating_apps.reset_index(drop=True, inplace=True)
top_20_max_rating_apps.index += 1

selected_columns = top_20_max_rating_apps[['App', 'Rating', 'Installs']]

apps_list = selected_columns.to_dict(orient='records')

print(tabulate(apps_list, headers='keys', tablefmt='psql'))

app_names = top_20_max_rating_apps['App']
ratings = top_20_max_rating_apps['Rating']
installs = top_20_max_rating_apps['Installs']

plt.figure(figsize=(10, 6))
plt.plot(app_names, ratings, marker='o', label='Rating', color='blue')
plt.plot(app_names, installs, marker='x', label='Installs', color='green')
plt.xticks(rotation=90)
plt.xlabel('App')
plt.ylabel('Value')
plt.title('Rating  and Installs of Top 20 Apps with Maximum Rating( 5.0 out of 5.0)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

"""# 8) Find  20  max rated apps which have minimum number of installation"""

max_rating = df['Rating'].max()
max_rating_apps = df[df['Rating'] == max_rating]

top_20_max_rating_apps = max_rating_apps.nsmallest(20, 'Installs')

top_20_max_rating_apps.reset_index(drop=True, inplace=True)
top_20_max_rating_apps.index += 1

selected_columns = top_20_max_rating_apps[['App', 'Rating', 'Installs']]

apps_list = selected_columns.to_dict(orient='records')

print(tabulate(apps_list, headers='keys', tablefmt='psql'))

app_names = top_20_max_rating_apps['App']
ratings = top_20_max_rating_apps['Rating']
installs = top_20_max_rating_apps['Installs']

plt.figure(figsize=(10, 6))
plt.plot(app_names, ratings, marker='o', label='Rating', color='blue')
plt.plot(app_names, installs, marker='x', label='Installs', color='Red')
plt.xticks(rotation=90)
plt.xlabel('App')
plt.ylabel('Value')
plt.title('Rating  and Installs of  20 Apps with Maximum Rating (5.0) but have very less number of installs ')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

"""# 9) Find  20   underrated apps which have Maximum number of installation




"""

min_rating = df['Rating'].min()
min_rating_apps = df[df['Rating'] == min_rating]

top_20_min_rating_apps = min_rating_apps.nlargest(20, 'Installs')

top_20_min_rating_apps.reset_index(drop=True, inplace=True)
top_20_min_rating_apps.index += 1

selected_columns = top_20_min_rating_apps[['App', 'Rating', 'Installs']]

apps_list = selected_columns.to_dict(orient='records')

print(tabulate(apps_list, headers='keys', tablefmt='psql'))

app_names = top_20_min_rating_apps['App']
ratings = top_20_min_rating_apps['Rating']
installs = top_20_min_rating_apps['Installs']

plt.figure(figsize=(10, 6))
plt.plot(app_names, ratings, marker='o', label='Rating', color='red')
plt.plot(app_names, installs, marker='x', label='Installs', color='Green')
plt.xticks(rotation=90)
plt.xlabel('App')
plt.ylabel('Value')
plt.title('Rating  and Installs of  20 Apps with Underrated (1 out of 5) but have Maximum number of installs ')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

"""# 10) Find  20   underrated apps which have very less number of installation"""

min_rating = df['Rating'].min()
min_rating_apps = df[df['Rating'] == min_rating]

top_20_min_rating_apps = min_rating_apps.nsmallest(20, 'Installs')

top_20_min_rating_apps.reset_index(drop=True, inplace=True)
top_20_min_rating_apps.index += 1

selected_columns = top_20_min_rating_apps[['App', 'Rating', 'Installs']]

apps_list = selected_columns.to_dict(orient='records')

print(tabulate(apps_list, headers='keys', tablefmt='psql'))

app_names = top_20_min_rating_apps['App']
ratings = top_20_min_rating_apps['Rating']
installs = top_20_min_rating_apps['Installs']

plt.figure(figsize=(10, 6))
plt.plot(app_names, ratings, marker='o', label='Rating', color='red')
plt.plot(app_names, installs, marker='x', label='Installs', color='Green')
plt.xticks(rotation=90)
plt.xlabel('App')
plt.ylabel('Value')
plt.title('Rating  and Installs of  20 Apps with Underrated (1 out of 5) but have very less number of installs ')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

df.head(10)

total_rows = len(df)
print("Total number of rows in the DataFrame:", total_rows)

"""# 11) Differentiate based on Content"""

content_rating_count = df['Content Rating'].value_counts().reset_index()
content_rating_count.columns = ['Content Audience', 'Number of Apps']

content_rating_count

plt.figure(figsize=(8, 8))
plt.pie(content_rating_count['Number of Apps'], labels=content_rating_count['Content Audience'], autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Apps by Content Audience')
plt.legend(content_rating_count['Content Audience'], loc="best")
plt.show()

plt.figure(figsize=(12,8))
sns.barplot(x="Content Rating", y="Installs", hue="Type", data=df)

# Create a bar plot
plt.figure(figsize=(10, 6))
bar_plot = sns.barplot(x='Content Audience', y='Number of Apps', data=content_rating_count, palette='viridis')

# Add counts on top of each bar
for index, row in content_rating_count.iterrows():
    bar_plot.text(row.name, row['Number of Apps'], f'{row["Number of Apps"]}', color='black', ha="center")

plt.title('Number of Apps by Content Audience')
plt.xlabel('Content Audience')
plt.ylabel('Number of Apps')
plt.xticks(rotation=45)

# Add legend
plt.legend(['Number of Apps'])

plt.show()

"""# 12) How are the ratings distributed across different apps?

"""

# How are the ratings distributed across different apps?
plt.figure(figsize=(10, 5))
sns.kdeplot(df['Rating'], color="green", shade=True)

"""#13) Top 20 Biggest apps by size

"""

# top 20 Biggest apps by size
df.nlargest(20, 'Size_in_Bytes')[['App', 'Size_in_Bytes']]

"""#14) Top 20 most expensive apps

"""

# Top 20 most expensive apps
df.nlargest(20, 'Price')[['App', 'Price']]

"""# 15) Top 10 reviewed apps

"""

# top 10 reviewed apps
df.nlargest(10, 'Reviews')[['App', 'Reviews']]

"""# 16) Distribution of content rating and rating"""

data = go.Box(
    x=df['Content Rating'],
    y=df['Rating'],
    marker_color='mediumorchid',
)
layout = go.Layout(height=800,
                   width=1200,
                   title={
                       'text': "Distribution Of Content Rating",
                       'x': 0.4,
                       'y': 0.93,
                       'xanchor': 'center',
                       'yanchor': 'top'
                   },
                   xaxis={'title': 'Content Rating'},
                   yaxis=dict(title='Rating'),
                   template='simple_white')
fig = go.Figure(data=data, layout=layout)
fig.show()

"""# **observations and conclusions**

#Based on the provided data, here is a summary

Top Apps:

The most popular app is ROBLOX with a rating of 9. Other notable apps include 8 Ball Pool, Bubble Shooter, Helix Jump, Zombie Catchers, Bowmasters, Candy Crush Saga, and Temple Run 2.

App Categories:

The majority of apps fall into the FAMILY category (1717), followed by GAME (1074) and TOOLS (733).

App Ratings:

The most common ratings are 4.4, 4.3, and 4.5, indicating a generally positive user sentiment.

App Sizes:

A significant number of apps have a size that varies with the device (1637), with other common sizes around 14M, 12M, 15M, and 11M.

Number of Installs:

A large portion of apps has been installed over 1,000,000 times (1576), with other popular install ranges being 10,000,000+ and 100,000+.

App Types:

The majority of apps are Free (8275), with only a small portion being Paid (611).

App Genres:

Top genres include Tools, Entertainment, Education, Action, and Productivity.

Content Ratings:

The majority of apps are rated Everyone (7089), followed by Teen, Mature 17+, and Everyone 10+.

# **Key Conclusions:**

Market Diversity:

There appears to be significant diversity in the app market, with a notable emphasis on family-oriented and gaming applications.

Positive Ratings:

The distribution of user ratings suggests a general preference and liking, with a high proportion of apps receiving favorable ratings.

High Installations:

A large number of apps have been installed over a million times, indicating widespread popularity among users.

Regular Updates:

The presence of a substantial number of updates, especially around August 2018, indicates ongoing developer interest in enhancing and updating the applications.

Trend Towards Free Apps:

It appears that the majority of apps are offered for free, reflecting the prevalent trend of providing free services to users.

Broad Android Version Support:

Developers seem to target a wide range of Android operating system versions to ensure app compatibility with a diverse array of devices.

User Engagement:

Positive ratings and high installation numbers suggest strong user engagement with these applications.
"""