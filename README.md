#Pocket Reading Time Tagger
I wish Pocket estimated the reading time for each article. Fortunately you can manually add tags to each item. So this uses [Pocket-API](https://github.com/rakanalh/pocket-api) to adds reading time estimate tags. Quick and dirty but it works.

Assumes 275wpm, based on [Medium's estimates](https://help.medium.com/hc/en-us/articles/214991667-Read-time). This is easily changed if you read at a different speed.

##Usage
1. Create your [Pocket consumer key](https://getpocket.com/developer/apps/new). To get the access token, you have to authorize the app on your own account.
2. Install [Pocket-API](https://github.com/rakanalh/pocket-api)
`pip install pocket-api`
3. Populate *apikey.txt* with your Consumer Key (on the first line) and Access Token (on the second line). *apikey.txt.sample* has been provided but will not work until you insert your own keys, and remove the *.sample* from the filename.
4. Run the code
`python readingSpeed.py`

