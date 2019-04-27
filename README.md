# Reddit_Anomalies
SubredditExtractor.py is ready to be made into .exe file for non-technical users. Add praw.ini and (edited) setup.txt to folder created by auto-py-to-exe. Follow README.

Anomalous_tokens currently finds words used unusually given their word2vec representation. Default gensim training settings are same as used for 'English Wikipedia Dump of February 2017' 300 dimensional skipgram with no lemmatization from http://vectors.nlpl.eu (and that's what should be used as reference). Since the goal is to find abnormalities, preprocessing is limited.

ToDo:
- consideration for phrases and words popularity
