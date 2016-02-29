----------
In[2]: import pandas as pd

In[3]: import numpy as np

In[4]: data_path = 'E:\\Trash\data\\df-data_twitter_vine\\twitter-vine-clean.tsv.bz2'

In[5]: df = pd.read_csv(data_path, sep='\t', compression='bz2')

----------
How many tweets?:
===================
In[25]: len(df.groupby("tweet_id").tweet_id)

Out[25]: 2128951

----------
How many unique users?:
===================
----------
How many tweets contains more than one URL?:
===================
In[63]: sum(df.groupby('tweet_id')['urls'].apply(lambda g: len(g)>1))

Out[63]: 706

How many tweets are geotagged (have latitude and longitude)?:
===================
In[89]: len(df[(df.geo != 'None')].groupby('tweet_id').tweet_id)

Out[89]: 15564

----------
How many tweets are original (e.g., not retweets)?:
===================
In[90]: len(df[(df.retweeted == False)].groupby('tweet_id').tweet_id)

Out[90]: 2128793

----------
How many tweets for each day? In average?:
===================
In[132]: df[['tweet_id','created_at']].groupby(df.created_at.map(lambda x: x.split('T',1)[0])).count()

Out[126]: 
            tweet_id  created_at
created_at                      

 - 2013-01-28     69123       69123 2013-01-29     98501       98501
 - 2013-01-30     75435       75435 2013-01-31     71642       71642
 - 2013-02-01     75419       75419 2013-02-02     72197       72197
 - 2013-02-03     46374       46374 2013-02-04     34824       34824
 - 2013-02-05     62784       62784 2013-02-06     79157       79157
 - 2013-02-07     72738       72738 2013-02-08     80017       80017
 - 2013-02-09     87639       87639 2013-02-10     79522       79522
 - 2013-02-11     64506       64506 2013-02-12     69265       69265
 - 2013-02-13     75196       75196 2013-02-14     69675       69675
 - 2013-02-15     72621       72621 2013-02-16     78666       78666
 - 2013-02-17     74956       74956 2013-02-18     71359       71359
 - 2013-02-19     70309       70309 2013-02-20     72000       72000
 - 2013-02-21     77571       77571 2013-02-22     80345       80345
 - 2013-02-23     89468       89468 2013-02-24     88286       88286
 - 2013-02-25     70160       70160

In[147]: df[['created_at']].groupby(df.created_at.map(lambda x: x.split('T',1)[0])).count().mean()

Out[141]: 

created_at    73439.827586

----------




Day of the week with highest volume of traffic?:


Which are the most popular user_location?:


Which are the most popular hashtags?:
