**Checksum_Script**



**How to Use:**  
This script can generate checksums from md5, sha1, sha224, sha256, sha384, and sha512. Additionally, for another layer of secret it can create signed checksums using HMAC and a provided secret. Lastly, to provide actual value to the script it can also verify if a checksum matches the file it was generated from.

Examples:

Generate a sha1 checksum

python checksum.py -H sha1 -f test.txt -g
# b29d28bc5239dbc2689215811b2a73588609f301
Generate a signature

python Checksum_Script.py -f test.txt -s secret
# 3YYMCthY4hFxQj1wPF3uAg==
Verify a checksum

python -H sha1 -f test.txt -v b29d28bc5239dbc2689215811b2a73588609f301
Verify a signature

python -f test.txt -s secret -v 3YYMCthY4hFxQj1wPF3uAg==


**conclusion:** 

This script can generate checksums from md5, sha1, sha224, sha256, sha384, and sha512 much more!

#### By [Kalivarapubindusree]() 
