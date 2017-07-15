# Pocket Reading Time Tagger
I wish Pocket estimated the reading time for each article. Fortunately you can manually add tags to each item. So this uses [Pocket-API](https://github.com/rakanalh/pocket-api) to adds reading time estimate tags to the last 20 items added to Pocket. Quick and dirty but it works.

Credit where it's due: This is similar to [msramalho's reading time estimator](https://github.com/msramalho/Pocket-ReadingTime-Estimation-Visualization). Msramalho's takes the link from Pocket, downloads and parses the HTML, and submits to an external API ([http://niram.org/read/](http://niram.org/read/)). This implementation simply uses the wordcount provided by Pocket API, divided by an assumed reading speed of 275 words per minute (which itself is based on [Medium's estimates](https://help.medium.com/hc/en-us/articles/214991667-Read-time). This is easily changed if you read at a different speed.)

## Usage
1. Create your [Pocket consumer key](https://getpocket.com/developer/apps/new). To get the access token, you have to authorize the app on your own account.
2. Install [Pocket-API](https://github.com/rakanalh/pocket-api)
`pip install pocket-api`
3. Populate *apikey.txt* with your Consumer Key (on the first line) and Access Token (on the second line). *apikey.txt.sample* has been provided but will not work until you insert your own keys, and remove the *.sample* from the filename.
4. Run the code
`python readingSpeed.py`

