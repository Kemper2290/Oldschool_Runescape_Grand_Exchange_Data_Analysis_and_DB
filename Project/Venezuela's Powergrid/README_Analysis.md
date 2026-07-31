
# Economical Impact of Bombing of Venezula Powergrid and It's effect on OSRS Grand Exchange

## Structure of Project
- Title
- Project Description
- Methods Used
- Dataset
- Tech Stack
- Project Architecture
- Results and Discussion
- Example Figures
- Future Improvements
- How to Run

## Project Description

On January 3, 2026, the United States detained the Venezuelan president for extradition to the United States on drug conspiracy charges. As part of this operation, the United States reportedly targeted portions of Venezuela's power grid in an attempt to limit the country's response. Disabling the power grid for as little as 36 hours had significant consequences for the country's population. The disruption resulted in health emergencies, lost work, and reduced leisure time. Because of the widespread power outages, many people also lost access to internet services, reducing the number of people able to play online video games.

One of the most popular video games of all time is RuneScape. The franchise has existed in some form since 2001. After several controversial updates that divided the community, RuneScape rereleased a nostalgic version of the game called Old School RuneScape (OSRS). OSRS places a strong emphasis on community feedback when determining the direction of future development while preserving the gameplay that originally made RuneScape popular. As a result, the game has experienced continued growth, with online player counts consistently exceeding 100,000 concurrent players. Jagex, the game's developer, has continued expanding the RuneScape universe and has been valued at over $1.1 billion, with both sales and player counts continuing to increase.

Today, OSRS is played all over the world by a diverse player base spanning many countries and languages. Unfortunately, like many massively multiplayer online (MMO) games, OSRS struggles with cheaters, exploiters, and bots. Due to RuneScape's unique server-side architecture, cheating is generally less prevalent than in many other online games. Instead, the primary issue is bots—scripted player accounts that automatically perform in-game tasks without human interaction. Because OSRS has relatively low hardware requirements, malicious users can run dozens or even hundreds of bot accounts simultaneously on a single computer. Regardless of the tasks they perform, these bots typically sell the resources they gather for real-world money or sell them on the Grand Exchange (GE) for in-game profit.

In OSRS, the Grand Exchange is the primary marketplace where players trade items for in-game currency. Conceptually, it is similar to a stock exchange, where players speculate on item values and attempt to profit from future price changes. The Grand Exchange is essential to the game's economy, allowing players to efficiently buy and sell resources needed for gameplay. It is also a nostalgic location that many long-time players remember fondly. On a small scale, a few dozen or even a few hundred bots would have little effect on a global economy that processes millions of item trades every hour. However, the profitability of botting has led to the creation of industrial-scale bot farms consisting of thousands of automated accounts. These bots generate real-world income, contribute to inflation, manipulate item prices, steal accounts, and generally reduce the quality of the game. Prosecuting the organizations responsible for operating these bot networks remains difficult because legal systems have been slow to adapt to this type of activity.

Within the OSRS community, there is a long-running belief that many of these bots are operated by individuals in Venezuela. Due to the country's economic conditions and the exchange value of OSRS gold relative to the U.S. dollar, botting is often perceived as a viable source of income. Additionally, several well-known RuneScape content creators have produced videos interviewing or exposing individuals involved in botting operations. Whenever large numbers of bots suddenly disappear, discussions quickly appear on Reddit, OSRS Discord communities, and YouTube. One explanation is that Jagex has conducted a large-scale bot ban wave, during which thousands of accounts are banned simultaneously to make it more difficult for bot developers to determine how their accounts were detected. Another commonly suggested explanation is Venezuela's recurring nationwide power outages. For years, players have observed what they believe to be substantial reductions in bot activity following prolonged blackouts in Venezuela.This project investigates whether the January 3 power outage, reportedly caused by U.S. strikes on Venezuela's power grid, provides measurable evidence supporting those claims.

