Setup Reddit bot:
	Go to https://www.reddit.com/prefs/apps, create new app, choose 'script', pick any name you like, set 'redirect uri' to 'http://localhost:8080', put in description something about research purposes.
Edit setup.txt:
	Open 'setup.txt' in this folder.
	Replace 'credentials' with info from app you just created.
	Replace 'subreddits' with list of subreddits you want to use.

Run SubredditExtractor.exe. It will create few files starting with 'OUTPUT'. Congrats, you did it.