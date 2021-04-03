import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

host = "127.0.0.1"
port = 9090


class Client:

    def __init__(self, HOST, PORT):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))  # Connecting to server

        messagebox = tkinter.Tk()
        messagebox.withdraw()

        self.nickname = simpledialog.askstring(
    "Nickname", "Please choose a nickname", parent=messagebox)

        self.GUI_done = False
        self.running = True

        GUI_thread = threading.Thread(target=self.GUI_loop)
        receive_thread = threading.Thread(target=self.receive)

        GUI_thread.start()
        receive_thread.start()

    def GUI_loop(self):
        '''
        This fuction will create the front end window
        '''
        self.win = tkinter.Tk()
        self.win.configure(bg='lightgrey')

        self.chat_label = tkinter.Label(self.win, text="Chat:", bg="lightblue")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state="disabled")  #Storing this as chat history, hence disabled to text

        self.message_label = tkinter.Label(self.win, text="message", bg="lightblue")
        self.message_label.config(font=("Arial", 12))
        self.message_label.pack(padx=20, pady=5)

        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = tkinter.Button(self.win, text="send", command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)
        
        self.GUI_done = True

        self.win.protocol("WM_delete_window", self.stop)

        self.win.mainloop()



    def write(self):
        message=f"{self.nickname}:{self.input_area.get('1.0', 'end')}"
        self.sock.send(message.encode('utf-8'))
        self.input_area.delete('1.0', 'end')


    def stop(self):
        self.running=False
        self.win.destroy()
        self.sock.close()
        exit(0)


    def receive(self):
        while self.running:
            try:
                message=self.sock.recv(1024).decode('utf-8')
                if message == "NICK":
                    self.sock.send(self.nickname.encode('utf-8'))
                else:
                    if self.GUI_done:
                        self.text_area.config(state='normal')
                        self.text_area.insert('end', message)
                        self.text_area.yview('end')
                        self.text_area.config(state="disabled")

            except ConnectionAbortedError():
                break
            except:
                print("Some Error occured")
                self.sock.close()
                break


client=Client(host, port)
