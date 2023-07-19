import argparse
import json

import warnings
# Quieten python-levenshtein warning
warnings.filterwarnings("ignore") 

from fuzzywuzzy import process
from lyricsscraper import LyricsDotComScraper as Scraper

DESC = """Get song lyrics or find a song from a snippet of it's lyrics, and \
          more."""

EXACT_TITLE_HELP = "Only return results that have an exact match in the titles"

EXACT_MATCH_HELP = "Only return results with an exact match within them."

GENDER_HELP = "Genders to match: m for male, f for female, g for groups. \
               Or a comma seperated list of values."

ARTIST_HELP = """Return artists that match can be combined with -l and -m."""

ALBUMS_HELP = "Return albums that match can be combined with -a and -l"

LYRICS_HELP = "Return lyrics that match can be combined with -a and -m"

GENRE_HELP = """Return matches in the genre(s). Genre can be a music genre or \
                a comma seperated list of genres.
                The genre(s) is matched against the programs list and the best\
                matches are choosen
           """

YEAR_HELP = """Only return results from the year(s) specified in the value, \
               The value can be a single year or a comma seperated list of \
               years.
               Note: Years can only be between 1900 and this year.
            """

DECADE_HELP = """Only return results in the specified decade(s) where each \
                 decade is represented by the first year in the decade (e.g \
                 1930 for the 30's).Value can be a value or a comma seperated \
                 list of values between the decades 1930 and 2020
        """

COUNT_HELP = "Return count number of matches. Defaults to 1"

STYLE_HELP = """Specify the style(s). Styles can be gotten from lyrics.com"""

LISTENER_HELP = ""

PAGE_HELP = """
            This program was originally build to scrape the first page \
            of each result but this argument allows you to scrape multiple\
            explicitly specified pages.
            The value can be a page number, a comma seperated list of page \
            numbers or a range of page number in the format a-z where a is \
            the start page and z is the end page.
        """

DOWNLOAD_LYRICS_HELP = """
                        Download the full lyrics of all songs matched into \
                        individual txt files.
                    """

OUT_HELP = """
              Output the search results to json file specified in the argument.
           """


def main():
    parser = argparse.ArgumentParser(description=DESC)

    parser.add_argument("st", help="The lyric snippet.")

    match_type_group = parser.add_mutually_exclusive_group()
    match_type_group.add_argument(
        "-e",
        "--exact-match",
        help=EXACT_MATCH_HELP,
        action="store_true",
        dest="exacttitle",
    )
    match_type_group.add_argument(
        "-t",
        "--exact-title",
        help=EXACT_TITLE_HELP,
        action="store_true",
        dest="exactmatch",
    )
    parser.add_argument("-n", "--gender", help=GENDER_HELP,
                        action="store")
    parser.add_argument("-a", "--artists", help=ARTIST_HELP,
                        action="store_true")
    parser.add_argument("-m", "--albums", help=ALBUMS_HELP,
                        action="store_true")
    parser.add_argument("-l", "--lyrics", help=LYRICS_HELP,
                        action="store_true")
    parser.add_argument("-g", "--genre", help=GENRE_HELP,
                        action="store")
    parser.add_argument("-o", "--output", help=OUT_HELP,
                        action="store")
    parser.add_argument("-d", "--decade", help=DECADE_HELP,
                        action="store")
    parser.add_argument(
                        "-c", "--count", help=COUNT_HELP, action="store",
                        type=int, default=1)
    parser.add_argument("-y", "--year", help=YEAR_HELP, action="store")
    parser.add_argument("-s", "--style", help=STYLE_HELP, action="store")
    parser.add_argument(
        "-b",
        "--download-full-lyrics",
        help=DOWNLOAD_LYRICS_HELP,
        action="store_true",
        dest="download_full_lyrics",
    )
    parser.add_argument(
        "--listener", help=LISTENER_HELP, action="store_true", dest="listen"
    )
    parser.add_argument(
        "--full-lyrics",
        action="store_true",
        dest="full_lyrics",
        help="Print full lyrics from match.",
    )
    parser.add_argument("-p", "--page", action="store", help=PAGE_HELP)
    args = parser.parse_args()
    app_arg = {"count": args.count}
    app = Scraper(**app_arg)
    # Build request parameters
    requests_params = {
        "st": [],
        "stype": [],
        "qtype": [],
        "gender": [],
        "genre": [],
        "decade": [],
        "year": [],
        "style": [],
        "p": [],
    }
    if args.exacttitle:
        requests_params["stype"] = "1"
    elif args.exactmatch:
        requests_params["stype"] = "2"

    if args.artists:
        requests_params["qtype"].append(2)
    if args.albums:
        requests_params["qtype"].append(3)
    if args.lyrics:
        requests_params["qtype"].append(1)

    if not args.artists and not args.albums and not args.lyrics:
        requests_params["qtype"].append(1)

    def parse_multiple_valued_args(arg_list):
        """
            Parse arguments with multiple values.
        """
        for arg in arg_list:
            val = getattr(args, arg)
            if val:
                vals = val.split(",")
                for i in vals:
                    if arg == "genre":
                        requests_params[arg].append(match_arg(
                            i.strip(), "genre"))
                    elif arg == "style":
                        requests_params[arg].append(match_arg(
                            i.strip(), "style"))
                    else:
                        requests_params[arg].append(i.strip())

    def parse_page_arg():
        """
            Parse multiple pages
        """
        page_val = args.page
        if not page_val:
            return
        if "," in page_val:
            parse_multiple_valued_args(["p"])
        elif "-" in page_val:
            start, end = page_val.split("-")
            for i in range(int(start), int(end) + 1):
                requests_params["p"].append(i)
        else:
            requests_params["p"].append(page_val)

    parse_multiple_valued_args(
        ["gender", "decade", "genre", "decade", "year", "style", "st"]
    )
    parse_page_arg()
    parsed_request_params = app.parse_params(**requests_params)
    app.search(parsed_request_params)
    if args.output:
        o = args.output
        if not o.endswith(".json"):
            o += ".json"
        json.dump(app.lyrics, open(o, "w"))
        print("Written to " + o)

    else:
        print("\n\n", app.lyrics)
    if args.full_lyrics:
        for i in app.lyrics:
            print(app.extract_full_lyrics(i["full_lyrics_url"], i["title"]))
    if args.download_full_lyrics:
        for i in app.lyrics:
            print(
                "Downloaded "
                + app.extract_full_lyrics(
                    i["full_lyrics_url"], i["title"], download=True
                )
            )


def match_arg(arg, type_):
    # Available genres
    genres = [
        "Blues",
        "Brass+_+Military",
        r"Children%27s",
        "Classical",
        "Electronic",
        "Folk%2C+World%2C+__+Country",
        "Funk+--+Soul",
        "Hip+Hop",
        "Jazz",
        "Latin",
        "Non-Music",
        "Pop",
        "Reggae",
        "Rock",
        "Spiritual",
        "Stage+__+Screen",
    ]

    # Available styles
    style = [
        "Aboriginal",
        "Abstract",
        "Acid",
        "Acid+House",
        "Acid+Jazz",
        "Acid+Rock",
        "Acoustic",
        "African",
        "Afro-Cuban",
        "Afro-Cuban+Jazz",
        "Afrobeat",
        "Alternative+Rock",
        "Ambient",
        "Andalusian+Classical",
        "AOR",
        "Appalachian+Music",
        "Arena+Rock",
        "Art+Rock",
        "Audiobook",
        "Avant-garde+Jazz",
        "Avantgarde",
        "Bachata",
        "Ballad",
        "Baltimore+Club",
        "Baroque",
        "Bass+Music",
        "Bassline",
        "Batucada",
        "Bayou+Funk",
        "Beat",
        "Beatbox",
        "Beguine",
        "Berlin-School",
        "Bhangra",
        "Big+Band",
        "Big+Beat",
        "Black+Metal",
        "Bluegrass",
        "Blues+Rock",
        "Bolero",
        "Bollywood",
        "Bongo+Flava",
        "Boogaloo",
        "Boogie",
        "Boogie+Woogie",
        "Boom+Bap",
        "Bop",
        "Bossa+Nova",
        "Bossanova",
        "Bounce",
        "Brass+Band",
        "Breakbeat",
        "Breakcore",
        "Breaks",
        "Brit+Pop",
        "Britcore",
        "Broken+Beat",
        "Bubblegum",
        "Cajun",
        "Calypso",
        "Candombe",
        "Canzone+Napoletana",
        "Cape+Jazz",
        "Celtic",
        "Cha-Cha",
        "Chacarera",
        "Chamam%C3%A9",
        "Champeta",
        "Chanson",
        "Charanga",
        "Chicago+Blues",
        "Chillwave",
        "Chiptune",
        "Choral",
        "Classic+Rock",
        "Classical",
        "Coldwave",
        "Comedy",
        "Compas",
        "Conjunto",
        "Conscious",
        "Contemporary",
        "Contemporary+Jazz",
        "Contemporary+R__B",
        "Cool+Jazz",
        "Copla",
        "Corrido",
        "Country",
        "Country+Blues",
        "Country+Rock",
        "Crunk",
        "Crust",
        "Cuatro",
        "Cubano",
        "Cumbia",
        "Cut-up--DJ",
        "Dance-pop",
        "Dancehall",
        "Danzon",
        "Dark+Ambient",
        "Darkwave",
        "Death+Metal",
        "Deathcore",
        "Deathrock",
        "Deep+House",
        "Deep+Techno",
        "Delta+Blues",
        "Descarga",
        "Dialogue",
        "Disco",
        "Dixieland",
        "DJ+Battle+Tool",
        "Donk",
        "Doo+Wop",
        "Doom+Metal",
        "Downtempo",
        "Dream+Pop",
        "Drone",
        "Drum+n+Bass",
        "Dub",
        "Dub+Poetry",
        "Dub+Techno",
        "Dubstep",
        "Early",
        "East+Coast+Blues",
        "Easy+Listening",
        "EBM",
        "Education",
        "Educational",
        "Electric+Blues",
        "Electro",
        "Electro+House",
        "Electroclash",
        "Emo",
        "Ethereal",
        "Euro+House",
        "Euro-Disco",
        "Eurobeat",
        "Eurodance",
        "Europop",
        "Experimental",
        "Fado",
        "Field+Recording",
        "Flamenco",
        "Folk",
        "Folk+Metal",
        "Folk+Rock",
        "Forr%C3%B3",
        "Free+Funk",
        "Free+Improvisation",
        "Free+Jazz",
        "Freestyle",
        "Funeral+Doom+Metal",
        "Funk",
        "Funk+Metal",
        "Fusion",
        "Future+Jazz",
        "G-Funk",
        "Gabber",
        "Gangsta",
        "Garage+House",
        "Garage+Rock",
        "Ghetto",
        "Ghetto+House",
        "Ghettotech",
        "Glam",
        "Glitch",
        "Go-Go",
        "Goa+Trance",
        "Gogo",
        "Goregrind",
        "Gospel",
        "Goth+Rock",
        "Gothic+Metal",
        "Grime",
        "Grindcore",
        "Grunge",
        "Guaguanc%C3%B3",
        "Guajira",
        "Guaracha",
        "Gypsy+Jazz",
        "Hands+Up",
        "Happy+Hardcore",
        "Hard+Beat",
        "Hard+Bop",
        "Hard+House",
        "Hard+Rock",
        "Hard+Techno",
        "Hard+Trance",
        "Hardcore",
        "Hardcore+Hip-Hop",
        "Hardstyle",
        "Harmonica+Blues",
        "Harsh+Noise+Wall",
        "Heavy+Metal",
        "Hi+NRG",
        "Highlife",
        "Hillbilly",
        "Hindustani",
        "Hip+Hop",
        "Hip-House",
        "Hiplife",
        "Honky+Tonk",
        "Horrorcore",
        "House",
        "Hyphy",
        "IDM",
        "Illbient",
        "Impressionist",
        "Indian+Classical",
        "Indie+Pop",
        "Indie+Rock",
        "Industrial",
        "Instrumental",
        "Interview",
        "Italo+House",
        "Italo-Disco",
        "Italodance",
        "J-pop",
        "Jazz-Funk",
        "Jazz-Rock",
        "Jazzdance",
        "Jazzy+Hip-Hop",
        "Jump+Blues",
        "Jumpstyle",
        "Jungle",
        "Junkanoo",
        "K-pop",
        "Karaoke",
        "Klezmer",
        "Krautrock",
        "Kwaito",
        "Lambada",
        "Latin",
        "Latin+Jazz",
        "Leftfield",
        "Light+Music",
        "Lo-Fi",
        "Louisiana+Blues",
        "Lounge",
        "Lovers+Rock",
        "Makina",
        "Maloya",
        "Mambo",
        "Marches",
        "Mariachi",
        "Marimba",
        "Math+Rock",
        "Medieval",
        "Melodic+Death+Metal",
        "Melodic+Hardcore",
        "Memphis+Blues",
        "Merengue",
        "Metalcore",
        "Miami+Bass",
        "Military",
        "Minimal",
        "Minimal+Techno",
        "Minneapolis+Sound",
        "Mizrahi",
        "Mod",
        "Modal",
        "Modern",
        "Modern+Classical",
        "Modern+Electric+Blues",
        "Monolog",
        "Mouth+Music",
        "Movie+Effects",
        "MPB",
        "Music+Hall",
        "Musical",
        "Musique+Concr%C3%A8te",
        "Neo+Soul",
        "Neo-Classical",
        "Neo-Romantic",
        "Neofolk",
        "New+Age",
        "New+Beat",
        "New+Jack+Swing",
        "New+Wave",
        "No+Wave",
        "Noise",
        "Nordic",
        "Norte%C3%B1o",
        "Novelty",
        "Nu+Metal",
        "Nu-Disco",
        "Nueva+Cancion",
        "Nueva+Trova",
        "Nursery+Rhymes",
        "Oi",
        "Opera",
        "Operetta",
        "Ottoman+Classical",
        "P.Funk",
        "Pachanga",
        "Pacific",
        "Parody",
        "Persian+Classical",
        "Piano+Blues",
        "Piedmont+Blues",
        "Pipe+__+Drum",
        "Plena",
        "Poetry",
        "Political",
        "Polka",
        "Pop+Punk",
        "Pop+Rap",
        "Pop+Rock",
        "Porro",
        "Post+Bop",
        "Post+Rock",
        "Post-Hardcore",
        "Post-Modern",
        "Post-Punk",
        "Power+Electronics",
        "Power+Metal",
        "Power+Pop",
        "Prog+Rock",
        "Progressive+Breaks",
        "Progressive+House",
        "Progressive+Metal",
        "Progressive+Trance",
        "Promotional",
        "Psy-Trance",
        "Psychedelic",
        "Psychedelic+Rock",
        "Psychobilly",
        "Pub+Rock",
        "Public+Broadcast",
        "Public+Service+Announcement",
        "Punk",
        "Quechua",
        "Radioplay",
        "Ragga",
        "Ragga+HipHop",
        "Ragtime",
        "Ra%C3%AF",
        "Ranchera",
        "Reggae",
        "Reggae+Gospel",
        "Reggae-Pop",
        "Reggaeton",
        "Religious",
        "Renaissance",
        "Rhythm+__+Blues",
        "Rhythmic+Noise",
        "RnB--Swing",
        "Rock+__+Roll",
        "Rock+Opera",
        "Rockabilly",
        "Rocksteady",
        "Romani",
        "Romantic",
        "Roots+Reggae",
        "Rumba",
        "Rune+Singing",
        "Salsa",
        "Samba",
        "Schlager",
        "Score",
        "Screw",
        "Sea+Shanties",
        "Shoegaze",
        "Ska",
        "Skiffle",
        "Sludge+Metal",
        "Smooth+Jazz",
        "Soca",
        "Soft+Rock",
        "Son",
        "Son+Montuno",
        "Sonero",
        "Soukous",
        "Soul",
        "Soul-Jazz",
        "Sound+Art",
        "Soundtrack",
        "Southern+Rock",
        "Space+Rock",
        "Space-Age",
        "Speech",
        "Speed+Garage",
        "Speed+Metal",
        "Speedcore",
        "Spoken+Word",
        "Steel+Band",
        "Stoner+Rock",
        "Story",
        "Surf",
        "Swamp+Pop",
        "Swing",
        "Swingbeat",
        "Symphonic+Rock",
        "Synth-pop",
        "Synthwave",
        "Tango",
        "Tech+House",
        "Tech+Trance",
        "Technical",
        "Techno",
        "Tejano",
        "Texas+Blues",
        "Theme",
        "Thrash",
        "Thug+Rap",
        "Trance",
        "Trap",
        "Tribal",
        "Tribal+House",
        "Trip+Hop",
        "Tropical+House",
        "Trova",
        "Turntablism",
        "UK+Garage",
        "Vallenato",
        "Vaporwave",
        "Viking+Metal",
        "Vocal",
        "Volksmusik",
        "Western+Swing",
        "Witch+House",
        "Zouk",
        "Zydeco",
    ]
    match = (
        process.extractOne(arg, genres)
        if type_ == "genre"
        else process.extractOne(arg, style)
    )
    print(f"Found {type_} match {match[0]} with {match[1]}% match.")
    return match[0]


if __name__ == "__main__":
    main()