import shodan
import requests

print('---------WELCOME TO THE EASE-OF-USE SHODAN API PROGRAM--------------------')
print('--------------------------------------------------------------------------')

## Stores Shodan API key for use in the program
api_key = input('Please enter your shodan api key to get started: ')
api = shodan.Shodan(api_key)

## Uses Shodan IP information API
def shodan_ip_info():
    x = True  
    while x is True:
        ip_add = input('enter ip: ')
        try:
            info = api.host(ip_add)
            print(info)
            print('---------------------------------------------')
        except:
            print('No information for that IP or invalid API key')            
        finally:
            cont_or_exit = str(input('type yes to continue or type no to exit: '))
            print(cont_or_exit)
            if cont_or_exit in ['Yes', 'yes', 'YES']:
                x = True
            elif cont_or_exit in ['No', 'no', 'NO']:
                x = False
                exit()
                
# Uses Shodan port info API               
def shodan_port_info():
    x = True
    while x == True:
        try:
            ip_add = input('enter an IP address: ')
            host = requests.get(f"https://internetdb.shodan.io/{ip_add}").json()
            print(host)
        except:
            print('No port information for that IP')            
        finally:
            cont_or_exit = str(input('type yes to continue or type no to exit: '))
            if cont_or_exit in ['Yes', 'yes', 'YES']:
                x = True
            elif cont_or_exit in ['No', 'no', 'NO']:
                x = False
                exit()

  
select = input('Type in 1 for IP address info OR Type in 2 for IP Port Info: ')

if select == '1':
    shodan_ip_info()
if select == '2':
    shodan_port_info()
else:
    print('Did not select an option')
    exit()
      
   
