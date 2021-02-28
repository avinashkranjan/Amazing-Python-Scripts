try:
    import scapy.all as scapy
    import optparse
except ImportError:
    print("[+] packages not installed ")
    print("try-> pip install scapy")
    print("pip install optparse-pretty")


def get_arguments():  # function to pass input in console
    parser = optparse.OptionParser()
    parser.add_option("-t",
                      "--target",
                      dest="target",
                      help="Target IP / IP range.")
    options, arguments = parser.parse_args()
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)  # destinationn ip
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()
    answered_list = scapy.srp(arp_request_broadcast, timeout=1,
                              verbose=False)[0]
    # print(answered_list.summary())
    # print(unanswered.summary())

    clients_list = []
    for element in answered_list:
        clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dict)
        # print(element[1].psrc +"\t\t"+element[1].hwsrc)

    return (clients_list)


def print_result(result_list):
    print(
        "IP\t\t\tMAC ADDRESS\n.........................................................................."
    )
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)
