from fractions import Fraction
import tkinter as tk
import webbrowser
import pyperclip
import math


# auto-py-to-exe
class Win1:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x300")
        self.frame = tk.Frame(self.master)
        self.label = tk.Label(self.frame, text="--- Math Tools ---", font=("arial", 10))
        self.label.pack()
        self.label = tk.Label(self.frame, text="Made By: cqb13", font=("arial", 10))
        self.label.pack()
        self.github = tk.Button(text=f"Github", command=github)
        self.github.place(x=5, y=5)
        self.butnew("Calculator", "2", Win2)
        self.butnew("Unit Conversion", "3", Win3)
        self.butnew("Pythagorean Theorem", "4", Win4)
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
    webbrowser.open_new("https://github.com/cqb13/calculators/releases")


def end():
    exit()


# Calculator (done)
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
            self.result = (Fraction(self.fraction1) + Fraction(self.fraction2))
        elif self.variable.get() == (self.operations[1]):  # subtraction
            self.result = (Fraction(self.fraction1) - Fraction(self.fraction2))
        elif self.variable.get() == (self.operations[2]):  # multiplication
            self.result = (Fraction(self.fraction1) * Fraction(self.fraction2))
        elif self.variable.get() == (self.operations[3]):  # division
            self.result = (Fraction(self.fraction1) / Fraction(self.fraction2))
        elif self.variable.get() == (self.operations[4]):  # cubing
            self.result = (str(float(self.n1) * float(self.n1)))
        elif self.variable.get() == (self.operations[5]):  # squaring
            self.result = (str(float(self.n1) * float(self.n1) * float(self.n1)))
        elif self.variable.get() == (self.operations[6]):  # square root (fix needing second num)
            self.result = (math.sqrt(float(self.n1)))
        elif self.variable.get() == (self.operations[7]):  # decimal to fraction
            self.result = (Fraction(str(float(self.n1))))
        elif self.variable.get() == (self.operations[8]):  # fraction to a decimal
            self.result = (str(float(Fraction(self.n1))))
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


