# tkinter and time modules are inbuilt
from tkinter import *
import time


def run():
    global root
    root = Tk()
    root.title("Stopwatch APP")
    width = 400
    height = 160
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Top = Frame(root)
    Top.pack(side=TOP)
    stopWatch = StopWatch(root)
    stopWatch.pack(side=TOP, pady=15)
    Bottom = Frame(root, width=400)
    Bottom.pack(side=BOTTOM)
    Start = Button(Bottom, text='Start', command=stopWatch.Start,
                   width=20, height=2, bg="green")
    Start.pack(side=LEFT)
    Stop = Button(Bottom, text='Stop', command=stopWatch.Stop,
                  width=20, height=2, bg="red")
    Stop.pack(side=LEFT)
    Reset = Button(Bottom, text='Reset',
                   command=stopWatch.Reset, width=15, height=2)
    Reset.pack(side=LEFT)
    root.config(bg="black")
    root.mainloop()


class StopWatch(Frame):
    def __init__(self, parent=None, **kw):
        '''When object is initialized'''
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0
        self.nextTime = 0.0
        self.onRunning = 0
        self.timestr = StringVar()
        self.MakeWidget()

    def Updater(self):
        '''update the time shown'''
        self.nextTime = time.time() - self.startTime
        self.SetTime(self.nextTime)
        self.timer = self.after(1, self.Updater)

    def MakeWidget(self):
        '''make widget for displaying time'''
        timeText = Label(self, textvariable=self.timestr, font=(
            "callibri", 50), fg="yellow", bg="grey")
        self.SetTime(self.nextTime)
        timeText.pack(fill=X, expand=NO, pady=2, padx=2)

    def SetTime(self, nextElap):
        '''set time that is to be displayed'''
        mins = int(nextElap / 60)
        secs = int(nextElap - mins * 60.0)
        milisecs = int((nextElap - mins * 60.0 - secs) * 100)
        self.timestr.set('%02d:%02d:%02d' % (mins, secs, milisecs))

    def Start(self):
        '''start stopwatch'''
        if not self.onRunning:
            self.startTime = time.time() - self.nextTime
            self.Updater()
            self.onRunning = 1

    def Stop(self):
        '''stop stopwatch'''
        if self.onRunning:
            self.after_cancel(self.timer)
            self.nextTime = time.time() - self.startTime
            self.SetTime(self.nextTime)
            self.onRunning = 0

    def Reset(self):
        '''reset stopwatch'''
        self.startTime = time.time()
        self.nextTime = 0.0
        self.SetTime(self.nextTime)


if __name__ == '__main__':
    run()
