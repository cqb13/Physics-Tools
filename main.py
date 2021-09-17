from fractions import Fraction
import tkinter as tk
from random import *
import webbrowser
import pyperclip
import math
import time


# auto-py-to-exe
class Win1:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x300")
        self.frame = tk.Frame(self.master)
        self.label = tk.Label(self.frame, text="Welcome to calculators", font=("arial", 10))
        self.label.pack()
        self.label = tk.Label(self.frame, text="Made by cqb13", font=("arial", 10))
        self.label.pack()
        self.github = tk.Button(text=f"Github", command=github)
        self.github.place(x=5, y=5)
        self.butnew("Calculator", "2", Win2)
        self.butnew2("About", "A", WinA)
        self.button = tk.Button()
        self.release = tk.Button(text=f"Releases", command=latest_release)
        self.release.place(x=426, y=5)
        self.close = tk.Button(text=f"Close", command=end)
        self.close.place(x=447, y=260)
        self.frame.pack()

    def butnew(self, text, number, _class):
        tk.Button(self.frame, text=text, command=lambda: self.new_window(number, _class)).pack()

    def butnew2(self, text, number, _class):
        tk.Button(text=text, command=lambda: self.new_window(number, _class)).place(x=5, y=260)

    def butnew3(self, number, _class):
        tk.Button(command=lambda: self.new_win(number, _class)).place(x=300, y=297)

    def new_window(self, number, _class):
        self.new = tk.Toplevel(self.master)
        _class(self.new, number)

    def new_win(self, number, _class):
        self.new = tk.Toplevel(self.master)
        _class(self.new, number)


def github():  # goes to my github
    webbrowser.open_new("https://github.com/cqb13")


def latest_release():
    webbrowser.open_new("https://github.com/cqb13/utility-app/releases")


def end():
    exit()


