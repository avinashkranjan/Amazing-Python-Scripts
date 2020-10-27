# Github Size-Contributor-List

## What this script accomplishes

- Makes an API call to the, "Github API" in order to retrieve the information needed. It retrieves the size of the repository and the number of contributors the repo has
- Information is saved to a text file called, "output.txt"

## How ro run script

### 1. Download script and install requests
```
pip install requests
```

### 2. Run script.py and specify the name of the github user and name of the repository as follows
```
python script.py -o NAMEOFGITHUBUSER -n NAMEOFGITHUBREPO
```

Note that the repo must be owned by the user, otherwise, it will fail.


### 3. Output of the script will be written to a text file called, "output.txt". If the script has incorrect values, it won't run. If the script could not gather data, nothing will be written.


## Example Output
![OutputText](https://i.imgur.com/Ckttce3.png)
    