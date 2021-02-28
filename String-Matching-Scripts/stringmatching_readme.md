# String matching

Using `Fuzzywuzzy`

# Short description of package/script

Fuzzy string matching is the process of finding strings that match a given pattern. Basically it uses Levenshtein Distance to calculate the differences between sequences.

## Setup instructions

- install python-Levenshtein and fuzzywuzzy
```bash
pip install fuzzywuzzy[speedup]
```

## Detailed explanation of script, if needed

Of course, a big problem with most corners of the internet is labeling. One of our most consistently frustrating issues is trying to figure out whether two ticket listings are for the same real-life event (that is, without enlisting the help of our army of interns).To pick an example completely at random,
Bollywood has a show running in India called “Zarkana”. When we scour the web to find tickets for sale, mostly those tickets are identified by a title, date, time, and venue. 
For example, we search for a given show or movie on internet, and we get a number of results with different names but represeting the same show.our human brain can easily comprehend that 
all are same, but we do want to do this programmatically and hence came the concept of fuzzywuzzy library in python which calculates the similarity of two or more sentences .
If we have far too many events (over 60,000) to be able to just throw us at the problem. So we want to do this programmatically, but we also want our programmatic results to pass the "human brain” test, and make sense to normal users.
So basically we want to have an efficient way of string matching script.

## Output

output in this file:

[![Capture.png](https://i.postimg.cc/Yqdxbzy2/Capture.png)](https://postimg.cc/KRgLYB2C)

## Author(s)

Vaishnavi Jha
