import tkinter as tk
from urllib.request import urlopen
from http import HTTPStatus
from fake_useragent import UserAgent

def get_status(status_code: int) -> str:
    for value in HTTPStatus:
        if value.value == status_code:
            description = f'({value.value} {value.name}) {value.description}'
            return description
    return "Unknown Status Code..."

def check_website():
    website_url = website_entry.get()
    result_text.delete("1.0", tk.END)

    try:
        response = urlopen(website_url)
        status_code = response.getcode()
        status_description = get_status(status_code)
        result = f"Status for {website_url}:\n{status_description}\n"
    except Exception as e:
        result = f"Error checking {website_url}:\n{str(e)}\n"

    result_text.insert(tk.END, result)

root = tk.Tk()
root.title("Website Checker")
root.configure(bg="#1e1e1e")  

website_label = tk.Label(root, text="Enter Website URL:", bg="#1e1e1e", fg="white")
website_label.pack(pady=5)

website_entry = tk.Entry(root, width=50)
website_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Website", command=check_website, bg="#303030", fg="white")
check_button.pack(pady=5)

result_text = tk.Text(root, wrap=tk.WORD, bg="#1e1e1e", fg="white")
result_text.pack(fill=tk.BOTH, expand=True)

root.mainloop()
