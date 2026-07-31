
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import mysql.connector
import matplotlib.dates as mdates

#anova libraries
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import scipy

pd.set_option('display.max_columns',None)
pd.set_option('display.width',1000)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "Dubclub2464!",
    database = "osrs_ge"
)

cursor = conn.cursor()

query = """
        select *
        from venezuela_bots
"""

fulldf = pd.read_sql(query,conn)
#fulldf.to_csv('venezuela_bots_csv',index=False)
fulldf['spread'] = fulldf['avg_buy_price']-fulldf['avg_sell_price']


fulldf.head()
print(fulldf.head().to_markdown(index=False))

fulldf.info()
data_summary = fulldf.dtypes.to_frame("Data Type")
print(data_summary.to_markdown())

fulldf.describe()
print(fulldf.describe().to_markdown(index=True))


fulldf.groupby(['item_name'])['item_id'].count()
fulldf.groupby(['item_name'])['item_id'].describe()
print(fulldf.groupby(['item_name'])['item_id'].describe().to_markdown(index=True))


fulldf['item_name'].unique()

days = np.arange(1,366,1)
print(days)
print(len(days))

#-----------------------
# Seperating Dataframes
#-----------------------

# item_name
# Anglerfish                365
# Blood rune                365
# Cosmic rune               365
# Lobster                   365
# Prayer potion(4)          365
# Ranging potion(4)         365
# Saradomin brew(4)         365
# Shark                     365
# Soul rune                 365
# Super combat potion(4)    365
# Super restore(4)          365
# Zulrah's scales           365


#common food
lobsterdf = fulldf.loc[fulldf['item_name']=='Lobster'].reset_index()
lobsterdf['days'] = days
lobsterdf.head()
print(lobsterdf.head().to_markdown(index=False))
lobsterdf.tail()
print(lobsterdf.tail().to_markdown(index=False))

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

# Common Potions




#---------------------------------------
#plotting data for buy and sell volume for food
#---------------------------------------

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


#----------------------------------------
# Plotting data for buy volume for food
#----------------------------------------


#ax=lobsterdf.plot('timestamp','sell_volume',label='lobster-SellVol',color='orange',xlim=('2025-12-15','2026-01-31'))
ax=lobsterdf.plot('timestamp','buy_volume',label='lobster-BuyVol',color ='peru',xlim=('2025-12-15','2026-01-31'))
sharkdf.plot('timestamp','buy_volume',label='shark-BuyVol',color = 'saddlebrown',ax=ax)
anglerfishdf.plot('timestamp','buy_volume',label='anglerfish-BuyVol',color = 'lightgreen',ax=ax)

ax.xaxis.set_major_locator(mdates.DayLocator()) # Label every day
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d')) # Format as Dec 01, Dec 02, or 12-01,12-02 ...
plt.xticks(rotation=45)

#-----------------------------------------
#plotting data for avg buy and sell price for food
#----------------------------------------

ax=lobsterdf.plot('timestamp','avg_sell_price',label='lobster-SellPrice',color='orange',xlim=('2025-12-15','2026-01-31'),linestyle='--')
lobsterdf.plot('timestamp','avg_buy_price',label='lobster-BuyPrice',color ='peru',ax=ax,linestyle='-')

sharkdf.plot('timestamp','avg_sell_price',label = 'shark-SellPrice',color='sandybrown',ax=ax,linestyle='--')
sharkdf.plot('timestamp','avg_buy_price',label='shark-BuyPrice',color = 'saddlebrown',ax=ax,linestyle='-')
ax=sharkdf.plot('timestamp','avg_sell_price',label = 'shark-SellPrice',color='sandybrown',xlim=('2025-12-15','2026-01-31'),linestyle='--')
sharkdf.plot('timestamp','avg_buy_price',label='shark-BuyPrice',color = 'saddlebrown',ax=ax,linestyle='-')