## Methods
To analyze whether there is a statistical difference in bot activity before and after the US bombed the Venezuelan powergrid we looked at buy volume of items and player population before and after. When using the OSRS API to pull item information from the grand exchange we had a lot of options available. We decided to settle on a few import items that are critical for all players and who's base ingredients are likely farmed by bots resulting in price changes if bots disappear. We can break these items into 3 categories: food,potions, and runes. 

All three of these items are generically agreed upon by the community that bots farm these base ingredients and sell them in high numbers or craft and sell those in high numbers. When pulling information from the OSRS GE we can see buy/sell price and volume. With these options, we agreed to focus on changes in buy volume for two reasons. One, real players could be holding vast amounts of these items and notice a increase in price once the number of items available decrease due to bots. That could result in a massive sell off which could skew our results. Second, we're interested in the normal players buying these items and using them, not billionaries with vast funds manipulating the market. As such, regular players would still be required to buy these items regardless of the price because they are critical for a wide variety of game content.Additionally, its unlikely that normal players would have a massive volume of items to sell on immediately. Currently, our analysis looked at cooked and raw lobsters,sharks,anglerfish and our statistical methods focused on the raw version since it is the easiest for the most amount of bots to get.

First, we analyzed the raw and cooked lobsters,sharks,anglerfish buy/sell volume and price over the last year to get an idea of the landscape for these items. After initial analysis and cleaning, we focused on the cooked versions of these items and split them into 1 week before jan 3rd 2026 and one week after jan 3rd include the 3rd. Cooked food was focused for this data analaysis because the difference in cost between cooked and uncooked is small resulting in players buying cooked food to save time and for convience. Each group was test for normalcy and equal variance so that we could run a Two Way ANOVA on the data. Normalcy was tested using QQ-plots,histograms, and a Shapiro-Wilks test. Variance was tested using a Levene's test.  Alongside analyzing those items, we also analyzed the player count under the same time constraint as the previous items. Here we tracked the last year of player counts with using osrsplayercount.com api. Here we used an independent t-test and a Mann-Whitney U test to determine if there was a statically significant difference in player count after we checked for normality and variance.

## DataSets

Data for the GE was pulled using runescape wiki API. Playercount was pulled from osrsplayercount.com using their api which tracks the historical player count for OSRS from OSRS's website each hour every day. The data from this project is stored in a database and accessed with sql commands. The database and item table is created by the create_osrs_ge_DB_and_item_table.py file. The Venezuela_bots table is created by the pull_data_Venezuela.py file. The player_count table is created by the Pull_player_count.py file.

## Tech Stack

| Category  | Technology    |
| Language  | Python        |
| Database  | MySQL         |
| Analysis  | Pandas, SciPy, Statsmodels |
| Visualization | Matplotlib |
| APIs      | OSRS wiki API, OSRSPlayercount.com API |

## Project Architecture

```text

──────────────────────────────────────────────────────────
                        Data Collection
──────────────────────────────────────────────────────────
            
                    OSRS Wiki Grand Exchange API
                                │
                    (HTTP GET requests using requests)
                                ▼
                    Python Data Collection Scripts
                                │
                    (Parse JSON responses and extract item data)
                                ▼
                    Store Historical data in MySQL Database
                    
            
──────────────────────────────────────────────────────────
                        Data Preparation    
──────────────────────────────────────────────────────────
            
                    Historical Item data from MySQL Database
                                │
                    (SQL queries retrive historical market data)
                                ▼
                    Utilize Pandas DataFrames
                                │
        ┌───────────────────────┴────────────────────────┐
        ▼                                                ▼
   Data Cleaning                               Feature Engineering
(Remove invalid rows,                   (Create time periods,
convert data types,                     calculate derived variables,
format timestamps)                      filter selected items)
        │                                                │
        └───────────────────────┬────────────────────────┘
                                ▼
                 Exploratory Data Analysis (EDA)
          (Summary statistics, trend plots, distributions)


──────────────────────────────────────────────────────────
                        Statistical Analysis
──────────────────────────────────────────────────────────
                    
                    Check Statistical Assumptions
                • Shapiro-Wilk Test (Normality)
                • Levene's Test ( Difference of Variance)
                
                                │
                          Two-Way ANOVA 
                (Evaluate the effects of item an time period on
                    Grand Exchange buy volume)
                                │
                    Interpret statistical significane
                                ▼
                        Post Hoc Analysis                         

```

