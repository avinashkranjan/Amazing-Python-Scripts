import html2md
"""
User needs to change the two paths here or else it wont work.
"""
path = "Path/To/Your/HTML"


def html_to_md():
    # opens your html file
    html = open(path, "r").read()
    # converts the html file to a md file
    md = html2md.convert(html)
    # Path where your md file is saved
    md_path = "Path/Where/You/Want/To/Save_MD.file"
    # Opens the path location and writes from html to md
    with open(md_path, "w") as mrd:
        mrd.write(md)
        mrd.close()
    # Simply tells you it is done.
    md_save_str = f"You have successfully written the HTML to a MD file and it is saved at {md_path}"
    print(md_save_str)


html_to_md()
