import tkinter as tk

# version 0.5
# made with python 3.7.3
# initializing variables
HEIGHT = 550
WIDTH = 400
cur_num = " "
cur_num2 = " "
store_num = " "
op = " "
final_num = " "

def num(numero):
    global cur_num
    global cur_num2
    cur_num = cur_num + numero
    screen["text"] = cur_num
    cur_num2 = cur_num

def del_op():
    global cur_num
    global cur_num2
    global store_num
    global op
    global final_num

    cur_num = " "
    cur_num2 = " "
    store_num = " "
    op = " "
    final_num = " "
    screen["text"] = " "

def add_op():
    global store_num
    global cur_num
    global op
    store_num = cur_num
    op = 1
    screen["text"] = " "
    cur_num = " "

def sub_op():
    global store_num
    global cur_num
    global op
    store_num = cur_num
    op = 2
    screen["text"] = " "
    cur_num = " "

def mult_op():
    global store_num
    global cur_num
    global op
    store_num = cur_num
    op = 3
    screen["text"] = " "
    cur_num = " "

def div_op():
    global store_num
    global cur_num
    global op
    store_num = cur_num
    op = 4
    screen["text"] = " "
    cur_num = " "

def final_op():
    global store_num
    global cur_num2
    global final_num
    int_store_num = float(store_num)
    int_cur_num2 = float(cur_num2)

    if op == 1:
        final_num = int_store_num + int_cur_num2
        screen["text"] = final_num

    elif op == 2:
        final_num = int_store_num - int_cur_num2
        screen["text"] = final_num

    elif op == 3:
        final_num = int_store_num * int_cur_num2
        screen["text"] = final_num

    elif op == 4:
        final_num = int_store_num / int_cur_num2
        screen["text"] = final_num

root = tk.Tk()

root.title("Calculator")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
# canvas to make the app a certain size

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor="n")
# placing the frame for all of the other objects

button0 = tk.Button(frame, text="0", bg="lightgrey", fg="black", font=40, command=lambda: num("0"))
button0.place(relx=0, rely=0.8, relwidth=0.75, relheight=0.2)
# button for the number 0

button_Equal = tk.Button(frame, text="=", bg="lightgrey", fg="black", font=40, command= final_op)
button_Equal.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.1)
# button for making result appear on screen

button_Remove = tk.Button(frame, text="DEL", bg="lightgrey", fg="black", font=40, command= del_op)
button_Remove.place(relx=0.75, rely=0.1, relwidth=0.25, relheight=0.1)
# button for clearing screen and resetting variables

button_Division = tk.Button(frame, text="/", bg="lightgrey", fg="black", font=40, command= div_op)
button_Division.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)
# button for the division opertaion

button_Multiplication = tk.Button(frame, text="*", bg="lightgrey", fg="black", font=40, command= mult_op)
button_Multiplication.place(relx=0.75, rely=0.6, relwidth=0.25, relheight=0.2)
# button for the multiplication operation

button_Subtraction = tk.Button(frame, text="-", bg="lightgrey", fg="black", font=40, command= sub_op)
button_Subtraction.place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.2)
# button for the subtraction operation

button_Addition = tk.Button(frame, text="+", bg="lightgrey", fg="black", font=40, command= add_op)
button_Addition.place(relx=0.75, rely=0.2, relwidth=0.25, relheight=0.2)
# button for the addition operation

button1 = tk.Button(frame, text="1", bg="lightgrey", fg="black", font=40, command=lambda: num("1"))
button1.place(relx=0, rely=0.6, relwidth=0.25, relheight=0.2)
# button for the number 1

button2 = tk.Button(frame, text="2", bg="lightgrey", fg="black", font=40, command=lambda: num("1"))
button2.place(relx=0.25, rely=0.6, relwidth=0.25, relheight=0.2)
#button for the number 2

button3 = tk.Button(frame, text="3", bg="lightgrey", fg="black", font=40, command=lambda: num("3"))
button3.place(relx=0.50, rely=0.6, relwidth=0.25, relheight=0.2)
#button for the number 3

button4 = tk.Button(frame, text="4", bg="lightgrey", fg="black", font=40, command=lambda: num("4"))
button4.place(relx=0, rely=0.4, relwidth=0.25, relheight=0.2)
#button for the number 4

button5 = tk.Button(frame, text="5", bg="lightgrey", fg="black", font=40, command=lambda: num("5"))
button5.place(relx=0.25, rely=0.4, relwidth=0.25, relheight=0.2)
#button for the number 5

button6 = tk.Button(frame, text="6", bg="lightgrey", fg="black", font=40, command=lambda: num("6"))
button6.place(relx=0.5, rely=0.4, relwidth=0.25, relheight=0.2)
#button for the number 6

button7 = tk.Button(frame, text="7", bg="lightgrey", fg="black", font=40, command=lambda: num("7"))
button7.place(relx=0, rely=0.2, relwidth=0.25, relheight=0.2)
#button for the number 7

button8 = tk.Button(frame, text="8", bg="lightgrey", fg="black", font=40, command=lambda: num("8"))
button8.place(relx=0.25, rely=0.2, relwidth=0.25, relheight=0.2)
#button for the number 8

button9 = tk.Button(frame, text="9", bg="lightgrey", fg="black", font=40, command=lambda: num("9"))
button9.place(relx=0.5, rely=0.2, relwidth=0.25, relheight=0.2)
#button for the number 9

screen = tk.Label(frame, text=" ", bg="lightgrey", fg="black", font=40 )
screen.place(relx=0, rely=0, relwidth=0.75, relheight=0.2)
# the screen where the numbers will be shown

# just configuring the GUI
root.mainloop()