## Results and Disccusion

### Step 1: Intial Data Exploration

As stated previously, our research aim is determine if there is a statistical difference in bot activity before and after the US bombed the Venezuelan powergrid. To find an answer to that question, we can look at buy and sell volumes and prices as well as player count. To begin, we looked at trends in the data by visualize columns in the data.

First we confirm our full dataframe and its types.
```Python
fulldf.head()
```
|   item_id | item_name   | timestamp   |   avg_buy_price |   avg_sell_price |   buy_volume |   sell_volume |
|----------:|:------------|:------------|----------------:|-----------------:|-------------:|--------------:|
|       377 | Raw lobster | 2025-06-29  |              74 |               71 |      1990604 |       1425499 |
|       377 | Raw lobster | 2025-06-30  |              73 |               71 |       567482 |        376524 |
|       377 | Raw lobster | 2025-07-01  |              74 |               72 |      1249003 |       1274335 |
|       377 | Raw lobster | 2025-07-02  |              73 |               72 |      1039449 |       1117976 |
|       377 | Raw lobster | 2025-07-03  |              77 |               76 |       443869 |        569578 |

```Python
fulldf.info()
```
|                | Data Type   |
|:---------------|:------------|
| item_id        | int64       |
| item_name      | object      |
| timestamp      | object      |
| avg_buy_price  | float64     |
| avg_sell_price | int64       |
| buy_volume     | int64       |
| sell_volume    | int64       |
 

Since the data from .head() and we understand the data types from .describe() we can look at the descriptive statistics of our dataframe for each group to understand the spread of our data

```Python
fulldf.groupby(['item_name'])['item_id'].describe()
```

| item_name              |   count |   mean |   std |   min |   25% |   50% |   75% |   max |
|:-----------------------|--------:|-------:|------:|------:|------:|------:|------:|------:|
| Anglerfish             |     365 |  13441 |     0 | 13441 | 13441 | 13441 | 13441 | 13441 |
| Blood rune             |     365 |    565 |     0 |   565 |   565 |   565 |   565 |   565 |
| Cosmic rune            |     365 |    564 |     0 |   564 |   564 |   564 |   564 |   564 |
| Lobster                |     365 |    379 |     0 |   379 |   379 |   379 |   379 |   379 |
| Prayer potion(4)       |     365 |   2434 |     0 |  2434 |  2434 |  2434 |  2434 |  2434 |
| Ranging potion(4)      |     365 |   2444 |     0 |  2444 |  2444 |  2444 |  2444 |  2444 |
| Raw anglerfish         |     365 |  13439 |     0 | 13439 | 13439 | 13439 | 13439 | 13439 |
| Raw lobster            |     365 |    377 |     0 |   377 |   377 |   377 |   377 |   377 |
| Raw shark              |     365 |    383 |     0 |   383 |   383 |   383 |   383 |   383 |
| Saradomin brew(4)      |     365 |   6685 |     0 |  6685 |  6685 |  6685 |  6685 |  6685 |
| Shark                  |     365 |    385 |     0 |   385 |   385 |   385 |   385 |   385 |
| Soul rune              |     365 |    566 |     0 |   566 |   566 |   566 |   566 |   566 |
| Super combat potion(4) |     365 |  12695 |     0 | 12695 | 12695 | 12695 | 12695 | 12695 |
| Super restore(4)       |     365 |   3024 |     0 |  3024 |  3024 |  3024 |  3024 |  3024 |
| Zulrah's scales        |     365 |  12934 |     0 | 12934 | 12934 | 12934 | 12934 | 12934 |