anglerfishdf.plot('timestamp','avg_sell_price',label= 'anglerfish-SellPrice',color='green',ax=ax,linestyle='--')
anglerfishdf.plot('timestamp','avg_buy_price',label='anglerfish-BuyPrice',color = 'lightgreen',ax=ax,linestyle='-')
ax=anglerfishdf.plot('timestamp','avg_sell_price',label= 'anglerfish-SellPrice',color='green',xlim=('2025-12-15','2026-01-31'),linestyle='--')
anglerfishdf.plot('timestamp','avg_buy_price',label='anglerfish-BuyPrice',color = 'lightgreen',ax=ax,linestyle='-')

ax.xaxis.set_major_locator(mdates.DayLocator()) # Label every day
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d')) # Format as Dec 01, Dec 02, or 12-01,12-02 ...
plt.xticks(rotation=45)
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Buy and Sell Price of Cooked Food')



#--------------------------------------------------------
#plotting data for avg buy and sell volume of raw food
#--------------------------------------------------------

ax=raw_lobsterdf.plot('timestamp','sell_volume',label='raw-lobster-SellVol',color='orange',xlim=('2025-12-15','2026-01-31'),linestyle='--')
raw_lobsterdf.plot('timestamp','buy_volume',label='raw-lobster-BuyVol',color ='peru',ax=ax,linestyle='-')

raw_sharkdf.plot('timestamp','sell_volume',label = 'raw-shark-SellVol',color='brown',ax=ax,linestyle='--')
raw_sharkdf.plot('timestamp','buy_volume',label='raw-shark-BuyVol',color = 'saddlebrown',ax=ax,linestyle='-')

raw_anglerfishdf.plot('timestamp','sell_volume',label= 'raw-anglerfish-SellVol',color='green',ax=ax,linestyle='--')
raw_anglerfishdf.plot('timestamp','buy_volume',label='raw-anglerfish-BuyVol',color = 'lightgreen',ax=ax,linestyle='-')

ax.xaxis.set_major_locator(mdates.DayLocator()) # Label every day
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d')) # Format as Dec 01, Dec 02, or 12-01,12-02 ...
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Buy and Sell Volume of Raw Food')

#-----------------------------------------
#plotting data for avg buy and sell price for raw food
#----------------------------------------

ax=raw_lobsterdf.plot('timestamp','avg_sell_price',label='raw-lobster-SellPrice',color='orange',xlim=('2025-12-15','2026-01-31'),linestyle='--')
raw_lobsterdf.plot('timestamp','avg_buy_price',label='raw-lobster-BuyPrice',color ='peru',ax=ax,linestyle='-')

raw_sharkdf.plot('timestamp','avg_sell_price',label = 'raw-shark-SellPrice',color='sandybrown',ax=ax,linestyle='--')
raw_sharkdf.plot('timestamp','avg_buy_price',label='raw-shark-BuyPrice',color = 'saddlebrown',ax=ax,linestyle='-')

raw_anglerfishdf.plot('timestamp','avg_sell_price',label= 'raw-anglerfish-SellPrice',color='green',ax=ax,linestyle='--')
raw_anglerfishdf.plot('timestamp','avg_buy_price',label='raw-anglerfish-BuyPrice',color = 'lightgreen',ax=ax,linestyle='-')

ax.xaxis.set_major_locator(mdates.DayLocator()) # Label every day
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d')) # Format as Dec 01, Dec 02, or 12-01,12-02 ...
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Buy and Sell Price of Raw Food')




#---------------------------------------------------------------
# Plotting data for buy and sell volume for cook and raw food
#----------------------------------------------------------------

ax=lobsterdf.plot('timestamp','sell_volume',label='lobster-SellVol',color='orange',xlim=('2025-12-15','2026-01-31'))
lobsterdf.plot('timestamp','buy_volume',label='lobster-BuyVol',color ='peru',ax=ax)

sharkdf.plot('timestamp','sell_volume',label = 'shark-SellVol',color='sandybrown',ax=ax)
sharkdf.plot('timestamp','buy_volume',label='shark-BuyVol',color = 'saddlebrown',ax=ax)

