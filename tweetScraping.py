
# Script Author: Martin Beck
# edited by Shivam Balajee

# Imports
import os
import pandas as pd

# Query by text search
# Setting variables to be used in format string command below
tweet_count = 500
text_query = "politics  lang:en"
since_date = "2020-03-01"
until_date = "2020-07-31"

# Using OS library to call CLI commands in Python
os.system('snscrape --jsonl --max-results {} --since {} twitter-search "{} until:{}"> text-query-tweets.json'.format(
    tweet_count, since_date, text_query, until_date))

# Reads the json generated from the CLI command above and creates a pandas dataframe
tweets_df2 = pd.read_json('text-query-tweets.json', lines=True)

# Displays first 5 entries from dataframe
# tweets_df2.head()

# Export dataframe into a CSV
tweets_df2.to_csv('text-query-tweets.csv', sep=',', index=False)