After beginning to see the range of our data in a genearl sense, we began seperating the items into item_name groups for analysis. Additionally, since our data uses a timestamp of Year-Month-Day, we additionally made a column called days to help visualize ranges of days before and after the bombing that start at 1 for our initial recording and end 365 days later due to data point restraints

```Python
days = np.arange(1,366,1)

#common food
lobsterdf = fulldf.loc[fulldf['item_name']=='Lobster'].reset_index()
lobsterdf['days'] = days
lobsterdf.head()
lobsterdf.tail()

raw_lobsterdf = fulldf.loc[fulldf['item_name']=='Raw lobster'].reset_index()
raw_lobsterdf['days'] = days
raw_lobsterdf.head()
raw_lobsterdf.tail()

sharkdf = fulldf.loc[fulldf['item_name']=='Shark'].reset_index()
sharkdf['days'] = days
sharkdf.head()
sharkdf.tail()

raw_sharkdf = fulldf.loc[fulldf['item_name']=='Raw shark'].reset_index()
raw_sharkdf['days'] = days
raw_sharkdf.head()
raw_sharkdf.tail()

anglerfishdf = fulldf.loc[fulldf['item_name']=='Anglerfish'].reset_index()
anglerfishdf['days'] = days
anglerfishdf.head()
anglerfishdf.tail()

raw_anglerfishdf = fulldf.loc[fulldf['item_name']=='Raw anglerfish'].reset_index()
raw_anglerfishdf['days'] = days
raw_anglerfishdf.head()
raw_anglerfishdf.tail()
 ```

The .head() and .tail() of these new dataframes for each food should look similar to what is below.

```Python
lobsterdf.head()
```

|   index |   item_id | item_name   | timestamp   |   avg_buy_price |   avg_sell_price |   buy_volume |   sell_volume |   days |
|--------:|----------:|:------------|:------------|----------------:|-----------------:|-------------:|--------------:|-------:|
|     365 |       379 | Lobster     | 2025-06-29  |             137 |              132 |      2228486 |        537716 |      1 |
|     366 |       379 | Lobster     | 2025-06-30  |             131 |              125 |       420910 |        110689 |      2 |
|     367 |       379 | Lobster     | 2025-07-01  |             124 |              122 |      1806859 |        493088 |      3 |
|     368 |       379 | Lobster     | 2025-07-02  |             122 |              117 |      1739691 |        569019 |      4 |
|     369 |       379 | Lobster     | 2025-07-03  |             118 |              116 |      1807006 |        701078 |      5 |

```Python
lobsterdf.tail()
```

|   index |   item_id | item_name   | timestamp   |   avg_buy_price |   avg_sell_price |   buy_volume |   sell_volume |   days |
|--------:|----------:|:------------|:------------|----------------:|-----------------:|-------------:|--------------:|-------:|
|     725 |       379 | Lobster     | 2026-06-24  |             133 |              131 |        53945 |         51645 |    361 |
|     726 |       379 | Lobster     | 2026-06-25  |             132 |              131 |        16825 |         30364 |    362 |
|     727 |       379 | Lobster     | 2026-06-26  |             133 |              131 |        32144 |         46799 |    363 |
|     728 |       379 | Lobster     | 2026-06-27  |             129 |              125 |        59097 |         25514 |    364 |
|     729 |       379 | Lobster     | 2026-06-28  |             129 |              127 |        26736 |         41282 |    365 |


After analyzing the data, we are primarily focused on the cooked food. Due to the small difference in value between cooked and uncooked and ease of access for cooked for most players, we will focus primarily on cooked food. Here we plot the buy and sell volumes of cooked shark, lobsters, and anglerfish.

