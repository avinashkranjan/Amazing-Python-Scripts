import shodan
import requests
import json
import os


print('--------------WELCOME TO THE EASE-OF-USE SHODAN API PROGRAM---------------')
print('--------------------------------------------------------------------------')
print('😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎')

## Checks if there is a stored api key in shodan_api.json
try:
        with open('shodan_api.json') as file:
            api_key = json.load(file)
        print("Successfully loaded pre-saved key")
except:
## If there is no shodan_api.json file, you will be requested to input one
        api_key = input('Please enter your shodan api key to get started: ')
        data = api_key
        with open('shodan_api.json', 'w+') as outfile:
            json.dump(data, outfile, indent=2)
finally:
        print('Starting program.............')
    
## Stores your API key for current session
api = shodan.Shodan(api_key)

## Retrieves IP info from target IP address
def shodan_ip_info():
    x = True  
    while x is True:
        ip_add = input('enter target IP address: ')
        try:
            info = api.host(ip_add)
            ## Saves IP information into shodan_data.json
            with open('shodan_data.json', 'w+') as datafile:
                json.dump(info, datafile, indent=2)    
            print(info)
            print('---------------------------------------------')
            print(f"Output file has been saved at: {os.path.dirname(os.path.abspath(__file__))}\shodan_data.json")    
        
        ## Throws an error if API key is invalid or if target IP has no information
        except shodan.APIError as error:
            print('Error:', error)   
        finally:
        ## Asks user for next steps
            cont_or_exit = str(input('type "main" to go to main menu || type "again" to repeat || type "exit" to exit: '))
            if cont_or_exit in ['Main', 'main', 'MAIN']:
                main()
            elif cont_or_exit in ['Again', 'again', 'AGAIN']:
                x = True
            elif cont_or_exit in ['Exit', 'exit', 'EXIT']:
                x = False
                exit()

## Targets an IP and finds open ports
def shodan_port_info():
    x = True
    while x == True:
        try:
            ip_add = input('enter target IP address: ')
            ## Retrieves Port information from target IP address
            host = requests.get(f"https://internetdb.shodan.io/{ip_add}").json()
            print(host)
            ## Saves Port information into a file called shodan_port_data.json
            with open('shodan_port_data.json', 'w+') as portfile:
                json.dump(host, portfile, indent=2)
            print(f"Output file has been saved at: {os.path.dirname(os.path.abspath(__file__))}\shodan_port_data.json")
        ## No API Key needed for this process, so only notifies user if there was any Port information or not
        except:
            print('No port information for that IP')            
        finally:
        ## Asks user for next steps
            cont_or_exit = str(input('type "main" to go to main menu || type "again" to repeat || type "exit" to exit: '))
            if cont_or_exit in ['Main', 'main', 'MAIN']:
                main()
            elif cont_or_exit in ['Again', 'again', 'AGAIN']:
                x = True
            elif cont_or_exit in ['Exit', 'exit', 'EXIT']:
                x = False
                exit()
                
def main():  
    select = input('Type in 1 for IP address info OR Type in 2 for IP Port Info: ')
    if select == '1':
        shodan_ip_info()
    if select == '2':
        shodan_port_info()
    else:
        print('Did not select an option')
        exit()
        
main()
      
