import pandas as pd
import numpy as np
data_path = 'E:\\Trash\data\\df-data_twitter_vine\\twitter-vine-clean.tsv.bz2'
len(df.index)
list(df.columns.values)
df
df.tail(5)
df.tweet_id.count()
df.groupby('user_id').user_id.nunique()
df.groupby('user_id').user_id.count
df2 = pd.read_csv(data_path, sep='\t', compression='bz2', names=["tweet_id"])
df2.tweet_id.count()
df2.groupby("tweet_id").tweet_id.count()
len(df2.groupby("tweet_id").tweet_id)
df.head (5)
df2.head (5)
lent(df.groupby("tweet_id").tweet_id)
len(df.groupby("tweet_id").tweet_id)
df.user_id.head(1000)
df.user_id.tail(1000)
len(df.groupby('user_id').user_id)
sum(df.text.str.count('http')>1)
df.urls(5)
df.urls
df.text
df.urls.count()>1
sum(df.urls.count()>1)
[elem for elem in df.urls if len(elem) > 1]
[elem for elem in df.urls if len(elem) > 1].count()
len([elem for elem in df.urls if len(elem) > 1])
g.filter(lambda x: len(x) > 1)
g.filter(lambda x: len(x.urls) > 1)
g.filter(lambda x: x["urls"].sum() > 1)
var g2 = g.filter(lambda x: x["urls"].sum() > 1)
g2 = g.filter(lambda x: x["urls"].sum() > 1)
g = df.groupby('tweet_id')
g.head(100)
g.head(5)
df.groupby('tweet_id').head(5)
df.urls.head(5)
df.groupby('tweet_id')
df.groupby('tweet_id').tweet_id
df.groupby('tweet_id').tweet_id.head(5)
df.groupby('user_id').user_id
df.groupby('user_id').user_id.head()
df.groupby('user_id').user_id.count()
df.groupby('tweet_id')['urls'].apply(lambda g: len(g)>1)
print 1
sum(df.groupby('tweet_id')['urls'].apply(lambda g: len(g)>1))
df.geo.head(5)
df.geo.head(100)
df.geo.apply(lambda g: g != 'None')
sum(df.geo.apply(lambda g: g != 'None'))
df.geo.filter(lambda g: g != 'None')
len([x for x in df.retweeted if x == False])
len([x for x in df.groupby("tweet_id").retweeted if x == False])
[x for x in df if x.geo != 'None']
[x for x in df.groupby("tweet_id").geo if x != 'None']
len([x for x in df.groupby("tweet_id").geo if x != 'None'])
len([x for x in df.geo if x != 'None'])
[x for x in df.geo if x != 'None']
[x for x in df["geo","tweet_id"] if x != 'None']
df["geo","tweet_id"]
df["geo,tweet_id"]
sum(df.retweetedw.apply(lambda g: g != 'False'))
sum(df.retweetedw.apply(lambda g: g != False))
sum(df.retweeted.apply(lambda g: g != False))
sum(df.retweeted.apply(lambda g: g == False))
sum(df.groupby("tweet_id")['retweeted'].apply(lambda g: g == False))
len(df[(df.geo != 'None')].groupby('tweet_id').tweet_id)
len(df[(df.retweeted == False)].groupby('tweet_id').tweet_id)
df.groupby([df.tweet_id, df.created_at])
df.groupby([df.tweet_id, df.created_at]).tweet_id
df.groupby([df.tweet_id, df.created_at]).count()
df.created_at.str.split('T',1).tolist()
df.groupby([df.tweet_id, df.created_at.str.split('T',1)[0]]).count()
df.created_at.str.split('T',1)[0]
df.created_at.str.split('T',1)[0][0]
df.groupby([df.tweet_id, df.created_at.str.split('T',1)[0][0]]).count()
df.groupby(df.created_at), level='date')
df.groupby(df.created_at, level='date')
df.groupby([df.tweet_id, df.created_at.map(lambda x: x.date)]).count()
df.groupby(df.created_at.map(lambda x: x.date)).count()
df.groupby(df.created_at.map(lambda x: x.split('T'))).count()
df.groupby(df.created_at.map(lambda x: x.str.split('T',1)[0][0])).count()
df.groupby(df.created_at.map(lambda x: x.split('T',1)[0])
df.groupby(df.created_at.map(lambda x: x.split('T',1)[0]).tweet_id
df.groupby(df.created_at.map(lambda x: x.split('T',1)[0][0]).tweet_id
df.groupby(df.created_at.map(lambda x: x.split('T',1)).tweet_id
df.created_at.map(lambda x: x.split('T',1)
df.created_at.map(lambda x: x.split('T',1))
df.groupby(df.created_at.map(lambda x: x.split('T',1).tolist()[0][0]).tweet_id
)
df.groupby(df.created_at.map(lambda x: x.split('T',1).tolist()[0][0]))
df.groupby(df.created_at.map(lambda x: x.split('T',1)[0][0]))
df.groupby(df.created_at.map(lambda x: x.split('T',1)[0]))
df.groupby(df.created_at.map(lambda x: x.split('T',1)[0])).tweet_id
df.groupby(df.created_at.map(lambda x: x.split('T',1)[0][0])).tweet_id
df.groupby(df.created_at.map(lambda x: x.split('T',1)[0][0])).count()
df.groupby([df.tweet_id, df.created_at.map(lambda x: x.split('T',1)[0])]).count()
df.groupby(df.tweet_id).groupby(df.created_at.map(lambda x: x.split('T',1)[0])).count()
df.groupby(df.created_at.map(lambda x: x.split('T',1)[0])).count()
df.groupby(df.created_at.map(lambda x: x.split('T',1)[0])).agg(['mean', 'count'])
df.groupby(df.created_at.map(lambda x: x.split('T',1)[0])).agg(['average'])
df.groupby(df.created_at.map(lambda x: x.split('T',1)[0])).agg(['count'])
df.groupby(df.created_at.map(lambda x: x.split('T',1)[0])).agg(['tweet_id','count'])
df['tweet_id','created_at'].groupby(df.created_at.map(lambda x: x.split('T',1)[0])).count()
df[['tweet_id','created_at']].groupby([df.tweet_id,df.created_at.map(lambda x: x.split('T',1)[0])]).count()
df[['tweet_id','created_at']].groupby(df.created_at.map(lambda x: x.split('T',1)[0])).mean(0)
df[['tweet_id','created_at']].groupby(df.created_at.map(lambda x: x.split('T',1)[0])).count()
df[['tweet_id','created_at']].groupby(df.created_at.map(lambda x: x.split('T',1)[0])).count(tweet_id)
df[['tweet_id','created_at']].groupby(df.created_at.map(lambda x: x.split('T',1)[0])).count("tweet_id")
df[['tweet_id','created_at']].groupby(df.created_at.map(lambda x: x.split('T',1)[0])).map(lambda x: x.tweet_id)
df[['tweet_id','created_at']].groupby(df.created_at.map(lambda x: x.split('T',1)[0])).mean()
df[['created_at']].groupby(df.created_at.map(lambda x: x.split('T',1)[0])).mean(0)
avg(df[['created_at']].groupby(df.created_at.map(lambda x: x.split('T',1)[0])))
df[['created_at']].groupby(df.created_at.map(lambda x: x.split('T',1)[0]))\
df[['created_at']].groupby(df.created_at.map(lambda x: x.split('T',1)[0]))
df[['created_at']].groupby(df.created_at.map(lambda x: x.split('T',1)[0])).count()
df[['created_at']].groupby(df.created_at.map(lambda x: x.split('T',1)[0])).mean()
df[['created_at']].groupby(df.created_at.map(lambda x: x.split('T',1)[0])).count().mean()
 import pandas as pd
 import numpy as np
from IPython.display import display
import warnings
warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', 100)
data_path = 'E:\Trash\data\df-data_twitter_vine\twitter-vine-clean.tsv.bz2'
 df = pd.read_csv(data_path, sep='\t', compression='bz2')
data_path = 'E:\\Trash\\data\\df-data_twitter_vine\\twitter-vine-clean.tsv.bz2'
df = pd.read_csv(data_path, sep='\t', compression='bz2')
df[["created_at", "user_id", "no_followers", "no_tweets", "no_tweets_with_retweets"]].head(10)
df[["created_at", "user_id"]].head(10)
df[["created_at", "user_id", "no_followers", "no_tweets"]].head(10)
df[["created_at", "user_id", "no_followers"]].head(10)
df[["created_at", "user_id", "no_tweets", "no_tweets_with_retweets"]].head(10)
print(rawdf.shape)
print('See number of rows and number of columns:')
print('See number of rows and number of columns:')
print(df.shape)
print('See the top 5 lines:')
df.head(5)