```Python
ax=lobsterdf.plot('timestamp','sell_volume',label='Lobster-SellVol',color='orange',xlim=('2025-12-15','2026-01-31'),linestyle='--')
lobsterdf.plot('timestamp','buy_volume',label='Lobster-BuyVol',color ='peru',ax=ax,linestyle='-')

sharkdf.plot('timestamp','sell_volume',label = 'Shark-SellVol',color='brown',ax=ax,linestyle='--')
sharkdf.plot('timestamp','buy_volume',label='Shark-BuyVol',color = 'saddlebrown',ax=ax,linestyle='-')

anglerfishdf.plot('timestamp','sell_volume',label= 'Anglerfish-SellVol',color='green',ax=ax,linestyle='--')
anglerfishdf.plot('timestamp','buy_volume',label='Anglerfish-BuyVol',color = 'lightgreen',ax=ax,linestyle='-')

ax.xaxis.set_major_locator(mdates.DayLocator()) # Label every day
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d')) # Format as Dec 01, Dec 02, or 12-01,12-02 ...
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Buy and Sell Volume of Cooked Food')
```


![img](Buy and Sell Volume of Cooked Food.png)

From the above graph, two things are clear. First, its obvious that the buy volumes are almost always greater than the sell volume. Intrinsically this makes sense, players use food for all sorts of content and likely consume more than they use. However, it should be noted that this data only shows that food is bought more than its sold, food could still be held in banks indicating vast stores. Secondly, there is a specific spike in both buy and sell volume at on january 3rd and sixth. There provides some concrete evidence that we are seeing shifts in the market that could possibly be related to the rolling blackouts in venezuela following the bombing of their powergrid.

As a logical check, we see a similar trend when we analyze the buy and sell volume in raw food below.

```Python

ax=raw_lobsterdf.plot('timestamp','sell_volume',label='raw-lobster-SellVol',color='orange',xlim=('2025-12-15','2026-01-31'),linestyle='--')
raw_lobsterdf.plot('timestamp','buy_volume',label='raw-lobster-BuyVol',color ='peru',ax=ax,linestyle='-')

raw_sharkdf.plot('timestamp','sell_volume',label = 'raw-shark-SellVol',color='sandybrown',ax=ax,linestyle='--')
raw_sharkdf.plot('timestamp','buy_volume',label='raw-shark-BuyVol',color = 'saddlebrown',ax=ax,linestyle='-')

raw_anglerfishdf.plot('timestamp','sell_volume',label= 'raw-anglerfish-SellVol',color='green',ax=ax,linestyle='--')
raw_anglerfishdf.plot('timestamp','buy_volume',label='raw-anglerfish-BuyVol',color = 'lightgreen',ax=ax,linestyle='-')

ax.xaxis.set_major_locator(mdates.DayLocator()) # Label every day
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d')) # Format as Dec 01, Dec 02, or 12-01,12-02 ...
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Buy and Sell Volume of Raw Food')
```


![img](Buy and Sell Volume of Raw Food.png)

Interesting enough we notice that when the raw food is analyzed, we see similar spikes at the same dates mentioned. However, here we see that the sell volume is greater than the buy volume for raw shark and anglerfish. It's possible that people were aware noticing a change in market value for these items and were selling off in mass. It's worth mentioning here that the change in buy and sell volumes is still within the same magnitude so that change is not to extreme.

Another interesting thing to note is that despite a change in buy and sell volume around Jan 3rd, the prices of the items and their margins stayed roughly the same. Below is a plot of the buy and sell price for the cooked food which resemblems the same trend in buy and sell price for raw food. However, we dont see a spike in prices around jan 3rd like we do in buy and sell volume.

```Python
ax=lobsterdf.plot('timestamp','avg_sell_price',label='lobster-SellPrice',color='orange',xlim=('2025-12-15','2026-01-31'),linestyle='--')
lobsterdf.plot('timestamp','avg_buy_price',label='lobster-BuyPrice',color ='peru',ax=ax,linestyle='-')

sharkdf.plot('timestamp','avg_sell_price',label = 'shark-SellPrice',color='sandybrown',ax=ax,linestyle='--')
sharkdf.plot('timestamp','avg_buy_price',label='shark-BuyPrice',color = 'saddlebrown',ax=ax,linestyle='-')

anglerfishdf.plot('timestamp','avg_sell_price',label= 'anglerfish-SellPrice',color='green',ax=ax,linestyle='--')
anglerfishdf.plot('timestamp','avg_buy_price',label='anglerfish-BuyPrice',color = 'lightgreen',ax=ax,linestyle='-')

ax.xaxis.set_major_locator(mdates.DayLocator()) # Label every day
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d')) # Format as Dec 01, Dec 02, or 12-01,12-02 ...
plt.xticks(rotation=45)
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Buy and Sell Price of Cooked Food')

```


![img](Buy and Sell Price of Cooked Food.png)

Now that we have confirmed our data in our dataframe and analyzed trends in the data, we can move forward with our statistical analysis. We begin by performing a two way anova on our cooked food buy volume by comparing the data a week before jan 3rd and a week after(including jan 3rd). As such our independent variables are the period (before vs after) and food type. Our dependent variable ,in this case, is buy volume since we are interested in that change. Our anova will tell us two main effects from our dependent variables and if there is an interaction between these two main effects. Our first main effect tell us if there is a difference in average buy volume for all items combined before and after jan 3rd. Our second effect tells us if there is a difference in sharks, lobsters, and anglerfish buy volumes regardless of the period it takes place. Finally the interaction between the two effects tells us if jan 3rd has an effect on which item your looking at. For example, did sharks buy volume increase more than lobsters. In general, the interaction tells us whether the change before and after jan 3rd is different for each item.

We begin our two way anova by setting up an event window to only contain data in the date range we're interested in 

```Python 
food_df = pd.concat([lobsterdf,sharkdf,anglerfishdf],axis=0,ignore_index=True)
food_df['timestamp'] = pd.to_datetime(food_df['timestamp'])
event_date = pd.Timestamp("2026-01-03")
event_window = food_df[
    (food_df['timestamp'] >= event_date - pd.Timedelta(days=7)) &
    (food_df['timestamp'] <= event_date + pd.Timedelta(days=6))].copy()

event_window['period'] = 'After'
event_window.loc[event_window['timestamp'] < event_date,'period'] = 'Before'

event_window.head()
```

|   index |   item_id | item_name   | timestamp           |   avg_buy_price |   avg_sell_price |   buy_volume |   sell_volume |   days | period   |
|--------:|----------:|:------------|:--------------------|----------------:|-----------------:|-------------:|--------------:|-------:|:---------|
|     546 |       379 | Lobster     | 2025-12-27 00:00:00 |             188 |              183 |       398827 |        276886 |    182 | Before   |
|     547 |       379 | Lobster     | 2025-12-28 00:00:00 |             188 |              183 |       404470 |        257661 |    183 | Before   |
|     548 |       379 | Lobster     | 2025-12-29 00:00:00 |             188 |              183 |       362695 |        261775 |    184 | Before   |
|     549 |       379 | Lobster     | 2025-12-30 00:00:00 |             186 |              181 |       376831 |        179768 |    185 | Before   |
|     550 |       379 | Lobster     | 2025-12-31 00:00:00 |             183 |              177 |       524085 |        227959 |    186 | Before   |


we follow up by showing a quick summary of our new event window to get an idea of the data and trends

```Python
summary = (
    event_window
    .groupby(["item_name", "period"])["buy_volume"]
    .agg(
        Count="count",
        Mean="mean",
        Std="std",
        Median="median",
        Q1=lambda x: x.quantile(0.25),
        Q3=lambda x: x.quantile(0.75),
        Min="min",
        Max="max"
    )
    .round(0)
)
summary=summary.reset_index()
print(summary)
```

