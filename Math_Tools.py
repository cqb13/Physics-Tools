from fractions import Fraction
from random import *
import tkinter as tk
import webbrowser
import pyperclip
import math
import sys


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
        self.butnew("Percent Calculator", "4", Win4)
        self.butnew("Speed Calculations", "5", Win5)
        self.butnew("Velocity Calculations", "6", Win6)
        self.butnew("Pythagorean Theorem", "7", Win7)
        self.butnew("Random Number Generator", "8", Win8)
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
    sys.exit()


# Calculator (done)
class Win2:
    def __init__(self, master, number):  # Calculator
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
            "+",  # 0
            "-",  # 1
            "*",  # 2
            "/",  # 3
            "??",  # 4
            "??",  # 5
            "???",  # 6
            "d to a/b",  # 7
            "a/b to d"  # 8
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
        if self.n1 == '':
            self.stat = False  # error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant change
            self.error1.title('error 404')  # name of window
            self.tk.Label(self.error1, text='error 404 first number not found  ??\_(???)_/??').pack()
            self.tk.Label(self.error1,
                          text='first number is needed for this operation enter first number and try again').pack()
            self.error1.after(5000, self.error1.destroy)  # window will close in 5 seconds
        elif self.n2 == '' and self.variable.get() == (self.operations[0]) or self.n2 == '' and self.variable.get() == (
                self.operations[1]) or self.n2 == '' and self.variable.get() == (
                self.operations[2]) or self.n2 == '' and self.variable.get() == (
                self.operations[3]):
            self.stat = False  # error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant change
            self.error1.title('error 404')  # name of window
            self.tk.Label(self.error1, text='error 404 second number not found  ??\_(???)_/??').pack()
            self.tk.Label(self.error1,
                          text='second number is needed for this operation enter second number and try again').pack()
            self.error1.after(5000, self.error1.destroy)  # window will close in 5 seconds
        else:
            pass

        if self.variable.get() == (self.operations[0]):  # addition
            self.fraction1 = (float(self.n1))
            self.fraction2 = (float(self.n2))
            self.result = self.fraction1 + self.fraction2
        elif self.variable.get() == (self.operations[1]):  # subtraction
            self.fraction1 = (float(self.n1))
            self.fraction2 = (float(self.n2))
            self.result = self.fraction1 - self.fraction2
        elif self.variable.get() == (self.operations[2]):  # multiply
            self.fraction1 = (float(self.n1))
            self.fraction2 = (float(self.n2))
            self.result = self.fraction1 * self.fraction2
        elif self.variable.get() == (self.operations[3]):  # divide
            self.fraction1 = (float(self.n1))
            self.fraction2 = (float(self.n2))
            self.result = self.fraction1 / self.fraction2
        elif self.variable.get() == (self.operations[4]):  # squaring
            self.fraction1 = (float(self.n1))
            self.result = self.fraction1 * self.fraction1
        elif self.variable.get() == (self.operations[5]):  # cubing
            self.fraction1 = (float(self.n1))
            self.result = self.fraction1 * self.fraction1 * self.fraction1
        elif self.variable.get() == (self.operations[7]):  # decimal to fraction
            self.fraction1 = (float(self.n1))
            self.result = (Fraction(str(float(self.n1))))
        elif self.variable.get() == (self.operations[8]):  # fraction to a decimal
            self.fraction1 = (float(self.n1))
            self.result = (str(float(Fraction(self.n1))))
        else:  # this error should not be possible if you get it you did something very wrong
            self.stat = False  # error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant change
            self.error1.title('error 404')  # name of window
            self.tk.Label(self.error1, text='error 404 something went very wrong ??\_(???)_/??').pack()  # message
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
        self.tk.Label(self.help_p, text='window will close in 20 seconds').pack()
        self.tk.Label(self.help_p, text='-- operation key --').pack()
        self.tk.Label(self.help_p, text='use a/b format to use fractions in operations').pack()
        self.tk.Label(self.help_p, text='+ = addition').pack()
        self.tk.Label(self.help_p, text='- = subtraction').pack()
        self.tk.Label(self.help_p, text='* = multiplication').pack()
        self.tk.Label(self.help_p, text='/ = division').pack()
        self.tk.Label(self.help_p, text='?? = squaring a number(only uses first number)').pack()
        self.tk.Label(self.help_p, text='?? = cubing a number(only uses first number )').pack()
        self.tk.Label(self.help_p, text='??? = square root of a number(only uses first number)').pack()
        self.tk.Label(self.help_p, text='d to a/b = decimal to a fraction(only uses first number)').pack()
        self.tk.Label(self.help_p, text='a/b to d = fraction to a decimal(only uses first number)').pack()
        self.help_p.after(10000, self.help_p.destroy)  # window will close in 10 seconds

    def close_window(self):  # closes window
        self.master.destroy()


# Unit Conversion (done)
class Win3:
    def __init__(self, master, number):  # unit conversions
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
        self.help = tk.Button(self.frame, text=f" Help ", command=self.help)  # button to open help window
        self.help.pack()
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
                self.units2[7]) or self.variable.get() == (self.units[8]) and self.variable2.get() == (
                self.units2[8]):  # converting to same unit error
            self.stat = False  # for error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant be changed
            self.error1.title('error 404')  # name of widnow
            self.tk.Label(self.error1, text='error 404 conversion not found ??\_(???)_/??').pack()  # message
            self.tk.Label(self.error1, text='please convert to a different unit').pack()  # message
            self.error1.after(5000, self.error1.destroy)  # window will close in 5 seconds
        elif self.variable.get() == (self.units[0]) and self.variable2.get() == (self.units2[1]):
            self.result = f'{self.convering_unit / 10} cm'  # mm to cm
        elif self.variable.get() == (self.units[0]) and self.variable2.get() == (self.units2[2]):
            self.result = f'{self.convering_unit / 1000} m'  # mm to m
        elif self.variable.get() == (self.units[0]) and self.variable2.get() == (self.units2[3]):
            self.result = f'{self.convering_unit / 1e+6} km'  # mm to km
        elif self.variable.get() == (self.units[0]) and self.variable2.get() == (self.units2[4]):
            self.result = f'{self.convering_unit / 25.4} in'  # mm to in
        elif self.variable.get() == (self.units[0]) and self.variable2.get() == (self.units2[5]):
            self.result = f'{self.convering_unit / 305} ft'  # mm to ft
        elif self.variable.get() == (self.units[0]) and self.variable2.get() == (self.units2[6]):
            self.result = f'{self.convering_unit / 914} yd'  # mm to yd
        elif self.variable.get() == (self.units[0]) and self.variable2.get() == (self.units2[7]):
            self.result = f'{self.convering_unit / 1.609e+6} mi'  # mm to mi
        elif self.variable.get() == (self.units[0]) and self.variable2.get() == (self.units2[8]):  # last check for mm
            self.result = f'{self.convering_unit / 1.852e+6} nm'  # mm to nm
        elif self.variable.get() == (self.units[1]) and self.variable2.get() == (self.units2[0]):
            self.result = f'{self.convering_unit * 10} mm'  # cm to mm
        elif self.variable.get() == (self.units[1]) and self.variable2.get() == (self.units2[2]):
            self.result = f'{self.convering_unit / 100} m'  # cm to m
        elif self.variable.get() == (self.units[1]) and self.variable2.get() == (self.units2[3]):
            self.result = f'{self.convering_unit / 100000} km'  # cm to km
        elif self.variable.get() == (self.units[1]) and self.variable2.get() == (self.units2[4]):
            self.result = f'{self.convering_unit / 2.54} im'  # cm to in
        elif self.variable.get() == (self.units[1]) and self.variable2.get() == (self.units2[5]):
            self.result = f'{self.convering_unit / 30.48} ft'  # cm to ft
        elif self.variable.get() == (self.units[1]) and self.variable2.get() == (self.units2[6]):
            self.result = f'{self.convering_unit / 91.44} yd'  # cm to yd
        elif self.variable.get() == (self.units[1]) and self.variable2.get() == (self.units2[7]):
            self.result = f'{self.convering_unit / 160934} mi'  # cm to mi
        elif self.variable.get() == (self.units[1]) and self.variable2.get() == (self.units2[8]):  # last check for cm
            self.result = f'{self.convering_unit / 185200} nm'  # cm to nm
        elif self.variable.get() == (self.units[2]) and self.variable2.get() == (self.units2[0]):
            self.result = f'{self.convering_unit * 1000} mm'  # m to mm
        elif self.variable.get() == (self.units[2]) and self.variable2.get() == (self.units2[1]):
            self.result = f'{self.convering_unit * 100} cm'  # m to cm
        elif self.variable.get() == (self.units[2]) and self.variable2.get() == (self.units2[3]):
            self.result = f'{self.convering_unit / 1000} km'  # m to km
        elif self.variable.get() == (self.units[2]) and self.variable2.get() == (self.units2[4]):
            self.result = f'{self.convering_unit * 39.37} in'  # m to in
        elif self.variable.get() == (self.units[2]) and self.variable2.get() == (self.units2[5]):
            self.result = f'{self.convering_unit * 3.281} ft'  # m to ft
        elif self.variable.get() == (self.units[2]) and self.variable2.get() == (self.units2[6]):
            self.result = f'{self.convering_unit * 1.094} yd'  # m to yd
        elif self.variable.get() == (self.units[2]) and self.variable2.get() == (self.units2[7]):
            self.result = f'{self.convering_unit / 1609} mi'  # m to mi
        elif self.variable.get() == (self.units[2]) and self.variable2.get() == (self.units2[8]):  # last check for m
            self.result = f'{self.convering_unit / 1852} nm'  # m to nm
        elif self.variable.get() == (self.units[3]) and self.variable2.get() == (self.units2[0]):
            self.result = f'{self.convering_unit * 1e+6} mm'  # km to mm
        elif self.variable.get() == (self.units[3]) and self.variable2.get() == (self.units2[1]):
            self.result = f'{self.convering_unit * 100000} cm'  # km to cm
        elif self.variable.get() == (self.units[3]) and self.variable2.get() == (self.units2[2]):
            self.result = f'{self.convering_unit * 1000} m'  # km to m
        elif self.variable.get() == (self.units[3]) and self.variable2.get() == (self.units2[4]):
            self.result = f'{self.convering_unit * 39370} in'  # km to in
        elif self.variable.get() == (self.units[3]) and self.variable2.get() == (self.units2[5]):
            self.result = f'{self.convering_unit * 3281} ft'  # km to ft
        elif self.variable.get() == (self.units[3]) and self.variable2.get() == (self.units2[6]):
            self.result = f'{self.convering_unit * 1094} yd'  # km to yd
        elif self.variable.get() == (self.units[3]) and self.variable2.get() == (self.units2[7]):
            self.result = f'{self.convering_unit / 1.609} mil'  # km to mi
        elif self.variable.get() == (self.units[3]) and self.variable2.get() == (self.units2[8]):  # last check for km
            self.result = f'{self.convering_unit / 1.852} nm'  # km to nm
        elif self.variable.get() == (self.units[4]) and self.variable2.get() == (self.units2[0]):
            self.result = f'{self.convering_unit * 25.4} mm'  # in to mm
        elif self.variable.get() == (self.units[4]) and self.variable2.get() == (self.units2[1]):
            self.result = f'{self.convering_unit * 2.54} cm'  # in to cm
        elif self.variable.get() == (self.units[4]) and self.variable2.get() == (self.units2[2]):
            self.result = f'{self.convering_unit / 39.37} m'  # in to m
        elif self.variable.get() == (self.units[4]) and self.variable2.get() == (self.units2[3]):
            self.result = f'{self.convering_unit / 39370} km'  # in to km
        elif self.variable.get() == (self.units[4]) and self.variable2.get() == (self.units2[5]):
            self.result = f'{self.convering_unit / 12} ft'  # in to ft
        elif self.variable.get() == (self.units[4]) and self.variable2.get() == (self.units2[6]):
            self.result = f'{self.convering_unit / 36} yd'  # in to yd
        elif self.variable.get() == (self.units[4]) and self.variable2.get() == (self.units2[7]):
            self.result = f'{self.convering_unit / 63360} mi'  # in to mi
        elif self.variable.get() == (self.units[4]) and self.variable2.get() == (self.units2[8]):  # last check for in
            self.result = f'{self.convering_unit / 72913} nm'  # in to nm
        elif self.variable.get() == (self.units[5]) and self.variable2.get() == (self.units2[0]):
            self.result = f'{self.convering_unit * 305} mm'  # ft to mm
        elif self.variable.get() == (self.units[5]) and self.variable2.get() == (self.units2[1]):
            self.result = f'{self.convering_unit * 30.48} cm'  # ft to cm
        elif self.variable.get() == (self.units[5]) and self.variable2.get() == (self.units2[2]):
            self.result = f'{self.convering_unit / 3.281} m'  # ft to m
        elif self.variable.get() == (self.units[5]) and self.variable2.get() == (self.units2[3]):
            self.result = f'{self.convering_unit / 3281} km'  # ft to km
        elif self.variable.get() == (self.units[5]) and self.variable2.get() == (self.units2[4]):
            self.result = f'{self.convering_unit * 12} in'  # ft to in
        elif self.variable.get() == (self.units[5]) and self.variable2.get() == (self.units2[6]):
            self.result = f'{self.convering_unit / 3} yd'  # ft to yd
        elif self.variable.get() == (self.units[5]) and self.variable2.get() == (self.units2[7]):
            self.result = f'{self.convering_unit / 5280} mi'  # ft to mi
        elif self.variable.get() == (self.units[5]) and self.variable2.get() == (self.units2[8]):  # last check for ft
            self.result = f'{self.convering_unit / 6076} nm'  # ft to nm
        elif self.variable.get() == (self.units[6]) and self.variable2.get() == (self.units2[0]):
            self.result = f'{self.convering_unit * 914} mm'  # yd to mm
        elif self.variable.get() == (self.units[6]) and self.variable2.get() == (self.units2[1]):
            self.result = f'{self.convering_unit * 91.44} cm'  # yd to cm
        elif self.variable.get() == (self.units[6]) and self.variable2.get() == (self.units2[2]):
            self.result = f'{self.convering_unit / 1.094} m'  # yd to m
        elif self.variable.get() == (self.units[6]) and self.variable2.get() == (self.units2[3]):
            self.result = f'{self.convering_unit / 1094} km'  # yd to km
        elif self.variable.get() == (self.units[6]) and self.variable2.get() == (self.units2[4]):
            self.result = f'{self.convering_unit * 36} in'  # yd to in
        elif self.variable.get() == (self.units[6]) and self.variable2.get() == (self.units2[5]):
            self.result = f'{self.convering_unit * 3} ft'  # yd to ft
        elif self.variable.get() == (self.units[6]) and self.variable2.get() == (self.units2[7]):
            self.result = f'{self.convering_unit / 1760} mi'  # yd to mi
        elif self.variable.get() == (self.units[6]) and self.variable2.get() == (self.units2[8]):  # last check for yd
            self.result = f'{self.convering_unit / 2025} nm'  # yd to nm
        elif self.variable.get() == (self.units[7]) and self.variable2.get() == (self.units2[0]):
            self.result = f'{self.convering_unit * 1.609e+6} mm'  # mi to mm
        elif self.variable.get() == (self.units[7]) and self.variable2.get() == (self.units2[1]):
            self.result = f'{self.convering_unit * 160934} cm'  # mi to cm
        elif self.variable.get() == (self.units[7]) and self.variable2.get() == (self.units2[2]):
            self.result = f'{self.convering_unit * 1609} m'  # mi to m
        elif self.variable.get() == (self.units[7]) and self.variable2.get() == (self.units2[3]):
            self.result = f'{self.convering_unit * 1.609} km'  # mi to km
        elif self.variable.get() == (self.units[7]) and self.variable2.get() == (self.units2[4]):
            self.result = f'{self.convering_unit * 63360} in'  # mi to in
        elif self.variable.get() == (self.units[7]) and self.variable2.get() == (self.units2[5]):
            self.result = f'{self.convering_unit * 5280} ft'  # mi to ft
        elif self.variable.get() == (self.units[7]) and self.variable2.get() == (self.units2[6]):
            self.result = f'{self.convering_unit * 1760} yd'  # mi to yd
        elif self.variable.get() == (self.units[7]) and self.variable2.get() == (self.units2[8]):  # last check for mi
            self.result = f'{self.convering_unit / 1.151} nm'  # mi to nm
        elif self.variable.get() == (self.units[8]) and self.variable2.get() == (self.units2[0]):
            self.result = f'{self.convering_unit * 1.852e+6} mm'  # nm to mm
        elif self.variable.get() == (self.units[8]) and self.variable2.get() == (self.units2[1]):
            self.result = f'{self.convering_unit * 185200} cm'  # nm to cm
        elif self.variable.get() == (self.units[8]) and self.variable2.get() == (self.units2[2]):
            self.result = f'{self.convering_unit * 1852} m'  # nm to m
        elif self.variable.get() == (self.units[8]) and self.variable2.get() == (self.units2[3]):
            self.result = f'{self.convering_unit * 1.852} km'  # nm to km
        elif self.variable.get() == (self.units[8]) and self.variable2.get() == (self.units2[4]):
            self.result = f'{self.convering_unit * 72913} in'  # nm to in
        elif self.variable.get() == (self.units[8]) and self.variable2.get() == (self.units2[5]):
            self.result = f'{self.convering_unit * 6076} ft'  # nm to ft
        elif self.variable.get() == (self.units[8]) and self.variable2.get() == (self.units2[6]):
            self.result = f'{self.convering_unit * 2025} yd'  # nm to yd
        elif self.variable.get() == (self.units[8]) and self.variable2.get() == (self.units2[7]):  # last check for nm
            self.result = f'{self.convering_unit / 1.151} mi'  # nm to mi
        else:
            self.stat = False  # error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(True, False)  # window size cant change
            self.error1.title('error 404')  # name of window
            self.tk.Label(self.error1, text='error 404 operation not found ??\_(???)_/??').pack()  # message
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
        self.tk.Label(self.help_p, text='window will close in 20 seconds').pack()
        self.tk.Label(self.help_p, text='-- unit key --').pack()
        self.tk.Label(self.help_p, text='millimeters = mm').pack()
        self.tk.Label(self.help_p, text='centimeter = cm').pack()
        self.tk.Label(self.help_p, text='meter = m').pack()
        self.tk.Label(self.help_p, text='kilometer = km').pack()
        self.tk.Label(self.help_p, text='inch = in').pack()
        self.tk.Label(self.help_p, text='foot = ft').pack()
        self.tk.Label(self.help_p, text='yard = yd').pack()
        self.tk.Label(self.help_p, text='mile = mi').pack()
        self.tk.Label(self.help_p, text='nautical mile = nm').pack()
        self.help_p.after(10000, self.help_p.destroy)  # window will close in 10 seconds

    def close_window(self):  # closes window
        self.master.destroy()