anglerfishdf.plot('timestamp','sell_volume',label= 'anglerfish-SellVol',color='green',ax=ax)
anglerfishdf.plot('timestamp','buy_volume',label='anglerfish-BuyVol',color = 'lightgreen',ax=ax)
#---
raw_lobsterdf.plot('timestamp','sell_volume',label='raw-lobster-SellVol',ax=ax)
raw_lobsterdf.plot('timestamp','buy_volume',label='raw-lobster-BuyVol',color ='peru',ax=ax)

raw_sharkdf.plot('timestamp','sell_volume',label = 'raw-shark-SellVol',ax=ax)
raw_sharkdf.plot('timestamp','buy_volume',label='raw-shark-BuyVol',ax=ax)

raw_anglerfishdf.plot('timestamp','sell_volume',label= 'raw-anglerfish-SellVol',ax=ax)
raw_anglerfishdf.plot('timestamp','buy_volume',label='raw-anglerfish-BuyVol',ax=ax)

ax.xaxis.set_major_locator(mdates.DayLocator()) # Label every day
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d')) # Format as Dec 01, Dec 02, or 12-01,12-02 ...
plt.xticks(rotation=45)


#---------------------------------------------------------------------------------------------------
# Performing an two way anova for the cooked food buy volumes where dependent variable is buy volume
#   and indepenent categorical data is week before jan 3rd and week after 3rd since time is not continous
#----------------------------------------------------------------------------------------------------

food_df = pd.concat([lobsterdf,sharkdf,anglerfishdf],axis=0,ignore_index=True)
food_df['timestamp'] = pd.to_datetime(food_df['timestamp'])

event_date = pd.Timestamp("2026-01-03")
event_window = food_df[
    (food_df['timestamp'] >= event_date - pd.Timedelta(days=7)) &
    (food_df['timestamp'] <= event_date + pd.Timedelta(days=6))].copy()

event_window['period'] = 'After'
event_window.loc[event_window['timestamp'] < event_date,'period'] = 'Before'
#event_window["spread"] = event_window["avg_buy_price"] - event_window["avg_sell_price"]


food_df.head()
food_df.tail()

event_window.head()
print(event_window.head().to_markdown(index=False))
event_window.tail()
print(event_window[['item_name','timestamp','period']])

#showing the descriptives of the event_window
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
print(summary.to_markdown())

print(summary.to_markdown(index=False))

# Boxplot
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

#ordinary least squares model that fits a linear regressio model
model = ols('buy_volume ~ C(period) * C(item_name)',data=event_window).fit()

twoway_anova = sm.stats.anova_lm(model,type=2)
print(twoway_anova.to_markdown())

# This means that there is a difference between in buy_volume between two volumes but since we only have two
#   categorical variables we dont need to run a post hoc test for this variable. However, since the p-value
#   item_name is less than .05 we know there is a difference between
#
# df        sum_sq       mean_sq         F    PR(>F)
# C(period)                1.0  3.348351e+12  3.348351e+12  5.054040  0.030787
# C(item_name)             2.0  1.088641e+13  5.443203e+12  8.216034  0.001150
# C(period):C(item_name)   2.0  1.501578e+12  7.507891e+11  1.133250  0.333202
# Residual                36.0  2.385035e+13  6.625098e+11       NaN       NaN
#


#checking the residuals from the anova model to check that they are approximately normal

residuals = model.resid

print(type(model.resid))
print(model.resid.head())
print(model.resid.describe())
print(model.resid.median())
print(residuals.dtype) #since the median >mean the data is right skewed
print(len(residuals))
print(residuals.nunique())
print(residuals.min())
print(residuals.max())
print(type(residuals))
print(residuals.shape)

#W stat tels how similar data is to normal distribution,  1 = highly normal,
# p value  tells statistical significance where  p<.05 means data is not normal
W_stat,W_p = scipy.stats.shapiro(residuals)
print(W_stat,W_p)

#qq_plot
scipy.stats.probplot(residuals,dist="norm",plot=plt)
plt.show()

plt.hist(residuals,bins=10)
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.title("Distribution of ANOVA Residuals")
plt.show()


#inconclusion the data is nonnormally distributed from the shapiro wilks test where the pvalue is <.05.
#   additionally we visuallized the data with a qqplot and a histogram plot. the qqplot showed us that
#   the data is slightly not normal towards the right side of the plot by the grand deviations in the plot
#   to investigate it further, we plotted a histogram plot where it showed us the data is skewed.However,
#   based off of our small amount of data and the typical dramatic spikes in volumes in the GE, we are going
#   to maintain that the data is normally distributed since our sample size is small and the chaotic nature
#   of buy volume in ge. additionally the data looks approximately normal.


#check the equal variance since ANOVA assumes equal variance
event_window.head()

l_stat, l_p = scipy.stats.levene(
    event_window.loc[event_window.item_name == "Shark","buy_volume"],
    event_window.loc[event_window.item_name == "Lobster","buy_volume"],
    event_window.loc[event_window.item_name == "Anglerfish",'buy_volume']
)
print(l_stat,l_p) #p value is >.05 meaning variances are not significantly different so the anova is okay



#-----------------------------------------------------------------------
# Analyze the difference in population before and after the bombing
#------------------------------------------------------------------------

prior_date = pd.read_sql(
    """
    select *,date(timestamp) as `date`
    from player_count
    WHERE timestamp between '2026-01-03' - interval 7 day and '2026-01-02 23:59:59'
    """,conn
)

prior_date

after_date = pd.read_sql(
    """
    select *,date(timestamp) as `date`
    from player_count
    where timestamp between '2026-01-03' and '2026-01-03' + interval 6 day
    """,conn
)

after_date

event_window.head()
event_window.timestamp.min()
event_window['timestamp'].max()

# confirmating that the data is normal and equal variance

tl_stat,tl_pvalue = scipy.stats.levene(prior_date.player_count,after_date.player_count)
print(f'tl_stat = {tl_stat:.4f}, tl_pvalue = {tl_pvalue:.4f}')
alpha =.05
if tl_pvalue < alpha:
    print("Reject the null hypothesis: Variances are NOT equal.")
else:
    print("Fail to reject the null hypothesis: Variances ARE equal.")


t_stat,t_pvalue = scipy.stats.ttest_ind(prior_date['player_count'],after_date['player_count'],equal_var=True) # since pvalue is >.05 , reject null hypothesis and variacnes are equal

print(f"t = {t_stat:.3f}, t_pvalue = {t_pvalue:.4f}")



#normality check here

W_before,W_before_pvalue = scipy.stats.shapiro(prior_date.player_count)
W_after,W_after_pvalue = scipy.stats.shapiro(after_date.player_count)

print(f"Before: W = {W_before:.3f}, p = {W_before_pvalue:.4f}")
print(f"After : W = {W_after:.3f}, p = {W_after_pvalue:.4f}")

scipy.stats.probplot(prior_date.player_count,dist='norm',plot=plt)
plt.title("Q-Q Plot: Player Population Before Jan. 3")

scipy.stats.probplot(after_date.player_count,dist='norm',plot=plt)
plt.title("Q-Q Plot: Player Population After Jan. 3")


plt.hist(prior_date.player_count,bins=20)
plt.title("Player Population Before Jan. 3")
plt.xlabel("Player Population")
plt.ylabel("Frequency")


plt.hist(after_date.player_count,bins=20)
plt.title("Player Population After Jan. 3")
plt.xlabel("Player Population")
plt.ylabel("Frequency")


# running a mann-whitney u test to compare to indepent t test since the data is likely non normal at this data size

MWU_stat, MWU_pvalue = scipy.stats.mannwhitneyu(prior_date.player_count,after_date.player_count,alternative='two-sided')

print(f"MWU_stat = {MWU_stat}, MWU_pvalue = {MWU_pvalue}")
#MWU_stat = 10211.0, MWU_pvalue = 0.013678399414026276 the player count between the two dates is significantly different