| item_name   | period   |   Count |             Mean |              Std |           Median |               Q1 |               Q3 |    Min |     Max |
|:------------|:---------|--------:|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|-------:|--------:|
| Anglerfish  | After    |       7 | 814703           | 716694           | 487263           | 413809           |      1.05044e+06 | 169272 | 2117893 |
| Anglerfish  | Before   |       7 | 421603           | 192858           | 498137           | 399770           | 536972           |  19520 |  560080 |
| Lobster     | After    |       7 | 579728           | 516580           | 361187           | 306128           | 750106           |  97507 | 1486936 |
| Lobster     | Before   |       7 | 367885           | 160591           | 398827           | 369763           | 442258           |  28245 |  524085 |
| Shark       | After    |       7 |      2.16331e+06 |      1.71024e+06 |      1.53879e+06 |      1.21978e+06 |      2.91497e+06 | 427574 | 4907279 |
| Shark       | Before   |       7 |      1.07414e+06 | 454605           |      1.21805e+06 |      1.13876e+06 |      1.28902e+06 |  65808 | 1379553 |


#to identify any outlier in our data, we created a boxplot of our food before and after the event.

```Python
fig,ax = plt.subplots(figsize=(8,6))
event_window.boxplot(
    column='buy_volume',
    by=['item_name','period'],
    ax=ax
)
plt.title("Buy Volume by Item and Period")
plt.suptitle("")  # Removes the automatic pandas title
plt.xlabel("Item and Period")
plt.ylabel("Buy Volume")
plt.xticks(rotation=45)


```


![img](boxplot for event window.png)

The boxplot above shows the various food groups time period vs the buy volume. The green line represents the median for each group and the whiskers are 1.5 the interquartile range from the edge of the box. As in all box plots, outliers are located outside of the whiskers and are up to the analyst to interpret. In this study, we are choosing to retain the outliers due to the small dataset and that likihood that these outliers are revelant to our research question.

After analyzing for any outliers in our new dataframe, we looked to see if there might be any interaction between food type and period in our dataset prior to any anova by looking at the means. The plot below is a plot of average buy volume for each food before and after Jan 3rd. Since the lines are somewhat parallel and within the same scale, we can roughly assume there is no interaction. However, a two way anova is required to prove that.

```Python
# Plotting the interaction means for the three types of food before and after the period.

means = (
    event_window
    .groupby(['period', 'item_name'])['buy_volume']
    .mean()
    .unstack()
)

# Put Before first
means = means.reindex(['Before', 'After'])
means.head()
print(means)

ax = means.plot(
    marker='o',
    linewidth=2
)

print(ax.get_xticks())
print(ax.get_xticklabels())

ax.set_xticks([0, 1])
ax.set_xticklabels(['Before', 'After'])

plt.title("Mean Buy Volume Before and After January 3, 2026")
plt.xlabel("Period")
plt.ylabel("Mean Buy Volume")
plt.grid(True)
plt.show()
```



![img](Mean Buy Volume Before and After January 3 2026.png)

Finally, we can now analyze our data using a two way anova. First we fit our data to a linear regression model using ordinary least squares (OLS) method that the statsmodels library can use for an ANOVA. Than we use our OLS model for our linear regression as shown below.

```Python
#ordinary least squares model that fits a linear regressio model
model = ols('buy_volume ~ C(period) * C(item_name)',data=event_window).fit()

twoway_anova = sm.stats.anova_lm(model,type=2)
print(twoway_anova)
```

|                        |   df |      sum_sq |     mean_sq |         F |      PR(>F) |
|:-----------------------|-----:|------------:|------------:|----------:|------------:|
| C(period)              |    1 | 3.34835e+12 | 3.34835e+12 |   5.05404 |   0.0307865 |
| C(item_name)           |    2 | 1.08864e+13 | 5.4432e+12  |   8.21603 |   0.00115   |
| C(period):C(item_name) |    2 | 1.50158e+12 | 7.50789e+11 |   1.13325 |   0.333202  |
| Residual               |   36 | 2.38504e+13 | 6.6251e+11  | nan       | nan         |






