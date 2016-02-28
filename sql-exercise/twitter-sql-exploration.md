In[2]: import pandas as pd
In[3]: import numpy as np
In[4]: data_path = 'E:\\Trash\data\\df-data_twitter_vine\\twitter-vine-clean.tsv.bz2'
In[5]: df = pd.read_csv(data_path, sep='\t', compression='bz2')


How many tweets?:
In[25]: len(df.groupby("tweet_id").tweet_id)
Out[25]: 2128951

How many unique users?:


How many tweets contains more than one URL?:
In[63]: sum(df.groupby('tweet_id')['urls'].apply(lambda g: len(g)>1))
Out[63]: 706

How many tweets are geotagged (have latitude and longitude)?:


How many tweets are original (e.g., not retweets)?:


How many tweets for each day? In average?:


Day of the week with highest volume of traffic?:


Which are the most popular user_location?:


Which are the most popular hashtags?:

