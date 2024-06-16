import threading
import time
import tkinter as tk
from queue import Queue

class SharedValue:
    def __init__(self, initial_value):
        self.value = initial_value
        self.lock = threading.Lock()

def add_rectangle(canvas, x1, y1, x2, y2, fill):
    rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill=fill)
    return rectangle

def delete_rectangle(canvas, rectangle):
    canvas.delete(rectangle)

def task1(label_red, t1, stop_event, event_queue):
    x_r1, x_r2, y_r1, y_r2, fill_red = 100, 250, 150, 150, "red"
    while not stop_event.is_set():
        if y_r2 < 600:
            while y_r2 < 600 and not stop_event.is_set():
                with t2.lock, t3.lock, t4.lock:
                    t1.value = (y_r2 - y_r1) * 0.1 * (x_r2 - x_r1) * 0.1
                    label_red.config(text='S='+str(t1.value))
                    rectangle = add_rectangle(canvas, x_r1, y_r1, x_r2, y_r2, fill_red)
                    y_r2 += 5
                    root.after(50, delete_rectangle, canvas, rectangle)
                time.sleep(0.05)

        if y_r2 == 600:
            while y_r2 != 180 and not stop_event.is_set():
                with t2.lock, t3.lock, t4.lock:
                    t1.value = (y_r2 - y_r1) * 0.1 * (x_r2 - x_r1) * 0.1
                    label_red.config(text='S='+str(t1.value))
                    rectangle = add_rectangle(canvas, x_r1, y_r1, x_r2, y_r2, fill_red)
                    y_r2 -= 5
                    root.after(50, delete_rectangle, canvas, rectangle)
                time.sleep(0.05)
    event_queue.put("Task1 Finished")

def task2(label_green, t2, stop_event, event_queue):
    x_r1, x_r2, y_r1, y_r2, fill_red = 300, 450, 150, 150, "green"
    while not stop_event.is_set():
        if y_r2 < 600:
            while y_r2 < 600 and not stop_event.is_set():
                with t1.lock, t3.lock, t4.lock:
                    t2.value = (y_r2 - y_r1) * 0.1 * (x_r2 - x_r1) * 0.1
                    label_green.config(text='S='+str(t2.value))
                    rectangle = add_rectangle(canvas, x_r1, y_r1, x_r2, y_r2, fill_red)
                    y_r2 += 5
                    root.after(40, delete_rectangle, canvas, rectangle)
                time.sleep(0.04)
        if y_r2 == 600:
            while y_r2 != 180 and not stop_event.is_set():
                with t1.lock, t3.lock, t4.lock:
                    t2.value = (y_r2 - y_r1) * 0.1 * (x_r2 - x_r1) * 0.1
                    label_green.config(text='S=' + str(t2.value))
                    rectangle = add_rectangle(canvas, x_r1, y_r1, x_r2, y_r2, fill_red)
                    y_r2 -= 5
                    root.after(40, delete_rectangle, canvas, rectangle)
                time.sleep(0.04)
    event_queue.put("Task2 Finished")

def task3(label_blue, t3, stop_event,event_queue):
    x_r1, x_r2, y_r1, y_r2, fill_red = 500, 650, 150, 150, "blue"
    while not stop_event.is_set():
        if y_r2 < 600:
            while y_r2 < 600 and not stop_event.is_set():
                with t1.lock, t2.lock, t4.lock:
                    t3.value = (y_r2 - y_r1) * 0.1 * (x_r2 - x_r1) * 0.1
                    label_blue.config(text='S='+str(t3.value))
                    rectangle = add_rectangle(canvas, x_r1, y_r1, x_r2, y_r2, fill_red)
                    y_r2 += 5
                    root.after(70, delete_rectangle, canvas, rectangle)
                time.sleep(0.07)
        if y_r2 == 600:
            while y_r2 != 180 and not stop_event.is_set():
                with t1.lock, t2.lock, t4.lock:
                    t3.value = (y_r2 - y_r1) * 0.1 * (x_r2 - x_r1) * 0.1
                    label_blue.config(text='S='+str(t3.value))
                    rectangle = add_rectangle(canvas, x_r1, y_r1, x_r2, y_r2, fill_red)
                    y_r2 -= 5
                    root.after(70, delete_rectangle, canvas, rectangle)
                time.sleep(0.07)
    event_queue.put("Task3 Finished")
def task4(label_orange, t4, stop_event, event_queue):
    x_r1, x_r2, y_r1, y_r2, fill_red = 700, 850, 150, 150, "orange"
    while not stop_event.is_set() :
        if y_r2 < 600:
            while y_r2 < 600 and not stop_event.is_set():
                with t1.lock, t2.lock, t3.lock:
                    t4.value = (y_r2 - y_r1) * 0.1 * (x_r2 - x_r1) * 0.1
                    label_orange.config(text='S=' + str(t4.value))
                    rectangle = add_rectangle(canvas, x_r1, y_r1, x_r2, y_r2, fill_red)
                    y_r2 += 5
                    root.after(20, delete_rectangle, canvas, rectangle)
                time.sleep(0.02)
        if y_r2 == 600:
            while y_r2 != 180 and not stop_event.is_set():
                with t1.lock, t2.lock, t3.lock:
                    t4.value = (y_r2 - y_r1) * 0.1 * (x_r2 - x_r1) * 0.1
                    label_orange.config(text='S=' + str(t4.value))
                    rectangle = add_rectangle(canvas, x_r1, y_r1, x_r2, y_r2, fill_red)
                    y_r2 -= 5
                    root.after(20, delete_rectangle, canvas, rectangle)
                time.sleep(0.02)
    event_queue.put("Task4 Finished")

def total_task(label_our, t1, t2, t3, t4):
    while True:
        with t1.lock, t2.lock, t3.lock, t4.lock:
            total = t1.value + t2.value + t3.value + t4.value
        label_our.config(text='Загальна площа: ' + str(total))
        time.sleep(0.001)

def red_start():
    global stop_eventR
    stop_eventR.clear()
    task1_thread = threading.Thread(target=task1, args=(label_red, t1, stop_eventR, event_queue1))
    task1_thread.start()

def red_stop(t1):
    t1.value=0
    # label_red.config(text='S=' + str(t1.value))
    stop_eventR.set()
    event_queue1.put("Stop Task1")



def green_start():
    global stop_eventG
    stop_eventG.clear()
    task2_thread = threading.Thread(target=task2, args=(label_green, t2, stop_eventG, event_queue1))
    task2_thread.start()

def green_stop(t2):
    t2.value=0
    # label_green.config(text='S=' + str(t2.value))
    stop_eventG.set()
    event_queue1.put("Stop Task2")


def blue_start():
    global stop_eventB
    stop_eventB.clear()
    task3_thread = threading.Thread(target=task3, args=(label_blue, t3, stop_eventB, event_queue1))
    task3_thread.start()

def blue_stop(t3):
    t3.value=0
    # label_blue.config(text='S=' + str(t3.value))
    stop_eventB.set()
    event_queue1.put("Stop Task3")


def orange_start():
    global stop_eventO
    stop_eventO.clear()
    task4_thread = threading.Thread(target=task4, args=(label_orange, t4, stop_eventO, event_queue1))
    task4_thread.start()

def orange_stop(t4):
    t4.value=0
    # label_orange.config(text='S=' + str(t4.value))
    stop_eventO.set()
    event_queue1.put("Stop Task4")


if __name__ == "__main__":
    root = tk.Tk()
    t1 = SharedValue(0)
    t2 = SharedValue(0)
    t3 = SharedValue(0)
    t4 = SharedValue(0)

    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack()
    canvas.create_text(500, 50, text='Площина прямокутників у кв. см', fill='red', font='Verdana 20')

    label_our = tk.Label(root, text='', font='Verdana 16', fg='red')
    label_our.place(x=350, y=700)

    label_red=tk.Label(root,text='')
    label_red.place(x=150,y=100)
    button_red_start = tk.Button(root, text='Start', command=red_start)
    button_red_start.place(x=150, y=640)
    button_red_cancel = tk.Button(root, text='Clear', command=lambda: red_stop(t1))
    button_red_cancel.place(x=150, y=670)

    label_green = tk.Label(root, text='')
    label_green.place(x=350, y=100)

    button_green_start = tk.Button(root, text='Start', command=green_start)
    button_green_start.place(x=350, y=640)
    button_green_cancel = tk.Button(root, text='Clear', command=lambda: green_stop(t2))
    button_green_cancel.place(x=350, y=670)

    label_blue = tk.Label(root, text='')
    label_blue.place(x=550, y=100)

    button_blue_start = tk.Button(root, text='Start', command=blue_start)
    button_blue_start.place(x=550, y=640)
    button_blue_cancel = tk.Button(root, text='Clear', command=lambda: blue_stop(t3))
    button_blue_cancel.place(x=550, y=670)

    label_orange = tk.Label(root, text='')
    label_orange.place(x=750, y=100)
    button_orange_start = tk.Button(root, text='Start', command=orange_start)
    button_orange_start.place(x=750, y=640)
    button_orange_cancel = tk.Button(root, text='Clear', command=lambda: orange_stop(t4))
    button_orange_cancel.place(x=750, y=670)

    stop_eventR = threading.Event()
    stop_eventG = threading.Event()
    stop_eventB = threading.Event()
    stop_eventO = threading.Event()
    event_queue1 = Queue()

    task1_thread = threading.Thread(target=task1, args=(label_red, t1, stop_eventR, event_queue1), name="Task1")
    task2_thread = threading.Thread(target=task2, args=(label_green, t2, stop_eventG, event_queue1), name="Task2")
    task3_thread = threading.Thread(target=task3, args=(label_blue, t3, stop_eventB, event_queue1), name="Task3")
    task4_thread = threading.Thread(target=task4, args=(label_orange, t4, stop_eventO, event_queue1), name="Task4")
    total_thread = threading.Thread(target=total_task, args=(label_our, t1, t2, t3, t4))

    total_thread.start()
    canvas.create_text(500, 50, text='Площина прямокутників у кв. см', fill='red', font='Verdana 20')
    canvas.create_text(180, 130, text='Thread 1', fill='gray', font='Verdana 12')
    canvas.create_text(380, 130, text='Thread 2', fill='gray', font='Verdana 12')
    canvas.create_text(580, 130, text='Thread 3', fill='gray', font='Verdana 12')
    canvas.create_text(780, 130, text='Thread 4', fill='gray', font='Verdana 12')
    canvas.create_text(250, 720, text='Thread 5', fill='gray', font='Verdana 12')

    root.geometry('1000x750+300+0')
    root.mainloop()