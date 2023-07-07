# check_external_ip.py

# script to check your external IP address
import re
import requests

ur_url = "http://checkip.dyndns.org"
request = requests.get(ur_url)
_result = request.text.split(': ', 1)[1]
your_ip = _result.split('</body></html>', 1)[0]

print(your_ip)
