# ICC rankings scraper

-Using this script you can get the ICC rankings of teams and players of different formats.

## Setup instructions

How to setup and run your script in user's system

"""
Create an instance of `ICC` class.
`python
    scraper = ICC()
    `
| Method | Details |
| ---------------------------- | ------------------------------------------------------------------- |
| `.team_rankings(format)` | Returns the list of rankings of teams of desired format |
|`.player_ranking(type,format)`| Returns the list of player ranking of desired type and format |
"""


## Detailed explanation of script, if needed

"""
        Create an instance of `ICC` class.\n
        Required Params - `format` - "ODI","T20" or "TEST"
        ```python
        icc = ICC()
        icc.team_rankings(format="odi")
        ```
        ```js
        [
            {
                "rank":1,
                "team":"Australia"
            }   
        ]
        ```
        """

"""
        Create an instance of `ICC` class.\n
        Required Params - `format` - "ODI","T20" or "TEST"
        `type` - "batting","bowling" or "all-rounder"
        ```python
        icc = ICC()
        icc.team_player(format="odi",type="batting")
        ```
        ```js
        [
            {
                "rank":1,
                "team":"Babar Azam"
            }   
        ]
        ```
        """

## Author(s)

[Arvind Srivastav](https://github.com/alwenpy)
