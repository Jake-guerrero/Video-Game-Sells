## Video Game Sales

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


## Loading the data and cleaning what needs to be edited out.

platform = pd.read_csv('vgsales.csv')
platform.head()

games_2024 = pd.read_csv('vgchartz-2024.csv')
games_2024.head(10)

## This data set contained images that did not show on vs code, only giving the url to these pictures of the games. Dropped the column that used the images helps with visualization when looking at the chart. Along with dropping the picture column, four other columns were dropped: na_sales, jp_sales, pal_sales and other_sales. I wanted to get the total sales of the games all together, not what countries had the sales of the specific games.

drop = ['img', 'developer', 'critic_score', 'total_sales', 'jp_sales', 'pal_sales', 'other_sales', 'last_update']
games_2024 = games_2024.drop(columns=drop)
games_2024.head()

drop = ['EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
platform = platform.drop(columns=drop)
platform.head()

## In the code above, I dropped the columns that will not be looked at and merging the two csv's into one. In the code below are the two csvs that will be looked at with the dropped columns.

games_2024
platform

## Below we will look at both the csvs into one merged csv.

games = pd.merge(games_2024[['title', 'release_date']], platform, left_on='title', right_on='Name', how='left')
games

games.to_csv("games.csv")
games


## We will now get the sum of the games, in physical copies, in North America.

Total = games['NA_Sales'].sum()
print("In North America", games['NA_Sales'].sum(), "in copies was made in video games.")

## Now to get the sum the total of the top five games in North America.

ps4_games = games.loc[(games['Year'] == 2015) & (games['Platform'] == 'PS4')]
ps4_games
ps4_games["Platform"].unique()

call_of_duty = games[games["title"]== "Call of Duty: Black Ops 3"].sum()
call_of_duty

## The two codes above will help find if the data set is a float and to help visualize calculating the total.


## Now to sort the games to help view one current year out of all the years given.
sort_games = pd.concat([
     games[games['Year'] == 2015].sort_values(by='NA_Sales', ascending=False),
     games[games['Year'] != 2015]
])


sort_games = sort_games.replace('nan', np.nan)
filter_year = sort_games[sort_games["Year"].notnull()]
filter_year["Year"] = filter_year["Year"].astype(int)
filter_year["Year"].unique()


games_2015 = games[games['Year'] == 2015]
games_totals = games_2015.groupby('title')['NA_Sales'].sum()
games_totals
top_games = games_totals.sort_values(ascending=False).head()
top_games



games_2015 = games[games['Year'] == 2015]
total_games = games_2015.groupby('title')['NA_Sales'].sum()
games_top_5 = total_games.sort_values(ascending=False).head
games_top_5


games = games[games['Year'] == 2015]
pub_2015_sales = games.groupby('Publisher')['NA_Sales'].sum()
pub_2015_sales = pub_2015_sales.sort_values(ascending=False)
pub_2015_sales.head()

## This code helps look at which genre had the most games total out of all genres given in the csv.
most_genre = games['Genre'].value_counts()
top_genre = most_genre.idxmax()
print(f"The top genre is: {top_genre}")


## Getting the genre counts to know what genre has produced the most games

genre_counts = games['Genre'].value_counts()
print("Genre Counts:")
print(genre_counts)


## Below we will see charts of how much games made, in copies, the top publishers and see the genre counts. The first code below shows how much games made per copy in a bar graph.

games_2015 = games[games['Year'] == 2015]
total_games = games_2015.groupby('title')['NA_Sales'].sum()
games_top_5 = total_games.sort_values(ascending=False).head()
games_top_5
plt.figure(figsize=(10, 6))
plt.bar(games_top_5.index, games_top_5.values, color='skyblue')
plt.title('Top 5 Games by North America Sales, by copy, in 2015')
plt.xlabel('Game Title')
plt.ylabel('Total NA Sales of copies (in millions)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


## This line of code shows how much, in copies, did the publisher make in one year, 2015, in just North America.
games_2015 = games[games['Year'] == 2015]
pub_2015_sales = games_2015.groupby('Publisher')['NA_Sales'].sum()
pub_2015_sales = pub_2015_sales.sort_values(ascending=False)
plt.figure(figsize=(10, 6))
plt.pie(pub_2015_sales.head(), labels=pub_2015_sales.head().index, autopct='%1.1f%%', startangle=140)
plt.title('Top Publishers by NA Sales in 2015')
plt.axis('equal')
plt.show()


## The final graph helps show the counts for genre that the story of the game was made for.
genre_counts = games['Genre'].value_counts()
plt.figure(figsize=(10, 6))
genre_counts.plot(kind='bar', color='skyblue')
plt.title('Genre Counts')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()