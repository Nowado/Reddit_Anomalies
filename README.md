Turns out I'm linking this more often than I expected, so I'm adding some general introduction on 'what and why' here.

Idea is as follows: groups of people focused on specific topics need words for expressing their growingly complex thoughts on said topics. Sometimes they invent new words, which is easy to detect, but sometimes they modify meaning of already existing ones (in more or less conscious ways). Given word embeddings are motivated by distributional hypothesis, shift in relative positions of words should correspond to (although it would possibly miss some of) change in meaning.

Motivations for creating tool improving detection of such shifts can be multiple, to name a few: user generated content moderation, marketing/sociological/political monitoring.

I decided to go with political front for PoC. Reasons included already existing infrastructure of highly motivated people, leading for example to relative ease of finding labeled data (whole subreddits dedicated to cataloging other subreddits containing for example hate speech) and possibility to further promote the tool.
That’s probably a good spot to mention content warning: specifically I decided to look for right wing dog whistles, so there’s a lot of hate speech of all sorts in data.

As mentioned in the beginning, it largely exists for transparency, so Jupyter won’t exactly work out of the box (local paths, I’m not allowed to share some specific data and such) and because of that I uploaded it with cells already run. 

Engine creates embeddings, then for words appearing in both referential embeddings (as specified in README) and in subreddits calculates change in distances for each word relative to other words in both groups. Idea being that those shifted the most would point at new meanings.
SubredditExtractor.py will work right away, however it’s pretty boring. README talks about .exe version which I PMed people, since it’s simply the same thing, but standalone.

Most obvious way in which it fails right now is very unusual popularity of words - as you can imagine people don’t exactly setup subreddits with the sole purpose of creating hate speech datasets, but rather simply talk about some topics, which leads to words related to those topics appearing in unusual contexts, because they simply appear more. There’s possibility that simply feeding in more data would fix it (at least to the point of speeding up human work). There’s also of course a chance that it’s a straight up wrong idea and it doesn’t work at all.


# Reddit_Anomalies
SubredditExtractor.py is ready to be made into .exe file for non-technical users. Add praw.ini and (edited) setup.txt to folder created by auto-py-to-exe. Follow README.

Anomalous_tokens currently finds words used unusually given their word2vec representation. Default gensim training settings are same as used for 'English Wikipedia Dump of February 2017' 300 dimensional skipgram with no lemmatization from http://vectors.nlpl.eu (and that's what should be used as reference). Since the goal is to find abnormalities, preprocessing is limited.

ToDo:
- consideration for phrases and words popularity
