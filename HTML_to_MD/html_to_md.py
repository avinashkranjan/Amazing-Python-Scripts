import html2md

"""
User needs to change the two paths here or else it wont work.
"""
path = "Path/To/Your/HTML"


def html_to_md():
    html = open(path, "r").read()
    md = html2md.convert(html)
    md_path = "Path/Where/You/Want/To/Save_MD.file"
    with open(md_path, "w") as mrd:
        mrd.write(md)
        mrd.close()
    md_save_str = f"You have successfully written the HTML to a MD file and it is saved at {md_path}"
    print(md_save_str)


html_to_md()
