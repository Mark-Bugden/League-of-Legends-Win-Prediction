## Data collection through the RIOT games API

The iPython notebook in this folder accesses the RIOT games API and aggregates data from ranked games in solo queue. The main output of the notebook is the 'ranked_matches.csv' file containing information on ranked games. This will be the input file for the Machine Learning program I will have in the parent folder. 


NOTE: The API client is currently experiencing some technical difficulties. In particular, the V5 Match server is having problems. I managed to get some match data to start testing and working with, but if I want actual results I will need to collect a lot more data, which will require the server to be operational again.

NOTE: If you want to reproduce this yourself, you will need an API key from the RIOT games developer portal: https://developer.riotgames.com/
It's very easy to get one. Once you have it, you simply include the key in a text file 'api_key.txt' in this folder, and the getAPI_key() function will access it.