class Win2:
    def __init__(self, master, number):  # does things with numbers
        self.tk = tk
        self.var1 = tk.IntVar()
        self.number = number
        self.master = master
        self.master.geometry("400x450+200+200")  # window size
        self.master.resizable(False, False)  # window size cant be changed
        self.frame = tk.Frame(self.master)
        self.name = tk.Label(self.frame, text="Calculator")  # name of script
        self.name.pack()
        self.about2 = tk.Label(self.frame, text="press clear before running again", font=("arial", 10))  # how to use
        self.about2.pack()
        self.num1e = tk.Label(self.frame, text="enter first number")  # label for text box
        self.num1e.pack()
        self.num1 = tk.Entry(self.frame, text="num1", font=("arial", 10))  # text box
        self.num1.pack()
        self.op_pic = tk.Label(self.frame, text="pick an operation")  # label for menu
        self.op_pic.pack()
        self.operations = [  # drop down menu with the operations
            "+",
            "-",
            "*",
            "/",
            "²",
            "³",
            "√",
            "d to a/b",
            "a/b to d"
        ]
        self.variable = tk.StringVar(master)
        self.variable.set(self.operations[0])  # defualt option
        self.menu = tk.OptionMenu(self.frame, self.variable, *self.operations)  # where to put the menu
        self.menu.pack()
        self.num2e = tk.Label(self.frame, text="enter second number")  # label for text box
        self.num2e.pack()
        self.num2 = tk.Entry(self.frame, text="num2", font=("arial", 10))  # where to put second number
        self.num2.pack()
        self.solve = tk.Button(self.frame, text=f"Solve", command=self.math)  # button to solve
        self.solve.pack()
        self.copyp = tk.Button(self.frame, text=f"Copy Answer", command=self.copy_answer)  # button to copy password
        self.copyp.pack()
        self.clear = tk.Button(self.frame, text=f"Clear", command=self.clear_results)
        self.clear.pack()  # will clear answers(temporary till it does it on its own)
        self.quit = tk.Button(self.frame, text=f"Close", command=self.close_window)  # button to close window
        self.quit.pack()
        self.help = tk.Button(self.frame, text=f" Help ", command=self.help)  # button to open help window
        self.help.pack()
        self.answer_name = tk.Label(self.frame, text="the answer is")  # label for answer area
        self.answer_name.pack()
        self.frame.pack()

    def math(self):
        self.stat = True
        self.n1 = self.num1.get()
        self.n2 = self.num2.get()
        self.fraction1 = (str(float(Fraction(self.n1))))  # number format
        self.fraction2 = (str(float(Fraction(self.n2))))  # number format
        if self.n1 == "":  # if the first number is not found it will stop here
            self.stat = False  # for error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant be changed
            self.error1.title('error 404')  # name of widnow
            self.tk.Label(self.error1, text='error 404 first number not found ¯\_(ツ)_/¯').pack()  # message
            self.tk.Label(self.error1, text='please enter the first number and try again').pack()  # message
            self.error1.after(5000, self.error1.destroy)  # window will close in 5 seconds
        elif self.n2 == "" and self.variable.get() == (self.operations[0]):  # if first number not found for addition
            self.stat = False  # for error not show
            self.error2 = tk.Toplevel(window)
            self.error2.resizable(False, False)  # window size cant change
            self.error2.title('error 404')  # name of window
            self.tk.Label(self.error2, text='error 404 second number not found ¯\_(ツ)_/¯').pack()  # message
            self.tk.Label(self.error2,
                          text='this operation needs a second number please enter a second number and try again').pack()  # message
            self.error2.after(5000, self.error2.destroy)  # window will close in 5 seconds
        elif self.n2 == "" and self.variable.get() == (self.operations[1]):  # first number not found for subtraction
            self.stat = False  # error not show
            self.error3 = tk.Toplevel(window)
            self.error3.resizable(False, False)  # window size cant change
            self.error3.title('error 404')  # name of window
            self.tk.Label(self.error3, text='error 404 second number not found ¯\_(ツ)_/¯').pack()  # message
            self.tk.Label(self.error3,
                          text='this operation needs a second number please enter a second number and try again').pack()  # message
            self.error3.after(5000, self.error3.destroy)  # window will close in 5 seconds
        elif self.n2 == "" and self.variable.get() == (self.operations[2]):  # first number not found for multiplication
            self.stat = False  # error not show
            self.error4 = tk.Toplevel(window)
            self.error4.resizable(False, False)  # window size cant change
            self.error4.title('error 404')  # name of window
            self.tk.Label(self.error4, text='error 404 second number not found ¯\_(ツ)_/¯').pack()  # message
            self.tk.Label(self.error4,
                          text='this operation needs a second number please enter a second number and try again').pack()  # message
            self.error4.after(5000, self.error4.destroy)  # window will close in 5 seconds
        elif self.n2 == "" and self.variable.get() == (self.operations[3]):  # first number not found for division
            self.stat = False  # error not show
            self.error5 = tk.Toplevel(window)
            self.error5.resizable(False, False)  # window size cant change
            self.error5.title('error 404')  # window name
            self.tk.Label(self.error5, text='error 404 second number not found ¯\_(ツ)_/¯').pack()  # message
            self.tk.Label(self.error5,
                          text='this operation needs a second number please enter a second number and try again').pack()  # message
            self.error5.after(5000, self.error5.destroy)  # window will close in 5 seconds
        elif self.n1 == '0' and self.n2 == '0' and self.variable.get() == (self.operations[3]):
            self.stat = False  # error not show
            # the thing that siri says when u ask 0 / 0
            self.popup0 = tk.Toplevel(window)
            self.popup0.resizable(False, False)  # window size cant change
            self.popup0.title('is it siri?')  # name of window
            self.tk.Label(self.popup0,
                          text='Imagine that you have 0 cookies and you split them evenly among 0 friends.').pack()  # message
            self.tk.Label(self.popup0, text='How many cookies does each person get?').pack()  # message
            self.tk.Label(self.popup0, text='See? It doesnt make sense.').pack()  # mesage
            self.tk.Label(self.popup0,
                          text='And Cookie Monster is sad that there are no cookies, and you are sad that you have no friends.').pack()  # message
            self.popup0.after(10000, self.popup0.destroy)  # window will close in 10 seconds
        elif self.variable.get() == (self.operations[0]):  # addition
            self.result = (Fraction(self.fraction1) + Fraction(self.fraction2))  # result
        elif self.variable.get() == (self.operations[1]):  # subtraction
            self.result = (Fraction(self.fraction1) - Fraction(self.fraction2))  # result
        elif self.variable.get() == (self.operations[2]):  # multiplication
            self.result = (Fraction(self.fraction1) * Fraction(self.fraction2))  # result
        elif self.variable.get() == (self.operations[3]):  # division
            self.result = (Fraction(self.fraction1) / Fraction(self.fraction2))  # result
        elif self.variable.get() == (self.operations[4]):  # cubing
            self.result = (str(float(self.n1) * float(self.n1)))  # result
        elif self.variable.get() == (self.operations[5]):  # squaring
            self.result = (str(float(self.n1) * float(self.n1) * float(self.n1)))  # result
        elif self.variable.get() == (self.operations[6]):  # square root (fix needing second num)
            self.result = (math.sqrt(float(self.n1)))  # result
        elif self.variable.get() == (self.operations[7]):  # decimal to fraction
            self.result = (Fraction(str(float(self.n1))))  # result
        elif self.variable.get() == (self.operations[8]):  # fraction to a decimal
            self.result = (str(float(Fraction(self.n1))))  # result
        else:  # error is not pisible in this program but if you mess with it and break something this will tell you
            self.stat = False  # error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant change
            self.error1.title('error 404')  # name of window
            self.tk.Label(self.error1, text='error 404 operation not found ¯\_(ツ)_/¯').pack()  # message
            self.tk.Label(self.error1,
                          text='this error should not be possible if you get it you did something very wrong').pack()  # message
            self.error1.after(5000, self.error1.destroy)  # window will close in 5 seconds

        if not self.stat:
            print('')  # error not show
        else:
            self.results = tk.Label(self.frame, text=self.result)  # prints result
            self.results.pack()
            self.ans = int(self.result)

    def copy_answer(self):
        pyperclip.copy(self.ans)

    def clear_results(self):
        self.results.destroy()

    def help(self):  # help window
        self.help_p = tk.Toplevel(window)
        self.help_p.resizable(False, False)  # window size cant change
        self.help_p.title('help')  # name of window
        self.tk.Label(self.help_p, text='help').pack()  # message
        self.tk.Label(self.help_p, text='window will close in 20 seconds').pack()  # message
        self.tk.Label(self.help_p, text='use a/b format to use fractions in operations').pack()  # message
        self.tk.Label(self.help_p, text='+ = addition').pack()  # message
        self.tk.Label(self.help_p, text='- = subtraction').pack()  # message
        self.tk.Label(self.help_p, text='* = multiplication').pack()  # message
        self.tk.Label(self.help_p, text='/ = division').pack()  # message
        self.tk.Label(self.help_p, text='² = squaring a number(only uses first number)').pack()  # message
        self.tk.Label(self.help_p, text='³ = cubing a number(only uses first number )').pack()  # message
        self.tk.Label(self.help_p, text='√ = square root of a number(only uses first number)').pack()  # message
        self.tk.Label(self.help_p, text='d to a/b = decimal to a fraction(only uses first number)').pack()  # message
        self.tk.Label(self.help_p, text='a/b to d = fraction to a decimal(only uses first number)').pack()  # message
        self.help_p.after(10000, self.help_p.destroy)  # window will close in 10 seconds

    def close_window(self):  # closes window
        self.master.destroy()


class WinA:
    def __init__(self, master, number):
        self.number = number
        self.master = master
        self.master.geometry("400x450+200+200")  # window size
        self.master.resizable(False, False)  # window size cant change
        self.frame = tk.Frame(self.master)
        self.name = tk.Label(self.frame, text="About", font=("arial", 10))
        self.name.pack()
        self.line1 = tk.Label(self.frame, text='calculators is an project I have always wanted to do', font=('arial', 10))
        self.line1.pack()
        self.line1 = tk.Label(self.frame, text='its goal is to put all the calculators you could ever need in one place', font=('arial', 10))
        self.line1.pack()
        self.line1 = tk.Label(self.frame, text='you can find the code and past versions of calculators on my github', font=('arial', 10))
        self.line1.pack()
        self.cqb13_github = tk.Button(self.frame, text=f"cqb13 github", command=github)  # button to github
        self.cqb13_github.pack()
        self.quit = tk.Button(self.frame, text=f"Close", command=self.close_window)
        self.quit.pack()
        self.frame.pack()

    def close_window(self):
        self.master.destroy()


window = tk.Tk()
window.title("calculators")
window.resizable(False, False)
app = Win1(window)
window.mainloop()