# Unit Conversion
class Win3:
    def __init__(self, master, number):  # does things with numbers
        self.tk = tk
        self.var1 = tk.IntVar()
        self.number = number
        self.master = master
        self.master.geometry("400x450+200+200")  # window size
        self.master.resizable(False, False)  # window size cant be changed
        self.frame = tk.Frame(self.master)
        self.name = tk.Label(self.frame, text="Unit Conversion")  # name of script
        self.name.pack()
        self.about2 = tk.Label(self.frame, text="press clear before running again", font=("arial", 10))  # how to use
        self.about2.pack()
        self.label1 = tk.Label(self.frame, text='enter a number', font=('arial', 10))
        self.label1.pack()
        self.amount = tk.Entry(self.frame, text='first unit', font=('arial', 10))
        self.amount.pack()
        self.label2 = tk.Label(self.frame, text='from', font=('arial', 10))
        self.label2.pack()
        self.units = [  # drop down menu with the units
            'millimeters',  # 0
            'centimeter',  # 1
            'meter',  # 2
            'kilometer',  # 3
            'inch',  # 4
            'foot',  # 5
            'yard',  # 6
            'mile',  # 7
            'nautical mile'  # 8
        ]
        self.variable = tk.StringVar(master)
        self.variable.set(self.units[0])  # defualt option
        self.menu = tk.OptionMenu(self.frame, self.variable, *self.units)  # where to put the menu
        self.menu.pack()
        self.label4 = tk.Label(self.frame, text='to', font=('arial', 10))
        self.label4.pack()
        self.units2 = [  # drop down menu with the units
            'millimeters',  # 0
            'centimeter',  # 1
            'meter',  # 2
            'kilometer',  # 3
            'inch',  # 4
            'foot',  # 5
            'yard',  # 6
            'mile',  # 7
            'nautical mile'  # 8
        ]
        self.variable2 = tk.StringVar(master)
        self.variable2.set(self.units2[0])  # defualt option
        self.menu = tk.OptionMenu(self.frame, self.variable2, *self.units2)  # where to put the menu
        self.menu.pack()
        self.converts = tk.Button(self.frame, text='Convert', command=self.converting)
        self.converts.pack()
        self.copyp = tk.Button(self.frame, text=f"Copy Answer", command=self.copy_answer)  # button to copy password
        self.copyp.pack()
        self.clear = tk.Button(self.frame, text=f"Clear", command=self.clear_results)
        self.clear.pack()  # will clear answers(temporary till it does it on its own)
        self.quit = tk.Button(self.frame, text=f"Close", command=self.close_window)  # button to close window
        self.quit.pack()
        self.ans = tk.Label(self.frame, text=f'the answer is', font=('arial', 10))
        self.ans.pack()
        self.frame.pack()

    def converting(self):
        self.stat = True
        self.convering_unit = (int(float(self.amount.get())))
        if self.variable.get() == (self.units[0]) and self.variable2.get() == (
                self.units2[0]) or self.variable.get() == (self.units[1]) and self.variable2.get() == (
                self.units2[1]) or self.variable.get() == (self.units[2]) and self.variable2.get() == (
                self.units2[2]) or self.variable.get() == (self.units[3]) and self.variable2.get() == (
                self.units2[3]) or self.variable.get() == (self.units[4]) and self.variable2.get() == (
                self.units2[4]) or self.variable.get() == (self.units[5]) and self.variable2.get() == (
                self.units2[5]) or self.variable.get() == (self.units[6]) and self.variable2.get() == (
                self.units2[6]) or self.variable.get() == (self.units[7]) and self.variable2.get() == (
                self.units2[7]) or self.variable.get() == (self.units[8]) and self.variable2.get() == (self.units2[8]):
            self.stat = False  # for error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant be changed
            self.error1.title('error 404')  # name of widnow
            self.tk.Label(self.error1, text='error 404 conversion not found ¯\_(ツ)_/¯').pack()  # message
            self.tk.Label(self.error1, text='please convert to a different unit').pack()  # message
            self.error1.after(5000, self.error1.destroy)  # window will close in 5 seconds
        elif self.variable.get() == (self.units[0]) and self.variable2.get() == (self.units2[1]):
            self.result = self.convering_unit / 10  # mm to cm
        elif self.variable.get() == (self.units[0]) and self.variable2.get() == (
                self.units2[2]) or self.variable.get() == (self.units[2]) and self.variable2.get() == (self.units2[3]):
            self.result = self.convering_unit / 1000  # mm to m and m to km
        elif self.variable.get() == (self.units[0]) and self.variable2.get() == (self.units2[3]):
            self.result = self.convering_unit / 1e+6  # mm to km
        elif self.variable.get() == (self.units[0]) and self.variable2.get() == (self.units2[4]):
            self.result = self.convering_unit / 25.4  # mm to in
        elif self.variable.get() == (self.units[0]) and self.variable2.get() == (self.units2[5]):
            self.result = self.convering_unit / 305  # mm to ft
        elif self.variable.get() == (self.units[0]) and self.variable2.get() == (self.units2[6]):
            self.result = self.convering_unit / 914  # mm to yd
        elif self.variable.get() == (self.units[0]) and self.variable2.get() == (self.units2[7]):
            self.result = self.convering_unit / 1.609e+6  # mm to mile
        elif self.variable.get() == (self.units[0]) and self.variable2.get() == (self.units2[8]):  # last check for mm
            self.result = self.convering_unit / 1.852e+6  # mm to nm
        elif self.variable.get() == (self.units[1]) and self.variable2.get() == (self.units2[0]):
            self.result = self.convering_unit * 10  # cm to mm
        elif self.variable.get() == (self.units[1]) and self.variable2.get() == (self.units2[2]):
            self.result = self.convering_unit / 100  # cm to m
        elif self.variable.get() == (self.units[1]) and self.variable2.get() == (self.units2[3]):
            self.result = self.convering_unit / 100000  # cm to km
        elif self.variable.get() == (self.units[1]) and self.variable2.get() == (self.units2[4]):
            self.result = self.convering_unit / 2.54  # cm to in
        elif self.variable.get() == (self.units[1]) and self.variable2.get() == (self.units2[5]):
            self.result = self.convering_unit / 30.48  # cm to ft
        elif self.variable.get() == (self.units[1]) and self.variable2.get() == (self.units2[6]):
            self.result = self.convering_unit / 91.44  # cm to yd
        elif self.variable.get() == (self.units[1]) and self.variable2.get() == (self.units2[7]):
            self.result = self.convering_unit / 160934  # cm to mile
        elif self.variable.get() == (self.units[1]) and self.variable2.get() == (self.units2[8]):  # last check for cm
            self.result = self.convering_unit / 185200  # cm to nm
        elif self.variable.get() == (self.units[2]) and self.variable2.get() == (self.units2[0]):
            self.result = self.convering_unit * 1000  # m to mm
        elif self.variable.get() == (self.units[2]) and self.variable2.get() == (self.units2[1]):
            self.result = self.convering_unit * 100  # m to cm
        elif self.variable.get() == (self.units[2]) and self.variable2.get() == (self.units2[4]):
            self.result = self.convering_unit * 39.37  # m to in
        elif self.variable.get() == (self.units[2]) and self.variable2.get() == (self.units2[5]):
            self.result = self.convering_unit * 3.281  # m to ft
        elif self.variable.get() == (self.units[2]) and self.variable2.get() == (self.units2[6]):
            self.result = self.convering_unit * 1.094  # m to yd
        elif self.variable.get() == (self.units[2]) and self.variable2.get() == (self.units2[7]):
            self.result = self.convering_unit / 1609  # m to mile
        elif self.variable.get() == (self.units[2]) and self.variable2.get() == (self.units2[8]):  # last check for m
            self.result = self.convering_unit / 1852  # m to nm
        elif self.variable.get() == (self.units[3]) and self.variable2.get() == (self.units2[0]):
            self.result = self.convering_unit * 1e+6  # km to mm
        elif self.variable.get() == (self.units[3]) and self.variable2.get() == (self.units2[1]):
            self.result = self.convering_unit * 100000  # km to cm
        elif self.variable.get() == (self.units[3]) and self.variable2.get() == (self.units2[2]):
            self.result = self.convering_unit * 1000  # km to m
        elif self.variable.get() == (self.units[3]) and self.variable2.get() == (self.units2[4]):
            self.result = self.convering_unit * 39370  # km to in
        elif self.variable.get() == (self.units[3]) and self.variable2.get() == (self.units2[5]):
            self.result = self.convering_unit * 3281  # km to ft
        elif self.variable.get() == (self.units[3]) and self.variable2.get() == (self.units2[6]):
            self.result = self.convering_unit * 1094  # km to yd
        elif self.variable.get() == (self.units[3]) and self.variable2.get() == (self.units2[7]):
            self.result = self.convering_unit / 1.609  # km to mile
        elif self.variable.get() == (self.units[3]) and self.variable2.get() == (self.units2[8]):  # last check for km
            self.result = self.convering_unit / 1.852  # km to nm
        elif self.variable.get() == (self.units[4]) and self.variable2.get() == (self.units2[0]):
            self.result = self.convering_unit * 25.4  # in to mm
        elif self.variable.get() == (self.units[4]) and self.variable2.get() == (self.units2[1]):
            self.result = self.convering_unit * 2.54  # in to cm
        elif self.variable.get() == (self.units[4]) and self.variable2.get() == (self.units2[2]):
            self.result = self.convering_unit / 39.37  # in to m
        elif self.variable.get() == (self.units[4]) and self.variable2.get() == (self.units2[3]):
            self.result = self.convering_unit / 39370  # in to km
        elif self.variable.get() == (self.units[4]) and self.variable2.get() == (self.units2[5]):
            self.result = self.convering_unit / 12  # in to ft
        elif self.variable.get() == (self.units[4]) and self.variable2.get() == (self.units2[6]):
            self.result = self.convering_unit / 36  # in to yd
        elif self.variable.get() == (self.units[4]) and self.variable2.get() == (self.units2[7]):
            self.result = self.convering_unit / 63360  # in to mile
        elif self.variable.get() == (self.units[4]) and self.variable2.get() == (self.units2[8]):  # last check for in
            self.result = self.convering_unit / 72913  # in to nm
        elif self.variable.get() == (self.units[5]) and self.variable2.get() == (self.units2[0]):
            self.result = self.convering_unit * 305  # ft to mm
        elif self.variable.get() == (self.units[5]) and self.variable2.get() == (self.units2[1]):
            self.result = self.convering_unit * 30.48  # ft to cm
        elif self.variable.get() == (self.units[5]) and self.variable2.get() == (self.units2[2]):
            self.result = self.convering_unit / 3.281  # ft to m
        elif self.variable.get() == (self.units[5]) and self.variable2.get() == (self.units2[3]):
            self.result = self.convering_unit / 3281  # ft to km
        elif self.variable.get() == (self.units[5]) and self.variable2.get() == (self.units2[4]):
            self.result = self.convering_unit * 12  # ft to in
        elif self.variable.get() == (self.units[5]) and self.variable2.get() == (self.units2[6]):
            self.result = self.convering_unit / 3  # ft to yd
        elif self.variable.get() == (self.units[5]) and self.variable2.get() == (self.units2[7]):
            self.result = self.convering_unit / 5280  # ft to mile
        elif self.variable.get() == (self.units[5]) and self.variable2.get() == (self.units2[8]):  # last check for ft
            self.result = self.convering_unit / 6076  # ft to nm
        elif self.variable.get() == (self.units[6]) and self.variable2.get() == (self.units2[0]):
            self.result = self.convering_unit * 914  # yd to mm
        elif self.variable.get() == (self.units[6]) and self.variable2.get() == (self.units2[1]):
            self.result = self.convering_unit * 91.44  # yd to cm
        elif self.variable.get() == (self.units[6]) and self.variable2.get() == (self.units2[2]):
            self.result = self.convering_unit / 1.094  # yd to m
        elif self.variable.get() == (self.units[6]) and self.variable2.get() == (self.units2[3]):
            self.result = self.convering_unit / 1094  # yd to km
        elif self.variable.get() == (self.units[6]) and self.variable2.get() == (self.units2[4]):
            self.result = self.convering_unit * 36  # yd to in
        elif self.variable.get() == (self.units[6]) and self.variable2.get() == (self.units2[5]):
            self.result = self.convering_unit * 3  # yd to ft
        elif self.variable.get() == (self.units[6]) and self.variable2.get() == (self.units2[7]):
            self.result = self.convering_unit / 1760  # yd to mile
        elif self.variable.get() == (self.units[6]) and self.variable2.get() == (self.units2[8]):  # last check for yd
            self.result = self.convering_unit / 2025  # yd to nm
        elif self.variable.get() == (self.units[7]) and self.variable2.get() == (self.units2[0]):
            self.result = self.convering_unit * 1.609e+6  # mile to mm
        elif self.variable.get() == (self.units[7]) and self.variable2.get() == (self.units2[1]):
            self.result = self.convering_unit * 160934  # mile to cm
        elif self.variable.get() == (self.units[7]) and self.variable2.get() == (self.units2[2]):
            self.result = self.convering_unit * 1609  # mile to m
        elif self.variable.get() == (self.units[7]) and self.variable2.get() == (self.units2[3]):
            self.result = self.convering_unit * 1.609  # mile to km
        elif self.variable.get() == (self.units[7]) and self.variable2.get() == (self.units2[4]):
            self.result = self.convering_unit * 63360  # mile to in
        elif self.variable.get() == (self.units[7]) and self.variable2.get() == (self.units2[5]):
            self.result = self.convering_unit * 5280  # mile to ft
        elif self.variable.get() == (self.units[7]) and self.variable2.get() == (self.units2[6]):
            self.result = self.convering_unit * 1760  # mile to yd
        elif self.variable.get() == (self.units[7]) and self.variable2.get() == (self.units2[8]):  # last check for mile
            self.result = self.convering_unit / 1.151  # mile to nm
        elif self.variable.get() == (self.units[8]) and self.variable2.get() == (self.units2[0]):
            self.result = self.convering_unit * 1.852e+6  # nm to mm
        elif self.variable.get() == (self.units[8]) and self.variable2.get() == (self.units2[1]):
            self.result = self.convering_unit * 185200  # nm to cm
        elif self.variable.get() == (self.units[8]) and self.variable2.get() == (self.units2[2]):
            self.result = self.convering_unit * 1852  # nm to m
        elif self.variable.get() == (self.units[8]) and self.variable2.get() == (self.units2[3]):
            self.result = self.convering_unit * 1.852  # nm to km
        elif self.variable.get() == (self.units[8]) and self.variable2.get() == (self.units2[4]):
            self.result = self.convering_unit * 72913  # nm to in
        elif self.variable.get() == (self.units[8]) and self.variable2.get() == (self.units2[5]):
            self.result = self.convering_unit * 6076  # nm to ft
        elif self.variable.get() == (self.units[8]) and self.variable2.get() == (self.units2[6]):
            self.result = self.convering_unit * 2025  # nm to yd
        elif self.variable.get() == (self.units[8]) and self.variable2.get() == (self.units2[7]):  # last check for nm
            self.result = self.convering_unit / 1.151  # nm to mile
        else:
            self.stat = False  # error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(True, False)  # window size cant change
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

    def close_window(self):  # closes window
        self.master.destroy()