# Percent Calculator (done)
class Win4:
    def __init__(self, master, number):  # does math related to percents
        self.tk = tk
        self.number = number
        self.master = master
        self.var = tk.DoubleVar()
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.master.geometry("400x450+200+200")  # window size
        self.master.resizable(False, False)  # window size cant change
        self.frame = tk.Frame(self.master)
        self.name = tk.Label(self.frame, text="Percent Calculator")
        self.name.pack()
        self.about = tk.Label(self.frame, text="does math realted to percents", font=("arial", 10))
        self.about.pack()
        self.about2 = tk.Label(self.frame, text="press clear before running again", font=("arial", 10))
        self.about2.pack()
        self.num1e = tk.Label(self.frame, text="enter first number")  # label for text box
        self.num1e.pack()
        self.num1 = tk.Entry(self.frame, text="num1", font=("arial", 10))  # text box
        self.num1.pack()
        self.op_pic = tk.Label(self.frame, text="pick an operation")  # label for menu
        self.op_pic.pack()
        self.operations = [  # drop down menu with the operations
            'percent change',  # 0
            'tax',  # 1
            'discount',  # 2
            '% to n',  # 3
            'n to %'  # 4
        ]
        self.variable = tk.StringVar(master)
        self.variable.set(self.operations[0])  # defualt option
        self.menu = tk.OptionMenu(self.frame, self.variable, *self.operations)  # where to put the menu
        self.menu.pack()
        self.num2e = tk.Label(self.frame, text="enter second number")  # label for text box
        self.num2e.pack()
        self.num2 = tk.Entry(self.frame, text="num2", font=("arial", 10))  # where to put second number
        self.num2.pack()
        self.gen = tk.Button(self.frame, text=f"Solve", command=self.maths)
        self.gen.pack()
        self.copyp = tk.Button(self.frame, text=f"Copy Password", command=self.copy_password)
        self.copyp.pack()
        self.clear = tk.Button(self.frame, text=f"Clear", command=self.clear_password)
        self.clear.pack()
        self.quit = tk.Button(self.frame, text=f"Close", command=self.close_window)
        self.quit.pack()
        self.help = tk.Button(self.frame, text=f" Help ", command=self.help)  # button to open help window
        self.help.pack()
        self.answer_name = tk.Label(self.frame, text="the answer is")  # label for answer area
        self.answer_name.pack()
        self.frame.pack()

    def maths(self):
        self.stat = True
        self.n1 = self.num1.get()
        self.n2 = self.num2.get()
        if self.n1 == '':
            self.stat = False  # error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant change
            self.error1.title('error 404')  # name of window
            self.tk.Label(self.error1, text='error 404 first number not found  ??\_(???)_/??').pack()
            self.tk.Label(self.error1,
                          text='first number is needed for this operation enter first number and try again').pack()
            self.error1.after(5000, self.error1.destroy)  # window will close in 5 seconds
        elif self.n2 == '' and self.variable.get() == (self.operations[0]) or self.n2 == '' and self.variable.get() == (
                self.operations[1]) or self.n2 == '' and self.variable.get() == (self.operations[2]):
            self.stat = False  # error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant change
            self.error1.title('error 404')  # name of window
            self.tk.Label(self.error1, text='error 404 second number not found  ??\_(???)_/??').pack()
            self.tk.Label(self.error1,
                          text='second number is needed for this operation enter second number and try again').pack()
            self.error1.after(5000, self.error1.destroy)  # window will close in 5 seconds
        else:
            pass

        if self.variable.get() == (self.operations[0]):  # percent change
            self.num_m_1 = float(self.n1)
            self.num_m_2 = float(self.n2)
            self.temp = self.num_m_1 - self.num_m_2
            self.temp_2 = self.temp / self.num_m_2
            self.result = f'{self.temp_2 * 100}%'
        elif self.variable.get() == (self.operations[1]):  # tax
            self.num_m_1 = float(self.n1)
            self.num_m_2 = float(self.n2)
            self.temp = self.num_m_2 / 100
            self.temp_2 = self.num_m_1 * self.temp
            self.result = f'{self.num_m_1 + self.temp_2}%'
        elif self.variable.get() == (self.operations[2]):  # discount
            self.num_m_1 = float(self.n1)
            self.num_m_2 = float(self.n2)
            self.temp = self.num_m_2 / 100
            self.temp_2 = self.num_m_1 * self.temp
            self.result = f'{self.num_m_1 - self.temp_2}%'
        else:
            self.num_m_1 = float(self.n1)

        if self.variable.get() == (self.operations[3]):
            self.result = self.num_m_1 * 100
        elif self.variable.get() == (self.operations[4]):
            self.result = f'{self.num_m_1 / 100}%'
        else:
            pass

        if not self.stat:
            print('')
        else:
            self.results = tk.Label(self.frame, text=self.result)  # result show
            self.results.pack()

    def copy_password(self):
        pyperclip.copy(self.result)

    def clear_password(self):
        self.results.destroy()

    def help(self):  # help window
        self.help_p = tk.Toplevel(window)
        self.help_p.resizable(False, False)  # window size cant change
        self.help_p.title('help')  # name of window
        self.tk.Label(self.help_p, text='window will close in 20 seconds').pack()
        self.tk.Label(self.help_p, text='-- increasing/decreasing help --').pack()
        self.tk.Label(self.help_p, text='first number should be original value').pack()
        self.tk.Label(self.help_p, text='second number should be new value').pack()
        self.tk.Label(self.help_p, text='if the answer is negative it is a percent decrease').pack()
        self.tk.Label(self.help_p, text='-- tax/discount help --').pack()
        self.tk.Label(self.help_p, text='first number should be price').pack()
        self.tk.Label(self.help_p, text='second number should be tax/discount').pack()
        self.tk.Label(self.help_p, text='-- % to n/n to % --').pack()
        self.tk.Label(self.help_p, text='only use first numer entry').pack()
        self.tk.Label(self.help_p, text='% to n percent is in first number').pack()
        self.tk.Label(self.help_p, text='n to % number is in first number').pack()
        self.help_p.after(10000, self.help_p.destroy)  # window will close in 10 seconds

    def close_window(self):
        self.master.destroy()


# Speed Calculations (done)
class Win5:
    def __init__(self, master, number):  # Speed Calculations
        self.tk = tk
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.number = number
        self.master = master
        self.master.geometry("400x450+200+200")  # window size
        self.master.resizable(False, False)  # window size cant be changed
        self.frame = tk.Frame(self.master)
        self.name = tk.Label(self.frame, text="Speed Calculations")  # name of script
        self.name.pack()
        self.formula = tk.Label(self.frame, text="formula for speed is s=d/t",
                                font=("arial", 10))  # how to use
        self.formula.pack()
        self.var_stand_for = tk.Label(self.frame, text="s(speed) d(distance) t(time)",
                                      font=("arial", 10))  # what the vars mean
        self.var_stand_for.pack()
        self.about = tk.Label(self.frame, text="press clear before running again", font=("arial", 10))  # how to use
        self.about.pack()
        self.find_c = tk.Checkbutton(self.frame, text='find s', onvalue=1, offvalue=0,
                                     variable=self.var1)
        self.find_c.toggle()
        self.find_c.pack()
        self.find_a = tk.Checkbutton(self.frame, text='find d', onvalue=1, offvalue=0,
                                     variable=self.var2)
        self.find_a.pack()
        self.find_b = tk.Checkbutton(self.frame, text='find t', onvalue=1, offvalue=0,
                                     variable=self.var3)
        self.find_b.pack()
        self.label1 = tk.Label(self.frame, text='enter the value of d', font=('arial', 10))
        self.label1.pack()
        self.amount_a = tk.Entry(self.frame, text='unit s', font=('arial', 10))
        self.amount_a.pack()
        self.label2 = tk.Label(self.frame, text='enter the value of t', font=('arial', 10))
        self.label2.pack()
        self.amount_b = tk.Entry(self.frame, text='unit d', font=('arial', 10))
        self.amount_b.pack()
        self.label3 = tk.Label(self.frame, text='enter the value of s', font=('arial', 10))
        self.label3.pack()
        self.amount_c = tk.Entry(self.frame, text='unit t', font=('arial', 10))
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
        if self.var1.get() == 1 and self.n1 == "" and self.n2 == "" or self.var1.get() == 1 and self.n1 == "" or self.var1.get() == 1 and self.n2 == "" \
                or self.var2.get() == 1 and self.n2 == "" and self.n3 == "" or self.var2.get() == 1 and self.n2 == "" or self.var2.get() == 1 and self.n3 == "" \
                or self.var3.get() == 1 and self.n1 == "" and self.n3 == "" or self.var3.get() == 1 and self.n1 == "" or self.var3.get() == 1 and self.n3 == "":  # numbers not found in operations that need them
            self.stat = False  # for error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant be changed
            self.error1.title('error 404')  # name of widnow
            self.tk.Label(self.error1, text='error 404 number not found ??\_(???)_/??').pack()  # message
            self.tk.Label(self.error1, text='please enter required numbers and try again').pack()  # message
            self.error1.after(5000, self.error1.destroy)  # window will close in 5 seconds
        elif self.var1.get() == 1 and self.var2.get() == 1 and self.var3.get() == 1 or self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 \
                or self.var1.get() == 0 and self.var2.get() == 1 and self.var3.get() == 1 \
                or self.var1.get() == 1 and self.var2.get() == 0 and self.var3.get() == 1 \
                or self.var1.get() == 1 and self.var2.get() == 1 and self.var3.get() == 0:  # invalid operation combination
            self.stat = False  # for error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant be changed
            self.error1.title('error 404')  # name of widnow
            self.tk.Label(self.error1, text='error 404 operation not compatable ??\_(???)_/??').pack()  # message
            self.tk.Label(self.error1,
                          text='please enter a valid operation combination and try again').pack()  # message
            self.error1.after(5000, self.error1.destroy)  # window will close in 5 seconds
        elif self.var1.get() == 1 and self.var2.get() == 0 and self.var3.get() == 0:  # find speed
            self.result = int(float(self.n1)) / int(float(self.n2))
        elif self.var1.get() == 0 and self.var2.get() == 1 and self.var3.get() == 0:  # find distance
            self.result = int(float(self.n3)) * int(float(self.n2))
        elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 1:  # find time
            self.result = int(float(self.n3)) * int(float(self.n1))
        else:  # this error should not be possible if you get it you did something very wrong
            self.stat = False  # error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant change
            self.error1.title('error 404')  # name of window
            self.tk.Label(self.error1, text='error 404 something went very wrong ??\_(???)_/??').pack()  # message
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


