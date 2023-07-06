from bs4 import BeautifulSoup as soup  # HTML data structure
import requests  # Web client
import webbrowser
import string
import random
import sys


def generateNames():

    # a list with random names to use for username
    # we choose a random name from the list

    names = "Mario Speedwagon, Petey Cruiser, Anna Sthesia,  Molive, Anna Mull, Gail Forcewind, Paige Turner, Bob Frapples, Walter Melon, Nick R. Bocker, Barb Ackue, Buck Kinnear, Greta Life, Ira Membrit, Shonda Leer, Brock Lee, Maya Didas, Rick O'Shea, Monty Carlo, Sal Monella, Sue Vaneer, Cliff Hanger, Barb Dwyer, Terry Aki, Cory Ander, Robin Banks, Jimmy Changa, Barry Wine, Wilma Mumduya, Buster Hyman, Poppa Cherry, Zack Lee, Don Stairs, Saul T. Balls, Peter Pants, Hal Appeno, Otto Matic, Moe Fugga, Graham Cracker, Tom Foolery, Al Dente, Bud Wiser, Polly Tech, Holly Graham, Frank N. Stein, Cam L. Toe, Pat Agonia, Tara Zona, Barry Cade, Phil Anthropist, Marvin Gardens, Phil Harmonic, Arty Ficial, Will Power, Donatella Nobatti, Juan Annatoo, Stew Gots, Anna Rexia, Bill Emia, Curt N. Call, Max Emum, Minnie Mum, Bill Yerds, Hap E. Birthday, Matt Innae, Polly Science, Tara Misu, Ed U. Cation, Gerry Atric, Kerry Oaky, Midge Itz, Gabe Lackmen, Mary Christmas, Dan Druff, Jim Nasium, Angie O. Plasty, Ella Vator, Sal Vidge, Bart Ender, Artie Choke, Hans Olo, Marge Arin, Hugh Briss, Gene Poole, Ty Tanic, Manuel Labor, Lynn Guini, Claire Voyant, Peg Leg, Jack E. Sack, Marty Graw, Ash Wednesday, Olive Yu, Gene Jacket, Tom Atoe, Doug Out, Sharon Needles, Beau Tie, Serj Protector, Marcus Down, Warren Peace, Bud Jet, Barney Cull, Marion Gaze, Eric Shun, Mal Practice, Ed Itorial, Rick Shaw, Paul Issy, Ben Effit, Kat E. Gory, Justin Case, Louie Z. Ana, Aaron Ottix, Ty Ballgame, Anne Fibbiyon, Barry Cuda, John Withawind, Joe Thyme, Mary Goround ,Marge Arita, Frank Senbeans, Bill Dabear, Ray Zindaroof, Adam Zapple, Lewis N. Clark, Matt Schtick, Sue Shee, Chris P. Bacon, Doug Lee Duckling, Mason Protesters, Sil Antro, Cal Orie, Sara Bellum, Al Acart, Marv Ellis, Evan Shlee, Terry Bull, Mort Ission, Mark Ette, Ken Tucky, Louis Ville, Colin Oscopy, Fred Attchini, Al Fredo, Penny Tration, Reed Iculous, Chip Zinsalsa, Matt Uhrafact, Jack Dup, Mike Roscope, Lou Sinclark, Faye Daway, Javy Cad,, Tom Ollie, Sam Buca, Phil Anderer, Sam Owen, Mary Achi, Ray Cyst, Curtis E. Flush, Holland Oats, Helen Highwater, Eddy Kitt, Al Toesacks, Sir Kim Scision, Elle Bowdrop, Yu Tube, Ellis Dee, Anna Lytics, Sara Bellum, Penny Trate, Phil Erup, Jenna Side, Mary Nara, Mick Donalds, Amber Alert, Vic Tory, Bobby Pin, Dom Inate, Hugh Miliation, Christian Mingle, Juan Soponatime, Dante Sinferno, Ed Zupp, Sarah Yevo, Jess Thetip, Arthur Itis, Faye Sbook, Carrie R. Pigeon, Rachel Slurs, Ty Pryder, Cole Slaw, Pat Ernity, Deb Utant, Luke Warm, Travis Tee, Clara Fication, Paul Itician, Deb Utant, Moe Thegrass, Carol Sell, Scott Schtape, Cody Pendant, Frank Furter, Barry Dalive, Mort Adella, Ray Diation, Mack Adamia, Farrah Moan, Theo Retical, Eda Torial, Mae Nayse, Bella Ruse, Yuri thra, Tucker Doubt, Cara Larm, Abel Body, Sal Ami, Colin Derr, Cathy Derr, Colin Scopy, Mel Anoma, Adam Up, Lou Zing, Mark Key, Sven Gineer, Mick Rib, Benny Ficial, Genie Inabottle, Gene Therapy, Reggie Stration, Lou Ow, Lance Dorporal, Lou Tenant, Nick Knack, Patty Whack, Reuben Sandwich, Hugo Slavia, Aaron Spacemuseum, Petey Atricks, Dan Delion, Terry Torial, Cal Q. Later, Jen Trification, Indy Nile, Ray Volver, Minnie Strone, Gustav Wind, Paul Samic, Vinny Gret, , oyce Tick, Cliff Diver, Earl E. Riser, Cooke Edoh, Jen Youfelct, Reanne Carnation, Paul Misunday, Chris P. Cream, Gio Metric, Caire Innet, Marsha Mello, Manny Petty, Val Adictorian, Lucy Tania, Jaques Amole"
    names = names.split(", ")
    return random.choices(names)[0]


