import json
import pandas as pd
#from textblob import TextBlob

def read_json(json_file: str)->list:
    """
    json file reader to open and read json files into a list
    Args:
    -----
    json_file: str - path of a json file
    
    Returns
    -------
    length of the json file and a list of json
    """
    
    tweets_data = []
    for tweets in open(json_file,'r'):
        tweets_data.append(json.loads(tweets))
    
    
    return len(tweets_data), tweets_data

class TweetDfExtractor:
    """
    this function will parse tweets json into a pandas dataframe
    
    Return
    ------
    dataframe
    """
    def __init__(self, tweets_list):
        
        self.tweets_list = tweets_list

    # an example function
    def find_statuses_count(self)->list:
        #statuses_count 
        pass
    def find_full_text(self)->list:
        text = [x.get('retweeted_status', {}).get('extended_tweet',{}).get('full_text', '') \
            for x in self.tweets_list]
        return text
       
    
    def find_sentiments(self, text)->list:
        
        #return polarity, self.subjectivity
        pass

    def find_created_time(self)->list:
        created_time = [x.get('created_at', None) for x in self.tweets_list]
        return created_time

    def find_source(self)->list:
        #source = 

        #return source
        pass

    def find_screen_name(self)->list:
        #screen_name =
        pass

    def find_followers_count(self)->list:
        followers_count = [x.get('user', {}).get('followers_count', 0) for x in self.tweets_list]
        return followers_count

    def find_friends_count(self)->list:
        friends_count =  [x.get('user', {}).get('friends_count', 0) for x in self.tweets_list]
        return friends_count

    def is_sensitive(self)->list:
        is_sensitive = [x.get('possibly_sensitive', None) for x in self.tweets_list]

        return is_sensitive

    def find_favourite_count(self)->list:
         fav_count = [x.get('retweeted_status', {}).get('favorite_count', 0) for x in self.tweets_list]
         return fav_count
    def find_retweet_count(self)->list:
        #retweet_count =
        pass

    def find_hashtags(self)->list:
        #hashtags =
        pass
    def find_mentions(self)->list:
        #mentions =
        pass
    
    def find_location(self)->list:
        location = [x.get('user', {}).get('location', None) for x in self.tweets_list]
        return location
    
    def get_tweet_df(self, save=False)->pd.DataFrame:
        """required column to be generated you should be creative and add more features"""
        
        columns = ['created_at', 'source', 'original_text','polarity','subjectivity', 'lang', 'favorite_count', 'retweet_count', 
            'original_author', 'followers_count','friends_count','possibly_sensitive', 'hashtags', 'user_mentions', 'place']
        
        created_at = self.find_created_time()
        source = self.find_source()
        text = self.find_full_text()
        polarity, subjectivity = self.find_sentiments(text)
        lang = self.find_lang()
        fav_count = self.find_favourite_count()
        retweet_count = self.find_retweet_count()
        screen_name = self.find_screen_name()
        follower_count = self.find_followers_count()
        friends_count = self.find_friends_count()
        sensitivity = self.is_sensitive()
        hashtags = self.find_hashtags()
        mentions = self.find_mentions()
        location = self.find_location()
        data = zip(created_at, source, text, polarity, subjectivity, lang, fav_count, retweet_count, screen_name, follower_count, friends_count, sensitivity, hashtags, mentions, location)
        df = pd.DataFrame(data=data, columns=columns)

        if save:
            df.to_csv('processed_tweet_data.csv', index=False)
            print('File Successfully Saved.!!!')
        
        return df

                
if __name__ == "__main__":
    # required column to be generated you should be creative and add more features
    columns = ['created_at', 'source', 'original_text','clean_text', 'sentiment','polarity','subjectivity', 'lang', 'favorite_count', 'retweet_count', 
    'original_author', 'screen_count', 'followers_count','friends_count','possibly_sensitive', 'hashtags', 'user_mentions', 'place', 'place_coord_boundaries']
    _, tweet_list = read_json("../Economic_Twitter_Data.json")
    tweet = TweetDfExtractor(tweet_list)
    tweet_df = tweet.get_tweet_df() 

    # use all defined functions to generate a dataframe with the specified columns above

    