# Velocity Calculations (done)
class Win6:
    def __init__(self, master, number):  # Velocity Calculations
        self.tk = tk
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.number = number
        self.master = master
        self.master.geometry("400x450+200+200")  # window size
        self.master.resizable(False, False)  # window size cant be changed
        self.frame = tk.Frame(self.master)
        self.name = tk.Label(self.frame, text="Velocity Calculations")  # name of script
        self.name.pack()
        self.formula = tk.Label(self.frame, text="formula for velocity is v=???x/???t",
                                font=("arial", 10))  # how to use
        self.formula.pack()
        self.var_stand_for = tk.Label(self.frame, text="v(velocity) ???x(displacement) ???t(time)",
                                      font=("arial", 10))  # what the vars mean
        self.var_stand_for.pack()
        self.about = tk.Label(self.frame, text="press clear before running again", font=("arial", 10))  # how to use
        self.about.pack()
        self.find_c = tk.Checkbutton(self.frame, text='find s', onvalue=1, offvalue=0,
                                     variable=self.var1)
        self.find_c.toggle()
        self.find_c.pack()
        self.find_a = tk.Checkbutton(self.frame, text='find ???x', onvalue=1, offvalue=0,
                                     variable=self.var2)
        self.find_a.pack()
        self.find_b = tk.Checkbutton(self.frame, text='find ???t', onvalue=1, offvalue=0,
                                     variable=self.var3)
        self.find_b.pack()
        self.label1 = tk.Label(self.frame, text='enter the value of d', font=('arial', 10))
        self.label1.pack()
        self.amount_a = tk.Entry(self.frame, text='unit v', font=('arial', 10))
        self.amount_a.pack()
        self.label2 = tk.Label(self.frame, text='enter the value of t', font=('arial', 10))
        self.label2.pack()
        self.amount_b = tk.Entry(self.frame, text='unit ???x', font=('arial', 10))
        self.amount_b.pack()
        self.label3 = tk.Label(self.frame, text='enter the value of s', font=('arial', 10))
        self.label3.pack()
        self.amount_c = tk.Entry(self.frame, text='unit ???t', font=('arial', 10))
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
        if self.var1.get() == 1 and self.n1 == "" and self.n2 == "" or self.var1.get() == 1 and self.n1 == "" or self.var1.get() == 1 and self.n2 == "" \
                or self.var2.get() == 1 and self.n2 == "" and self.n3 == "" or self.var2.get() == 1 and self.n2 == "" or self.var2.get() == 1 and self.n3 == "" \
                or self.var3.get() == 1 and self.n1 == "" and self.n3 == "" or self.var3.get() == 1 and self.n1 == "" or self.var3.get() == 1 and self.n3 == "":  # numbers not found in operations that need them
            self.stat = False  # for error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant be changed
            self.error1.title('error 404')  # name of widnow
            self.tk.Label(self.error1, text='error 404 number not found ??\_(???)_/??').pack()  # message
            self.tk.Label(self.error1, text='please enter required numbers and try again').pack()  # message
            self.error1.after(5000, self.error1.destroy)  # window will close in 5 seconds
        elif self.var1.get() == 1 and self.var2.get() == 1 and self.var3.get() == 1 or self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 \
                or self.var1.get() == 0 and self.var2.get() == 1 and self.var3.get() == 1 \
                or self.var1.get() == 1 and self.var2.get() == 0 and self.var3.get() == 1 \
                or self.var1.get() == 1 and self.var2.get() == 1 and self.var3.get() == 0:  # invalid operation combination
            self.stat = False  # for error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant be changed
            self.error1.title('error 404')  # name of widnow
            self.tk.Label(self.error1, text='error 404 operation not compatable ??\_(???)_/??').pack()  # message
            self.tk.Label(self.error1,
                          text='please enter a valid operation combination and try again').pack()  # message
            self.error1.after(5000, self.error1.destroy)  # window will close in 5 seconds
        elif self.var1.get() == 1 and self.var2.get() == 0 and self.var3.get() == 0:  # find velocity
            self.result = int(float(self.n1)) / int(float(self.n2))
        elif self.var1.get() == 0 and self.var2.get() == 1 and self.var3.get() == 0:  # find displacement
            self.result = int(float(self.n3)) * int(float(self.n2))
        elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 1:  # find time
            self.result = int(float(self.n3)) * int(float(self.n1))
        else:  # this error should not be possible if you get it you did something very wrong
            self.stat = False  # error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant change
            self.error1.title('error 404')  # name of window
            self.tk.Label(self.error1, text='error 404 something went very wrong ??\_(???)_/??').pack()  # message
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
class Win7:
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
        self.formula = tk.Label(self.frame, text="pythagorean theorem formula: a?? + b?? = c??",
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
            self.tk.Label(self.error1, text='error 404 number not found??\_(???)_/??').pack()  # message
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
            self.tk.Label(self.error1, text='error 404 number not found??\_(???)_/??').pack()  # message
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
            self.tk.Label(self.error1, text='error 404 number not found??\_(???)_/??').pack()  # message
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
            self.tk.Label(self.error1, text='error 404 operation not compatable ??\_(???)_/??').pack()  # message
            self.tk.Label(self.error1,
                          text='please entera  valid operation combination and try again').pack()  # message
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
            self.tk.Label(self.error1, text='error 404 something went very wrong ??\_(???)_/??').pack()  # message
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


# Random Number Generator (done)
class Win8:
    def __init__(self, master, number):  # generates a random password
        self.tk = tk
        self.number = number
        self.master = master
        self.random = random
        self.var = tk.DoubleVar()
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.master.geometry("400x450+200+200")  # window size
        self.master.resizable(False, False)  # window size cant change
        self.frame = tk.Frame(self.master)
        self.name = tk.Label(self.frame, text="Random Number Generator")
        self.name.pack()
        self.about = tk.Label(self.frame, text="generates a random number", font=("arial", 10))
        self.about.pack()
        self.about2 = tk.Label(self.frame, text="press clear before running again", font=("arial", 10))
        self.about2.pack()
        self.about_s = tk.Label(self.frame, text="pick the length of the number",
                                font=("arial", 10))  # label for scale
        self.about_s.pack()
        self.Slider = tk.Scale(self.frame, orient=tk.HORIZONTAL, length=32 * 10, from_=0, to=32,
                               variable=self.var)  # scale
        self.Slider.pack()
        self.pos_neg = tk.Checkbutton(self.frame, text='number will be positive or negative', onvalue=1, offvalue=0,
                                      variable=self.var1)
        self.pos_neg.toggle()  # on when load
        self.pos_neg.pack()
        self.pos = tk.Checkbutton(self.frame, text='number will be positive', onvalue=1, offvalue=0,
                                  variable=self.var2)
        self.pos.pack()
        self.neg = tk.Checkbutton(self.frame, text='number will be negative', onvalue=1, offvalue=0,
                                  variable=self.var3)
        self.neg.pack()
        self.gen = tk.Button(self.frame, text=f"Generate", command=self.number_gen)
        self.gen.pack()
        self.copyp = tk.Button(self.frame, text=f"Copy Password", command=self.copy_password)
        self.copyp.pack()
        self.clear = tk.Button(self.frame, text=f"Clear", command=self.clear_password)
        self.clear.pack()
        self.quit = tk.Button(self.frame, text=f"Close", command=self.close_window)
        self.quit.pack()
        self.answer_name = tk.Label(self.frame, text="the number is")  # label for answer area
        self.answer_name.pack()
        self.frame.pack()

    def number_gen(self):
        self.stat = True
        self.digits = "1234567890"  # list of numbers
        self.ints_pos_neg = "12"  # 1 is ppos 2 is neg
        self.val = "1"
        if int(self.var.get()) == 0:  # no number length
            self.stat = False  # error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant change
            self.error1.title('error 404')  # name of window
            self.tk.Label(self.error1, text='error 404 paramater not found ??\_(???)_/??').pack()
            self.tk.Label(self.error1, text='please select a length longer than 0 for your number and try again').pack()
            self.error1.after(5000, self.error1.destroy)
        elif (self.var1.get() == 1) and (self.var2.get() == 1) and (self.var3.get() == 1) or (
                self.var1.get() == 0) and (self.var2.get() == 1) and (self.var3.get() == 1) or (
                self.var1.get() == 0) and (self.var2.get() == 0) and (self.var3.get() == 0) or (
                self.var1.get() == 1) and (self.var2.get() == 1) and (self.var3.get() == 0) or (
                self.var1.get() == 1) and (self.var2.get() == 0) and (self.var3.get() == 1):
            self.stat = False  # error not show
            self.error1 = tk.Toplevel(window)
            self.error1.resizable(False, False)  # window size cant change
            self.error1.title('error 404')  # name of window
            self.tk.Label(self.error1, text='error 404 paramater not found ??\_(???)_/??').pack()
            self.tk.Label(self.error1, text='please enter a valid paramater combination and try again').pack()
            self.error1.after(5000, self.error1.destroy)
        elif (self.var1.get() == 1) and (self.var2.get() == 0) and (self.var3.get() == 0):
            characters = self.digits
            number = "".join(choice(characters) for _ in range(int(self.var.get())))
            self.result_pos_neg = number
        elif (self.var1.get() == 0) and (self.var2.get() == 1) and (self.var3.get() == 0):
            characters = self.digits
            number = "".join(choice(characters) for _ in range(int(self.var.get())))
            self.result = number
        elif (self.var1.get() == 0) and (self.var2.get() == 0) and (self.var3.get() == 1):
            characters = self.digits
            number = "".join(choice(characters) for _ in range(int(self.var.get())))
            self.result = f'-{number}'
        else:
            self.stat = False  # error not show
            self.error2 = tk.Toplevel(window)
            self.error2.resizable(False, False)  # window size cant change
            self.error2.title('error 404')  # name of window
            self.tk.Label(self.error2, text='error 404 paramater not found ??\_(???)_/??').pack()
            self.tk.Label(self.error2, text='please select at least one option and try again').pack()
            self.error2.after(5000, self.error2.destroy)  # window closes in 5 seconds

        chance = self.ints_pos_neg
        yes_or_no = "".join(choice(chance) for _ in range(int(self.val)))

        if not self.stat:
            print('')  # error no show
        elif (self.var1.get() == 1) and (self.var2.get() == 0) and (self.var3.get() == 0) and yes_or_no == "1":  # makes pos
            self.result = self.result_pos_neg
            self.results = tk.Label(self.frame, text=self.result)
            self.results.pack()
        elif (self.var1.get() == 1) and (self.var2.get() == 0) and (self.var3.get() == 0) and yes_or_no == "2":  # makes neg
            self.result = f'-{self.result_pos_neg}'
            self.results = tk.Label(self.frame, text=self.result)
            self.results.pack()
        else:
            self.results = tk.Label(self.frame, text=self.result)  # result show
            self.results.pack()

    def copy_password(self):
        pyperclip.copy(self.result)

    def clear_password(self):
        self.results.destroy()

    def close_window(self):
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
        self.line1 = tk.Label(self.frame, text='you can find the code and past versions of math tools on my github',
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
window.title("Math Tools V.7")
window.resizable(False, False)
app = Win1(window)
window.mainloop()