def generatePassword(length):

    # declaring [letter (upper and lower case), numbers, and special characters]
    letters = string.ascii_letters
    numbers = string.digits
    punctuations = "!#$%&()*+-/<=>?@[]^_{|}~"

    # we convert all the characters from above into a list
    # we then shuffle this list to create a random sequence
    # and choose a sequence of given length

    printable = f'{letters}{numbers}{punctuations}'
    printable = list(printable)
    random.shuffle(printable)
    temp_password = ''.join(random.choices(printable, k=length))
    return temp_password


def generateEmailIdAndLink():

    # providing header for beautiful soup
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
    }

    # using request.get on https://10minutemail.net/ site, and pass header as extra data
    response = requests.get('https://10minutemail.net/', headers=headers)
    # the response has session Id required to retrieve email and link
    ses = str(response.cookies).split(",")[2].split(" ")[2]

    # we then pass this session id to get JSON data for the email
    response = requests.get('https://10minutemail.net/address.api.php?' + ses)
    page_soup = soup(response.content, "html.parser")  # saving the json

    # selecting the needed data from the json, cleaning the data
    cookies = str(page_soup).split('"')
    # url for the given email
    permalink = cookies[cookies.index("url") + 2]
    # to access the mail page an extra key data is required [mentioned in json object]
    permalink = permalink.replace(
        '\/', "/") + "?key=" + cookies[cookies.index("key") + 2]

    temp_email_id = cookies[cookies.index("mail_get_mail") + 2]
    return temp_email_id, permalink


def getResult(name, password, email, link):

    # Different ways to get the data from the script (different UI methods)

    # opens a new tab in chrome with the temporary data
    getResultInChromeTab(name, password, email, link)
    # getResultInNotepad(name, password, email, link)       # open a new notepad with the temporary data
    # getResultInClipboard(name, password, email, link)     # stores data in clipboard (multiple clipboard items) [--coming soon--]

    # add a if else case if you want to choose options during run time


def getResultInChromeTab(name, password, email, link):

    # creates a file with html extension
    # writes out the data in the file (using basic html format [paras and href]) [-- can be beautified --]
    # saves the data and opens the file (open in localhost)

    out_filename = "tempRegistration.html"
    f = open(out_filename, "w")

    f.write('<p> Username: ' + name + "</p>")
    f.write('<p> Password: ' + password + "</p>")
    f.write('<p> Email Id: ' + email + "</p>")
    f.write(f'<a href = {link}> Link: ' + link + "</a>")
    f.close()
    webbrowser.open("tempRegistration.html")


def getResultInNotepad(name, password, email, link):

    # creates a file with txt extension
    # writes all the data in the file saves it closes it and then opens it as a popup

    out_filename = "tempRegistration.txt"
    f = open(out_filename, "w")

    f.write('Name: ' + name + '\n')
    f.write("Password: " + password + '\n')
    f.write("Email Id: " + email + '\n' + '\n')
    f.write("Link: " + link)

    f.close()
    webbrowser.open("tempRegistration.txt")


if __name__ == "__main__":

    # function call to generate a password
    # inputs given to the functions is length of the password
    random_password = generatePassword(16)

    # function call for creating a list with random names and returning a temporary username
    random_name = generateNames()

    # function call to get temporary email with its link to get confirmation mails etc
    temporary_emailID, temp_link = generateEmailIdAndLink()

    # multiple ways to get output in UI
    getResult(random_name, random_password, temporary_emailID, temp_link)

    # get result as a new text file
    # get result as a new chrome tab
    # get result in clipboard win + V change settings if not enables
