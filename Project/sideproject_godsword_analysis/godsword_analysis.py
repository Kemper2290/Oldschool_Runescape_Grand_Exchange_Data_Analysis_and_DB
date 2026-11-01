import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import mysql.connector

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
        from godswords_91day
        """

fulldf = pd.read_sql(query,conn)


print(fulldf.head())
print("rows,columns of dataframe: ",fulldf.shape)

# trying it by running in python consol for better interactions and data tracking
fulldf.head()

fulldf.info()
fulldf.describe()

#sanity check to make sure that i have 365 datapoints where 365 datapoints * 6h / 24hr/day = 91.25 days
fulldf.groupby(['item_name'])['item_id'].count()

fulldf['item_name'].unique()

days = np.repeat(np.arange(1,92),4)

GS_blade_df = fulldf.loc[fulldf['item_name']=='Godsword blade'].reset_index()
GS_blade_df = GS_blade_df[GS_blade_df.index<364]
GS_blade_df['days'] = days
GS_blade_df.head()
GS_blade_df.tail()
GS_blade_df.nunique()


Ags_df   = fulldf.loc[fulldf['item_name']=='Armadyl godsword'].reset_index()
Ags_df = Ags_df[Ags_df.index < 364]
Ags_df['days'] = days
Ags_df.head()

Ahilt_df = fulldf.loc[fulldf['item_name']=='Armadyl hilt'].reset_index()
Ahilt_df = Ahilt_df[Ahilt_df.index<364]
Ahilt_df['days'] = days
Ahilt_df.head()

Bgs_df   = fulldf.loc[fulldf['item_name']=='Bandos godsword'].reset_index()
Bgs_df = Bgs_df[Bgs_df.index< 364]
Bgs_df['days'] =days
Bgs_df.head()

Bhilt_df = fulldf.loc[fulldf['item_name']=='Bandos hilt'].reset_index()
Bhilt_df = Bhilt_df[Bhilt_df.index<364]
Bhilt_df['days'] = days
Bhilt_df.head()

Sgs_df   = fulldf.loc[fulldf['item_name']=='Saradomin godsword'].reset_index()
Sgs_df = Sgs_df[Sgs_df.index<364]
Sgs_df['days'] = days
Sgs_df.head()

Shilt_df = fulldf.loc[fulldf['item_name']=='Saradomin hilt'].reset_index()
Shilt_df = Shilt_df[Shilt_df.index < 364]
Shilt_df['days'] = days
Shilt_df.head()

Zgs_df   = fulldf.loc[fulldf['item_name']=='Zamorak godsword'].reset_index()
Zgs_df = Zgs_df[Zgs_df.index< 364]
Zgs_df['days'] = days
Zgs_df.head()

Zhilt_df = fulldf.loc[fulldf['item_name']=='Zamorak hilt'].reset_index()
Zhilt_df = Zhilt_df[Zhilt_df.index<364]
Zhilt_df['days'] = days
Zhilt_df.head()
Zhilt_df.tail()




ax=GS_blade_df.plot.scatter(x='days',y='buy_volume',label='GS_blade_df_buy',color='blue')
GS_blade_df.plot.scatter(x='days',y='sell_volume',label='GS_blade_df_sell',color='purple',ax=ax)

Ags_df.plot.scatter(x='days',y='buy_volume', label='Ags_df',color='orange',ax=ax)
Ags_df.plot.scatter(x='days',y='buy_volume', label='Ags_df',color='orange',ax=ax)

Ahilt_df.plot.scatter(x='days',y='buy_volume',label='Ags_hilt',color='red',ax=ax)
Ahilt_df.plot.scatter(x='days',y='buy_volume',label='Ags_hilt',color='red',ax=ax)

plt.ylabel('buy_volume')
plt.xlabel('days')
plt.show()

fulldf.head(10)
fulldf.info()
fulldf['item_name'].unique()




















