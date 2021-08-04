
# ITC DATA_MINING

This project is designed to help an indiviudal gather 
information from the popular rating website MetaCritic.com/game.
It enables the user to select different platforms, genres and 
unique timeframes. It returns all usefull information gathered
from each game in a CSV file. 


## Deployment

This program helps the user navigate throught metacritic.com/game to a search page.
It does so by getting input from user on available search parameters such as platform, dates etc.  

This program can be run in two modes:
1. manually (when search_code is not provided)
2. automaticly

When the program is run manually it will help the user find the search page he is looking for by prompting available options.
In auto-mode the user knows which search page is he looking for and knows the code to get there. 
If the code is uknown run the program manually and the search code is the cancatanation of your input.

usage in auto-mode: [program_name] [options]

options:

-search_code / -sc : a sting of ints indicating the search page the user whishes to scrape. 
if the search code is too long the program will use its first n digits. If not provided the program will run on manual mode.

-fetch / -f : int; the number of articles to fetch from the search page. default is 100.
Can be used only in combination with search_code. 

-asc / -a : bool; some search pages allow to sort the results ascending. if a code to such a search page was used asc 
can be chossen as True. default is False. Can be used only in combination with search_code. 

  
## Acknowledgements

 - We would like to thank ITC for their time and tutelage. 

  
## FAQ

#### How does one use your program?

One simply runs main.py and is prompted to answer some questions.
Answer the questions by typing the required numbers. 
These will help narrow down the users search to the exact type
of games to which he is interested in gathering information about.

#### Why does it take longer then usual?

We implemented a sleep function to ensure the program runs smoothly.
This has increased the total running time. 

## ERD

The Database has a few main tables:

Games: This tables has information regarding each game, such as the id, name, main platform, publisher, developer, age rating, number of players and release date. The main platfrom, publisher, developer and age rating are all foreign keys to other tables. 

Publishers: This records all the publishers scraped.

Developers: This records all the developers scraped.

Age Ratings: This records all the age ratings scrapred. 

Consoles: This records the name of all the consoles scraped. 

Scores: This is a table that records the final critic score as well as the final user score. It also records the total number of critic scores and user scores.

Critic Reviews: This tables records the number of positive, mixed and negative critic scores.

User Reviews: This tables records the number of positive, mixed and negative user scores. 

Genres: This records all the genres scraped.

Game to Genres: This is a junction table between games and genres. 

Game to Console: This is a junction table between game and console. 




![alt text](https://github.com/yonatan1988eisenberg/ITC_data_mining_project/blob/2c41e22a8531e9e723915f9db728a5fbf2db29ea/database.PNG)

  
## Authors

- [@yonatan1988eisenberg](https://github.com/yonatan1988eisenberg/ITC_data_mining_project)
- [@Doron-Ben-Chayim](https://github.com/yonatan1988eisenberg/ITC_data_mining_project) 
  
