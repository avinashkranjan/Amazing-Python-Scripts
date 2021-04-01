# Cryptocurrency Wallet
This is a simple Cryptocurrency wallet made with the help of python and its associate libraries and PubNub for the api calls. In this project it is shown how a cryptocurrency wallet keep track od the user transaction and this total project is build on the basis of Blockchain where the mining is happening and the time is dynamically adjusted with mean time of 4sec/ transaction speed. If sometime the transaction time is increased due to comparatively easy Proof Of Work (PoW) to agree to the consensus in the next transaction the complexity is increased by 1 zero(0) in front the Nonce. The program is build in such a way that it can simulate real life Blockchain ledger keeping by updating the ledger to each and every Node of the Network. In this program also a new instance of the current blockchain can be created and from that instance blocks can be mined and transactions can be made. 

## Setup instructions
There are two ways to run it on your Linux, MAC or Windows

- To run this program at first you have to create a virtual environment in your pc
- Then you have to go to the core backend folder and run the app.py file
- Running the app.py file will start the first instance for the flask program 
- After running the first instance we have to make some demo transaction by running the test.app in the scripts folder inside the backend folder
- After we have done some demo transaction we can look at the blockchain in the http://localhost:5000 by typing http://localhost:5000/blockchain in the browser and if you want to mine some demo blocks through the weblink then just type http://localhost:5000/blockchain/mine
- Now as we have some demo transaction and the link we can go for the multiple instance aspect of the program i.e. the ledger keeping of different Cryptocurrency Wallet addresses
- For this on windows machine we have to type $env:PEER = 'True'; python -m backend.app 
- By doing  this your program will be running more than 1 instance which will be updated simultaneously and will be able to perform mining separately.
## Requirements:
- Python3
- Else libraries are on the Requirements.txt file

Click on the Click Here to see the Cryptocurrency Wallet  on YouTube.

| Name of Script | YouTube Link |  Author |
| --- | --- | ---  
| Cryptocurrency Wallet | [Click Here](https://youtu.be/BU7nVBDtDpM)| [Arnab Ray](https://github.com/Arnab11917676) | 
## Output

![image](https://user-images.githubusercontent.com/59610398/113293398-55ea1d00-9313-11eb-9645-b186a88a9eda.png)
![image](https://user-images.githubusercontent.com/59610398/113293431-5f738500-9313-11eb-93f8-f759796b206d.png)
![image](https://user-images.githubusercontent.com/59610398/113293451-67332980-9313-11eb-8608-5e63fa4626a9.png)





## Author(s)

- Arnab Ray (Arnab11917676)
