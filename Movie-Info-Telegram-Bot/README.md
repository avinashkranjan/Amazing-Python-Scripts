# Movie Info Telegram Bot

## Description
A telegram Bot made using python which scrapes IMDb website and has the following functionalities
1. Replies to a movie name with genre and rating of the movie
2. Replies to a genre with a list of top movies and tv shows belonging to that genre

## Setup Instructions

1. Install required packages:

       pip install -r requirements.txt

2. Create a bot in telegram:

       1. Go to @BotFather and click /start and type /newbot and give it a name. 
       2. Choose a username and get the token 
3. Paste the token in a .env file (Take [.env.example](.env.example) as an example) 

4. Run the python script to start the bot

5. Type /start command to start conversation with the chatbot.

6. Type /name <movie_name> to get the genre and Rating of the movie. The bot replies with atmost three results.
7. Type /genre \<genre> to get a list of movies and TV shows belonging to that genres

## Output

### /start command

<img src="https://i.ibb.co/jwpJHKX/start.png">

### /name command

<img src="https://i.ibb.co/FzrGjSQ/movie.png">

### /genre command

<img src="https://i.ibb.co/VJQy108/genre.png">

## Author
 
[Aishwarya A J](https://github.com/aish2002)
