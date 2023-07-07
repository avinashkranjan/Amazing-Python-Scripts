import tkinter
import tkinter.ttk

tkinter_umlauts = ['odiaeresis', 'adiaeresis', 'udiaeresis',
                   'Odiaeresis', 'Adiaeresis', 'Udiaeresis', 'ssharp']


class myentry(tkinter.Entry):
    def set_completion_list(self, completion_list):
        self._completion_list = sorted(completion_list, key=str.lower)
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)

    def autocomplete(self, delta=0):
        if delta:
            self.delete(self.position, tkinter.END)
        else:
            self.position = len(self.get())
        _hits = []
        for element in self._completion_list:
            if element.lower().startswith(self.get().lower()):
                _hits.append(element)
        if _hits != self._hits:
            self._hit_index = 0
            self._hits = _hits
        if _hits == self._hits and self._hits:
            self._hit_index = (self._hit_index + delta) % len(self._hits)
        if self._hits:
            self.delete(0, tkinter.END)
            self.insert(0, self._hits[self._hit_index])
            self.select_range(self.position, tkinter.END)

    def handle_keyrelease(self, event):
        if event.keysym == "BackSpace":
            self.delete(self.index(tkinter.INSERT), tkinter.END)
            self.position = self.index(tkinter.END)
        if event.keysym == "Left":
            if self.position < self.index(tkinter.END):
                self.delete(self.position, tkinter.END)
            else:
                self.position = self.position-1
                self.delete(self.position, tkinter.END)
        if event.keysym == "Right":
            self.position = self.index(tkinter.END)
        if event.keysym == "Down":
            self.autocomplete(1)
        if event.keysym == "Up":
            self.autocomplete(-1)
        if len(event.keysym) == 1 or event.keysym in tkinter_umlauts:
            self.autocomplete()


class mycombobox(tkinter.ttk.Combobox):

    def set_completion_list(self, completion_list):
        self._completion_list = sorted(completion_list, key=str.lower)
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)
        self['values'] = self._completion_list

    def autocomplete(self, delta=0):
        if delta:
            self.delete(self.position, tkinter.END)
        else:
            self.position = len(self.get())
        _hits = []
        for element in self._completion_list:
            if element.lower().startswith(self.get().lower()):  # Match case insensitively
                _hits.append(element)
        if _hits != self._hits:
            self._hit_index = 0
            self._hits = _hits
        if _hits == self._hits and self._hits:
            self._hit_index = (self._hit_index + delta) % len(self._hits)
        if self._hits:
            self.delete(0, tkinter.END)
            self.insert(0, self._hits[self._hit_index])
            self.select_range(self.position, tkinter.END)

    def handle_keyrelease(self, event):
        if event.keysym == "BackSpace":
            self.delete(self.index(tkinter.INSERT), tkinter.END)
            self.position = self.index(tkinter.END)
        if event.keysym == "Left":
            if self.position < self.index(tkinter.END):
                self.delete(self.position, tkinter.END)
            else:
                self.position = self.position-1
                self.delete(self.position, tkinter.END)
        if event.keysym == "Right":
            self.position = self.index(tkinter.END)
        if len(event.keysym) == 1:
            self.autocomplete()
# TEST THIS


def test(test_list):
    root = tkinter.Tk(className=' AutocompleteEntry demo')
    entry = myentry(root)
    entry.set_completion_list(test_list)
    entry.pack()
    entry.focus_set()
    combo = mycombobox(root)
    combo.set_completion_list(test_list)
    combo.pack()
    combo.focus_set()
    root.bind('<Control-Q>', lambda event=None: root.destroy())
    root.bind('<Control-q>', lambda event=None: root.destroy())
    root.mainloop()
