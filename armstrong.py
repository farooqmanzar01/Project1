
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


win= Tk()
win.geometry("550x250")

def armstrong(num):
   sum = 0
   temp = num
   while temp > 0:
      digit = temp % 10
      sum += digit ** 3
      temp //= 10
   if num == sum:
      messagebox.showinfo(title="Output", message=f"{num} is an Armstrong Number")
   else:
      messagebox.showerror(title="Output", message=f"{num} is not an Armstrong Number")

def display_text():
   global entry
   string= entry.get()
   #validate input
   if(string.isalpha()):
       messagebox.showerror(message="Please enter a number")
   elif(int(string)<100):
       messagebox.showerror(message="Please enter a number between 100 and 999")
   elif(int(string)>999):
       messagebox.showerror(message="Please enter a number between 100 and 999")
   else:
       #if validated check armstrong
       armstrong(int(string))


label1=Label(win, text="Enter number to find armstrong", font=("Arial 22 bold"))
label1.pack()

entry= Entry(win, width= 40)
entry.focus_set()
entry.pack(pady=20)

ttk.Button(win, text= "Submit",width= 20, command= display_text).pack()

win.mainloop()
