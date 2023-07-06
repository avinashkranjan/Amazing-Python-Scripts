# What Is Bitcoin Mining?
Bitcoin mining is performed by high-powered computers that solve complex computational math problems , these problems are so complex that they cannot be solved by hand and are complicated enough to tax even incredibly powerful computers.




# Terminology :

1. Transaction : An transaction is a transfer of Bitcoin value and are collected in Blocks 

2. SHA256: a function which can generate an almost-unique 256-bit (32-byte) signature(Hexa-Decimal) for a text.

3. Block: Blocks are files where data pertaining to the Bitcoin network are permanently recorded

4. Nonce : Miners have to guess this number which will reward them Btc , A nonce is an abbreviation for "number only used once," which is a number added to a hashed—or encrypted—block in a blockchain that, when rehashed, meets the difficulty level restrictions. 

5. Difficulty Level : Number of prefix Contagiuos Zeroes 




# Theory :

Btc will be rewarded if Nonce gives us string with prefix of Zeroes the difficult number of times. sounds confusing?

So,Let's take example :

1. Let's assume we have difficulty level = 20 
2. Now, Let's again assume that we have previous hash as : 'a5x208fecf9a66be9a2bc7...'
3. Now we create text as  : text = str(block_number) + transactions + previous_hash + str(nonce)
4. Now we pass text to SHA256 Function to generate hash
5. Finally, that hash prefix must be equal to number of zeroes as difficulty level.
6. And Boom!! You have mined succesfully.



# Draw Backs:
The script has no drawbacks but due to increase in miners , the difficultly level increases and hence we'd require best hardware as fastest wins. 

# Refrences:

https://www.investopedia.com/terms/b/bitcoin.asp

https://www.youtube.com/watch?v=wTC31ZI6QM4

https://www.youtube.com/watch?v=ZhnJ1bkIWWk&t=143s


 



