from tkinter import *
from tkinter import ttk
from random import *
import time


win = Tk()
win.geometry("1340x600+10+10")
win.title("Sorting Algorithm Visualizer")
win.config(bg="black")
win.resizable(0, 0)

data = []

f1 = Frame(win, width=1300, height=100, bg="#e6a64e")
f1.grid(row=0, column=0, padx=15, pady=10)
can = Canvas(win, width=1330, height=470, bg="grey")
can.grid(row=1, column=0)


def main(data, carr):
    can.delete("all")
    cheight = 470
    cwidth = 1330
    bwidth = cwidth/(len(data)+1)
    offset = 5
    spacing = 0
    normdata = [i/max(data) for i in data]
    for i, height in enumerate(normdata):
        x1 = i*bwidth+offset+spacing
        y1 = cheight-height*370
        x2 = (i+1)*bwidth+offset
        y2 = cheight
        can.create_rectangle(x1, y1, x2, y2, fill=carr[i])
        # can.create_text(x1+0.2,y1,anchor=SW,text=str(data[i]))
    win.update_idletasks()


def Generate():
    global data
    data = []
    size = int(e1.get())
    min = int(e2.get())
    max = int(e3.get())
    for i in range(size):
        data.append(randrange(min, max+1))
    # data = [22, 11, 34, 23, 44, 33, 9, 30, 31, 30, 42, 39, 40, 23, 34, 32, 31, 46, 15, 43, 9, 1, 23, 22, 41, 32, 31, 39, 38, 16, 24, 24, 31, 12, 42, 16, 23, 28, 4, 22, 47, 25, 3, 2, 38, 25, 18, 20, 50, 41]
    main(data, ["white" for x in range(len(data))])


def BubbleSort(arr, main, sspeed):
    l = len(arr)
    for i in range(l, 1, -1):
        for j in range(i):
            if j+1 < i:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    main(arr, ["red" if x == j or x == j +
                         1 else "white" for x in range(len(data))])
                    time.sleep(sspeed)
    main(arr, ["green" for x in range(len(data))])


def SelectionSort(arr, main, sspeed):
    l = len(arr)
    for i in range(l):
        mini = i
        for j in range(i+1, l):
            if arr[j] < arr[mini]:
                mini = j
                main(
                    arr, ["red" if x == mini else "white" for x in range(len(data))])
                time.sleep(sspeed)
        if mini != i:
            arr[mini], arr[i] = arr[i], arr[mini]
            main(arr, ["red" if x == i or x ==
                 mini else "white" for x in range(len(data))])
            time.sleep(sspeed)
    main(arr, ["green" for x in range(len(data))])


def MainMS(data, main, sspeed):

    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = [0] * (n1)
        R = [0] * (n2)

        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            main(arr, ["red" if x == k else "white" for x in range(len(data))])
            time.sleep(sspeed)
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def mergeSort(arr, l, r):
        if l < r:
            m = l+(r-l)//2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)

    if __name__ == "__main__":
        mergeSort(data, 0, int(len(data)-1))
        main(data, ["green" for x in range(len(data))])


def InsertionSort(arr, main, sspeed):
    l = len(arr)
    for i in range(1, l):
        temp = arr[i]
        j = i-1
        main(arr, ["red" if x == j else "white" for x in range(len(data))])
        time.sleep(sspeed)
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            main(arr, ["red" if x == j or x == j +
                 1 else "white" for x in range(len(data))])
            j -= 1
        arr[j+1] = temp
        main(arr, ["red" if x == j+1 else "white" for x in range(len(data))])
        time.sleep(sspeed)
    main(arr, ["green" for x in range(len(data))])


def MyInS(arr, main, sspeed):
    l = len(arr)
    for i in range(1, l):
        for j in range(i, -1, -1):
            if arr[j] < arr[j-1] and j != 0:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                main(arr, ["red" if x == j or x == j +
                     1 else "white" for x in range(len(data))])
                time.sleep(sspeed)
    main(arr, ["green" for x in range(len(data))])


def start():
    global data
    algorithm = algo.get()
    speed = float(e4.get())
    if algorithm == "Bubble Sort":
        BubbleSort(data, main, speed)
    elif algorithm == "Selection Sort":
        SelectionSort(data, main, speed)
    elif algorithm == "Insertion Sort":
        InsertionSort(data, main, speed)
    elif algorithm == "Merge Sort":
        MainMS(data, main, speed)
    elif algorithm == "My InS":
        MyInS(data, main, speed)


l1 = Label(f1, text="Algorithms : ", bg="#e6a64e").grid(
    row=0, column=0, sticky=W, pady=5, padx=5)
algo = ttk.Combobox(f1, values=[
                    "Bubble Sort", "Selection Sort", "My InS", "Insertion Sort", "Merge Sort"])
algo.grid(row=0, column=1, pady=5, padx=5)
algo.current(0)
bttn1 = Button(f1, text="Generate", command=Generate)
bttn1.grid(row=0, column=4, pady=5, padx=5)

l2 = Label(f1, text="Size : ", bg="#e6a64e").grid(
    row=1, column=0, sticky=W, pady=5, padx=5)
e1 = Entry(f1, textvariable=IntVar())
e1.grid(row=1, column=1, pady=5, padx=5)

l3 = Label(f1, text="Min Value : ", bg="#e6a64e").grid(
    row=1, column=2, sticky=W, pady=5, padx=5)
e2 = Entry(f1, textvariable=IntVar())
e2.grid(row=1, column=3, pady=5, padx=5)

l4 = Label(f1, text="Max Value : ", bg="#e6a64e").grid(
    row=1, column=4, sticky=W, pady=5, padx=5)
e3 = Entry(f1, textvariable=IntVar())
e3.grid(row=1, column=5, pady=5, padx=5)

l5 = Label(f1, text="Speed : ", bg="#e6a64e").grid(
    row=0, column=2, sticky=W, pady=5, padx=5)
e4 = Entry(f1, textvariable=IntVar())
e4.grid(row=0, column=3, pady=5, padx=5)

bttn2 = Button(f1, text="START SORTING", command=start)
bttn2.grid(row=0, column=5, pady=5, padx=5)


win.mainloop()
