# COVID19 STATS APP FOR INDIAN STATES

This project uses the following API for getting the stats
[COVID19 STATS](https://api.covid19india.org/data.json)

## Requirments
- Flask
- ngrok: for getting public URL for your local API else deploy in servers like Heroku
- Facebook page
- Facebook developer account: for connecting backend with chatbot app

## How to use this code ?
- Create app in developer portal and connect with facebook page
  - Obtain app id
  - Generate token for the page you have linked with the app  
- Install flask and other requirements and run the app
- Use ngrok like software for creating public URL
- Add public URL as callback URL in developer portal
- Edit subscription of your added page and tick the following
    - messages
    - messaging_postbacks
    - messaging_referrals
- The verification token for this script is "abc".This will be used for verifying the webhook
- Ensure that you have added the generation token in the step 1 in the code

```ACCESS_TOKEN = "random token"```

Now send a message from messenger from your facebook page and get corresponding stats

![messenger-1](https://user-images.githubusercontent.com/73653978/111796544-4a97fa00-88ee-11eb-9e8a-e22031a6d665.PNG)

![messenger-2](https://user-images.githubusercontent.com/73653978/111796445-318f4900-88ee-11eb-9db0-07bc8c765bae.PNG)

![messenger-3](https://user-images.githubusercontent.com/73653978/111796633-5e436080-88ee-11eb-9f2e-f8e257bf43fb.PNG)

## Author
[Devika S G](https://github.com/dsg1320)
