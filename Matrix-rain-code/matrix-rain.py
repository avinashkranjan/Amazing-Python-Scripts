from termcolor import colored
from random import randint
from time import sleep

symbol = [[
    u"\u30A0", u"\u30A1", u"\u30A2", u"\u30A3", u"\u30A4", u"\u30A5",
    u"\u30A6", u"\u30A7", u"\u30A8", u"\u30A9", u"\u30AB", u"\u30AC",
    u"\u30AD", u"\u30AE", u"\u30AF"
],
    [
    u"\u30B0", u"\u30B1", u"\u30B2", u"\u30B3", u"\u30B4", u"\u30B5",
    u"\u30B6", u"\u30B7", u"\u30B8", u"\u30B9", u"\u30BB", u"\u30BC",
    u"\u30BD", u"\u30BE", u"\u30BF"
],
    [
    u"\u30C0", u"\u30C1", u"\u30C2", u"\u30C3", u"\u30C4", u"\u30C5",
    u"\u30C6", u"\u30C7", u"\u30C8", u"\u30C9", u"\u30CB", u"\u30CC",
    u"\u30CD", u"\u30CE", u"\u30CF"
],
    [
    u"\u30D0", u"\u30D1", u"\u30D2", u"\u30D3", u"\u30D4", u"\u30D5",
    u"\u30D6", u"\u30D7", u"\u30D8", u"\u30D9", u"\u30DB", u"\u30DC",
    u"\u30DD", u"\u30DE", u"\u30DF"
],
    [
    u"\u30E0", u"\u30E1", u"\u30E2", u"\u30E3", u"\u30E4", u"\u30E5",
    u"\u30E6", u"\u30E7", u"\u30E8", u"\u30E9", u"\u30EB", u"\u30EC",
    u"\u30ED", u"\u30EE", u"\u30EF"
],
    [
    u"\u30F0", u"\u30F1", u"\u30F2", u"\u30F3", u"\u30F4", u"\u30F5",
    u"\u30F6", u"\u30F7", u"\u30F8", u"\u30F9", u"\u30FB", u"\u30FC",
    u"\u30FD", u"\u30FE", u"\u30FF"
]]

while 1:

    chunk_template = ["" for i in range(139)]
    chunk_length = randint(23, 31)
    positions_to_fill = randint(21, 27)
    symbol_positions = set([randint(0, 138) for j in range(positions_to_fill)])
    symbol_positions = list(symbol_positions)

    for x in range(chunk_length):

        for a in symbol_positions:

            row = randint(0, 5)
            col = randint(0, 14)

            chunk_template[a] = symbol[row][col]

        final_line = " ".join(chunk_template)
        print(colored(final_line, "green"))
        sleep(0.07)