# Pythagorean Theorem (done)
class Win4:
    def __init__(self, master, number):  # Pythagorean Theorem
        self.tk = tk
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.number = number
        self.master = master
        self.master.geometry("400x450+200+200")  # window size
        self.master.resizable(False, False)  # window size cant be changed
        self.frame = tk.Frame(self.master)
        self.name = tk.Label(self.frame, text="Pythagorean Theorem")  # name of script
        self.name.pack()
        self.formula = tk.Label(self.frame, text="pythagorean theorem formula: a² + b² = c²",
                                font=("arial", 10))  # how to use
        self.formula.pack()
        self.about = tk.Label(self.frame, text="press clear before running again", font=("arial", 10))  # how to use
        self.about.pack()
        self.square = tk.Checkbutton(self.frame, text='find the square root of c', onvalue=1, offvalue=0,
                                     variable=self.var1)
        self.square.toggle()
        self.square.pack()
        self.find_c = tk.Checkbutton(self.frame, text='find c', onvalue=1, offvalue=0,
                                     variable=self.var2)
        self.find_c.toggle()
        self.find_c.pack()
        self.find_a = tk.Checkbutton(self.frame, text='find a', onvalue=1, offvalue=0,
                                     variable=self.var3)
        self.find_a.pack()
        self.find_b = tk.Checkbutton(self.frame, text='find b', onvalue=1, offvalue=0,
                                     variable=self.var4)
        self.find_b.pack()
        self.label1 = tk.Label(self.frame, text='enter the value of a', font=('arial', 10))
        self.label1.pack()
        self.amount_a = tk.Entry(self.frame, text='unit a', font=('arial', 10))
        self.amount_a.pack()
        self.label2 = tk.Label(self.frame, text='enter the value of b', font=('arial', 10))
        self.label2.pack()
        self.amount_b = tk.Entry(self.frame, text='unit b', font=('arial', 10))
        self.amount_b.pack()
        self.label3 = tk.Label(self.frame, text='enter the value of c', font=('arial', 10))
        self.label3.pack()
        self.amount_c = tk.Entry(self.frame, text='unit c', font=('arial', 10))
        self.amount_c.pack()
        self.solve = tk.Button(self.frame, text='Solve', command=self.maths)
        self.solve.pack()
        self.copyp = tk.Button(self.frame, text=f"Copy Answer", command=self.copy_answer)  # button to copy password
        self.copyp.pack()
        self.clear = tk.Button(self.frame, text=f"Clear", command=self.clear_results)
        self.clear.pack()  # will clear answers(temporary till it does it on its own)
        self.quit = tk.Button(self.frame, text=f"Close", command=self.close_window)  # button to close window
        self.quit.pack()
        self.ans = tk.Label(self.frame, text=f'the answer is', font=('arial', 10))
        self.ans.pack()
        self.frame.pack()

    def maths(self):
        self.stat = True
        self.n1 = self.amount_a.get()
        self.n2 = self.amount_b.get()
        self.n3 = self.amount_c.get()
        if self.amount_a.get() == "" and self.amount_b.get() == "" and (self.var1.get() == 1) and (
                self.var2.get() == 1) and (self.var3.get() == 0) and (
                self.var4.get() == 0) or self.amount_b.get() == "" and (self.var1.get() == 1) and (
                self.var2.get() == 1) and (self.var3.get() == 0) and (
                self.var4.get() == 0) or self.amount_a.get() == "" and (self.var1.get() == 1) and (
                self.var2.get() == 1) and (self.var3.get() == 0) and (
                self.var4.get() == 0):  # find C, A and B are not there
            self.stat = False  # for error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant be changed
            self.error1.title('error 404')  # name of widnow
            self.tk.Label(self.error1, text='error 404 number not found¯\_(ツ)_/¯').pack()  # message
            self.tk.Label(self.error1, text='please enter a number and try again').pack()  # message
            self.error1.after(5000, self.error1.destroy)  # window will close in 5 seconds
        elif self.amount_b.get() == "" and self.amount_c.get() == "" and (self.var1.get() == 0) and (
                self.var2.get() == 0) and (self.var3.get() == 1) and (
                self.var4.get() == 0) or (self.var1.get() == 0) and (self.var2.get() == 0) and (
                self.var3.get() == 1) and (
                self.var4.get() == 0) and self.amount_c.get() == "" or (self.var1.get() == 0) and (
                self.var2.get() == 0) and (self.var3.get() == 1) and (
                self.var4.get() == 0) and self.amount_b.get() == "":  # find A, C and B are not there
            self.stat = False  # for error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant be changed
            self.error1.title('error 404')  # name of widnow
            self.tk.Label(self.error1, text='error 404 number not found¯\_(ツ)_/¯').pack()  # message
            self.tk.Label(self.error1, text='please enter a number and try again').pack()  # message
            self.error1.after(5000, self.error1.destroy)  # window will close in 5 seconds
        elif self.amount_a.get() == "" and self.amount_c.get() == "" and (self.var1.get() == 0) and (
                self.var2.get() == 0) and (self.var3.get() == 1) and (
                self.var4.get() == 0) or (self.var1.get() == 0) and (self.var2.get() == 0) and (
                self.var3.get() == 0) and (
                self.var4.get() == 1) and self.amount_c.get() == "" or (self.var1.get() == 0) and (
                self.var2.get() == 0) and (self.var3.get() == 0) and (
                self.var4.get() == 1) and self.amount_a.get() == "":  # find B, C and A are not there
            self.stat = False  # for error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant be changed
            self.error1.title('error 404')  # name of widnow
            self.tk.Label(self.error1, text='error 404 number not found¯\_(ツ)_/¯').pack()  # message
            self.tk.Label(self.error1, text='please enter a number and try again').pack()  # message
            self.error1.after(5000, self.error1.destroy)  # window will close in 5 seconds
        elif (self.var1.get() == 0) and (self.var2.get() == 0) and (self.var3.get() == 0) and (
                self.var4.get() == 0) or (self.var1.get() == 1) and (self.var2.get() == 1) and (
                self.var3.get() == 1) and (self.var4.get() == 1) or (self.var1.get() == 0) and (
                self.var2.get() == 1) and (self.var3.get() == 1) and (
                self.var4.get() == 1) or (self.var1.get() == 0) and (self.var2.get() == 0) and (
                self.var3.get() == 1) and (
                self.var4.get() == 1) or (self.var1.get() == 1) and (self.var2.get() == 1) and (
                self.var3.get() == 1) and (
                self.var4.get() == 1) or (self.var1.get() == 0) and (self.var2.get() == 1) and (
                self.var3.get() == 1) and (
                self.var4.get() == 1) or (self.var1.get() == 0) and (self.var2.get() == 0) and (
                self.var3.get() == 1) and (
                self.var4.get() == 1) or (self.var1.get() == 1) and (self.var2.get() == 1) and (
                self.var3.get() == 1) and (
                self.var4.get() == 0) or (self.var1.get() == 0) and (self.var2.get() == 1) and (
                self.var3.get() == 1) and (
                self.var4.get() == 0) or (self.var1.get() == 1) and (self.var2.get() == 0) and (
                self.var3.get() == 0) and (
                self.var4.get() == 1):  # selection error
            self.stat = False  # for error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant be changed
            self.error1.title('error 404')  # name of widnow
            self.tk.Label(self.error1, text='error 404 options not found ¯\_(ツ)_/¯').pack()  # message
            self.tk.Label(self.error1, text='please select a valid option').pack()  # message
            self.error1.after(5000, self.error1.destroy)  # window will close in 5 seconds
        elif (self.var1.get() == 1) and (self.var2.get() == 1) and (self.var3.get() == 0) and (
                self.var4.get() == 0):  # find C square root ans
            self.not_square_root = (
                    int(float(self.n1)) * int(float(self.n1)) + (int(float(self.n2)) * int(float(self.n2))))
            self.result = (math.sqrt(float(self.not_square_root)))
        elif (self.var1.get() == 0) and (self.var2.get() == 1) and (self.var3.get() == 0) and (
                self.var4.get() == 0):  # find C no square root
            self.result = (int(float(self.n1)) * int(float(self.n1)) + (int(float(self.n2)) * int(float(self.n2))))
        elif (self.var1.get() == 0) and (self.var2.get() == 0) and (self.var3.get() == 1) and (
                self.var4.get() == 0):  # find A no square root
            self.not_square_root = (
                    int(float(self.n3)) * int(float(self.n3)) - (int(float(self.n2)) * int(float(self.n2))))
            self.result = (math.sqrt(float(self.not_square_root)))
        elif (self.var1.get() == 1) and (self.var2.get() == 0) and (self.var3.get() == 1) and (
                self.var4.get() == 0):  # find A no square root
            self.not_square_root = (
                    int(float(self.n3)) * int(float(self.n3)) - (int(float(self.n2)) * int(float(self.n2))))
            self.result = (math.sqrt(float(self.not_square_root)))
        elif (self.var1.get() == 0) and (self.var2.get() == 0) and (self.var3.get() == 0) and (
                self.var4.get() == 1):  # find B no square root
            self.not_square_root = (
                    int(float(self.n3)) * int(float(self.n3)) - (int(float(self.n1)) * int(float(self.n1))))
            self.result = (math.sqrt(float(self.not_square_root)))
        elif (self.var1.get() == 1) and (self.var2.get() == 0) and (self.var3.get() == 0) and (
                self.var4.get() == 1):  # find B no square root
            self.not_square_root = (
                    int(float(self.n3)) * int(float(self.n3)) - (int(float(self.n1)) * int(float(self.n1))))
            self.result = (math.sqrt(float(self.not_square_root)))
        else:  # error is not pisible in this program but if you mess with it and break something this will tell you
            self.stat = False  # error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant change
            self.error1.title('error 404')  # name of window
            self.tk.Label(self.error1, text='error 404 something went very wrong ¯\_(ツ)_/¯').pack()  # message
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

    def close_window(self):  # closes window
        self.master.destroy()


# About
class WinA:
    def __init__(self, master, number):
        self.number = number
        self.master = master
        self.master.geometry("400x450+200+200")  # window size
        self.master.resizable(False, False)  # window size cant change
        self.frame = tk.Frame(self.master)
        self.name = tk.Label(self.frame, text="About", font=("arial", 10))
        self.name.pack()
        self.line1 = tk.Label(self.frame, text='math tools is an project I have always wanted to make',
                              font=('arial', 10))
        self.line1.pack()
        self.line1 = tk.Label(self.frame,
                              text='its goal is to put all the math tools you could ever need in one place',
                              font=('arial', 10))
        self.line1.pack()
        self.line1 = tk.Label(self.frame, text='you can find the code and past versions of calculators on my github',
                              font=('arial', 10))
        self.line1.pack()
        self.cqb13_github = tk.Button(self.frame, text=f"cqb13 github", command=github)  # button to github
        self.cqb13_github.pack()
        self.quit = tk.Button(self.frame, text=f"Close", command=self.close_window)
        self.quit.pack()
        self.frame.pack()

    def close_window(self):
        self.master.destroy()


window = tk.Tk()
window.title("Math Tools V.3")
window.resizable(False, False)
app = Win1(window)
window.mainloop()