from tkinter import *
from tkinter import messagebox
root = Tk()
root.title(' Right Cross')
root.iconbitmap('C:/Users/Acer/OneDrive/Desktop/multithreading pythopn/tic-tac-toe_39453.ico')

click = True
count = 0

def disable():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)

def winner():
    global win
    win = False

    if button1["text"] == "✓" and button2["text"] == "✓" and button3["text"] == "✓":
        button1.config(bg="green")
        button2.config(bg="green")
        button3.config(bg="green")
        win = True
        messagebox.showinfo("Right Cross", "✓ wins")
        disable()

    elif button4["text"] == "✓" and button5["text"] == "✓" and button6["text"] == "✓":
        button4.config(bg="green")
        button5.config(bg="green")
        button6.config(bg="green")
        win = True
        messagebox.showinfo("Right Cross", "✓ wins")
        disable()

    elif button7["text"] == "✓" and button8["text"] == "✓" and button9["text"] == "✓":
        button7.config(bg="green")
        button8.config(bg="green")
        button9.config(bg="green")
        win = True
        messagebox.showinfo("Right Cross", "✓ wins")
        disable()

    elif button1["text"] == "✓" and button4["text"] == "✓" and button7["text"] == "✓":
        button1.config(bg="green")
        button4.config(bg="green")
        button7.config(bg="green")
        win = True
        messagebox.showinfo("Right Cross", "✓ wins")
        disable()

    elif button2["text"] == "✓" and button5["text"] == "✓" and button8["text"] == "✓":
        button2.config(bg="green")
        button5.config(bg="green")
        button8.config(bg="green")
        win = True
        messagebox.showinfo("Right Cross", "✓ wins")
        disable()

    elif button3["text"] == "✓" and button6["text"] == "✓" and button9["text"] == "✓":
        button3.config(bg="green")
        button6.config(bg="green")
        button9.config(bg="green")
        win = True
        messagebox.showinfo("Right Cross", "✓ wins")
        disable()

    elif button1["text"] == "✓" and button5["text"] == "✓" and button9["text"] == "✓":
        button1.config(bg="green")
        button5.config(bg="green")
        button9.config(bg="green")
        win = True
        messagebox.showinfo("Right Cross", "✓ wins")
        disable()

    elif button3["text"] == "✓" and button5["text"] == "✓" and button7["text"] == "✓":
        button3.config(bg="green")
        button5.config(bg="green")
        button7.config(bg="green")
        win = True
        messagebox.showinfo("Right Cross", "✓ wins")
        disable()



    elif button1["text"] == "✖" and button2["text"] == "✖" and button3["text"] == "✖":
        button1.config(bg="green")
        button2.config(bg="green")
        button3.config(bg="green")
        win = True
        messagebox.showinfo("Right Cross", "✖ wins")
        disable()

    elif button4["text"] == "✖" and button5["text"] == "✖" and button6["text"] == "✖":
        button4.config(bg="green")
        button5.config(bg="green")
        button6.config(bg="green")
        win = True
        messagebox.showinfo("Right Cross", "✖ wins")
        disable()

    elif button7["text"] == "✖" and button8["text"] == "✖" and button9["text"] == "✖":
        button7.config(bg="green")
        button8.config(bg="green")
        button9.config(bg="green")
        win = True
        messagebox.showinfo("Right Cross", "✖ wins")
        disable()

    elif button1["text"] == "✖" and button4["text"] == "✖" and button7["text"] == "✖":
        button1.config(bg="green")
        button4.config(bg="green")
        button7.config(bg="green")
        win = True
        messagebox.showinfo("Right Cross", "✖ wins")
        disable()

    elif button2["text"] == "✖" and button5["text"] == "✖" and button8["text"] == "✖":
        button2.config(bg="green")
        button5.config(bg="green")
        button8.config(bg="green")
        win = True
        messagebox.showinfo("Right Cross", "✖ wins")
        disable()

    elif button3["text"] == "✖" and button6["text"] == "✖" and button9["text"] == "✖":
        button3.config(bg="green")
        button6.config(bg="green")
        button9.config(bg="green")
        win = True
        messagebox.showinfo("Right Cross", "✖ wins")
        disable()

    elif button1["text"] == "✖" and button5["text"] == "✖" and button9["text"] == "✖":
        button1.config(bg="green")
        button5.config(bg="green")
        button9.config(bg="green")
        win = True
        messagebox.showinfo("Right Cross", "✖ wins")
        disable()

    elif button3["text"] == "✖" and button5["text"] == "✖" and button7["text"] == "✖":
        button3.config(bg="green")
        button5.config(bg="green")
        button7.config(bg="green")
        win = True
        messagebox.showinfo("Right Cross", "✖ wins")
        disable()
    
    elif count == 9 and not win:
        messagebox.showinfo("Right Cross", "The game is a draw")
        disable()






#function for the button
def b_function(b):
    global click, count

    if b["text"] == " " and click == True:
        b["text"] = "✓"
        click = False
        count +=count
        winner()

    elif b["text"] == " " and click == False:
        b["text"] = "✖"
        click = True
        count+=count
        winner()

    else:
        messagebox.showerror("Right Cross", "The button is Allready taken")

#buttons

button1 = Button(root, text=" ", height=3, width= 6,bg="white", command= lambda: b_function(button1))
button2 = Button(root, text=" ", height=3, width= 6,bg="white", command= lambda: b_function(button2))
button3 = Button(root, text=" ", height=3, width= 6,bg="white", command= lambda: b_function(button3))

button4 = Button(root, text=" ", height=3, width= 6,bg="white", command= lambda: b_function(button4))
button5 = Button(root, text=" ", height=3, width= 6,bg="white", command= lambda: b_function(button5))
button6 = Button(root, text=" ", height=3, width= 6,bg="white", command= lambda: b_function(button6))

button7 = Button(root, text=" ", height=3, width= 6,bg="white", command= lambda: b_function(button7))
button8 = Button(root, text=" ", height=3, width= 6,bg="white", command= lambda: b_function(button8))
button9 = Button(root, text=" ", height=3, width= 6,bg="white", command= lambda: b_function(button9))



button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

menu44 = Menu(root)
root.config(menu=menu44)

# options = Menu(menu44, tearoff=False)
# menu44.add_cascade(label="Option", menu= options)
# options.add_command(label="Reset", command = Reset())




root.mainloop()
