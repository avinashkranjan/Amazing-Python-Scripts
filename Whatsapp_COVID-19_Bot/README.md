# WhatsApp COVID-19 Bot

A COVID-19 Bot build using `Twilio API`, that tracks the Number of Infected persons, Recovered Persons and Number of
Total deaths along with the day-to-day increase in the statistics. The information is then updated via WhatsApp.

## Note

The script requires personal info, like `API-Token`, `API-ID`, and `PHONE-NUMBER`
for that reason, a [`.env`](.env.example) file has been used, for more info, see usage.

## Usage

- Setup a Virtual Environment.
- Download dependencies using `pip install -r requirements.txt`.
- Set up an account at [`Twilio`](https://www.twilio.com/). It's Free.
- Follow 
  [this guide](https://medium.com/hackernoon/how-to-send-whatsapp-message-using-python-and-twilio-api-fc63f62154ca)
  for Setting up WhatsApp API.  
- Make a `.env` file similar to `.env.example` file.
- Paste the required information:

    ```text
    SID="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" <ACCOUNT SID goes here>
    TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" <AUTH TOKEN>
    NUM="+91XXXXXXXXXX" <TARGET PHONE NUMBER GOES HERE>
    ```

- The bot script is now ready.
- For scheduling, [`apscheduler`](https://apscheduler.readthedocs.io/en/stable/)
  has been used for cron-style scheduling.
- The script is coded to run the bot once every day.  
- For making your own cron schedule, use this [website](https://crontab.guru/).
- After setting up the Cron Job, run the scheduler script using `python3 schedule.py`.

## Output

![](https://i.postimg.cc/GpmVJrJt/Whats-App-Image-2021-02-27-at-20-18-13.jpg)

Sample Message

```text
Last Updated on: 2021-02-27
Top 3 Indian States sorted by Newly registered cases of COVID-19.
    [Maharashtra]
    |   Total Infected = 68810
    |   New Infections =  3349
    |   Total Recovery = 2017303
    |   New Recovery = 4936
    |   Total Deaths = 52041
    |   New Deaths = 48
    
    [Punjab]
    |   Total Infected = 4222
    |   New Infections =  352
    |   Total Recovery = 170968
    |   New Recovery = 255
    |   Total Deaths = 5814
    |   New Deaths = 15
    
    [Gujarat]
    |   Total Infected = 2136
    |   New Infections =  145
    |   Total Recovery = 262487
    |   New Recovery = 315
    |   Total Deaths = 4408
    |   New Deaths = 0
```

## Author(s)  

Made by [Vybhav Chaturvedi](https://www.linkedin.com/in/vybhav-chaturvedi-0ba82614a/)

### Disclaimer

Kindly follow all the guidelines of Twilio and respect the request rate.

Despite the recent downfall in cases, COVID-19 is still a major threat for all of us, I strongly request you to follow
all the necessary guidelines.
