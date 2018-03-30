# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 10:15:23 2018
@author: Dirk

Calculates the area under the Gaussian bell curve between
the upper and lower limit (defining the intervale).

INPUT: 
    left entry field takes the lower limit (set to -infinity if left empty)
    right entry field takes the upper limit (set to +infinity if left empty)
    
OUTPUT:
    probability that an individual of a population resides in the
    interval defined by the lower and upper limit
"""

import tkinter as tk
import math

class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        LabelIntroField(root)
        low = EntryFieldLowerLimit(root)
        up = EntryFieldUpperLimit(root)
        lab = LabelField(root, low, up) 
        ButtonField(root, low, up, lab) 
        
class LabelIntroField():
    def __init__(self, parent):
        self.parent = parent
        str = 'Calculate probability from lower and upper limit '
        str = str + '\nwithin Normal Distribution\n'
        str = str + 'Leave field empty if -infinity or +infinity'
        self.label = tk.Label(None, text = str)
        self.label.grid(row=0, column=0, columnspan = 2)
                                 
class EntryFieldLowerLimit():
    def __init__(self, parent):
        self.parent = parent
        self.entrylow = tk.StringVar()
        self.entrylow = tk.Entry(None, textvariable = self.entrylow) 
        self.entrylow.grid(row=1, column=0)
        
class EntryFieldUpperLimit():
    def __init__(self, parent):
        self.parent = parent
        self.entryhigh = tk.StringVar()
        self.entryhigh = tk.Entry(None, textvariable = self.entryhigh)
        self.entryhigh.grid(row=1, column=1)

class ButtonField():
    def __init__(self, parent, fromEntryLow, fromEntryHigh, fromLabelField):
        self.parent = parent
        self.fromEntryLow = fromEntryLow
        self.fromEntryLow = fromEntryHigh
        self.fromLabelField = fromLabelField
        self.button = tk.Button(None, text = '    OK    ',
                      command = self.fromLabelField.extract)
        self.button.grid(row=2, column=0, columnspan = 2)

class LabelField():
    def __init__(self, parent, fromEntryLow, fromEntryHigh):
        self.parent = parent
        self.fromEntryLow = fromEntryLow
        self.fromEntryHigh = fromEntryHigh
        self.label = tk.Label(None, text = '')
        self.label.grid(row=3, column=0, columnspan = 2)
        
    def extract(self): 
        temp1 = self.fromEntryLow.entrylow.get()
        temp2 = self.fromEntryHigh.entryhigh.get()
        if temp1 is '' and temp2 is not '':
            try:
                res = LabelField.phi(-float(temp2))
            except ValueError:
                self.label.config(text = 'Field 2 is not a number, try again')
            result = 1.0 - res
        elif temp1 is not '' and temp2 is '':
            try:
                res = LabelField.phi(float(temp1))
            except ValueError:
                self.label.config(text = 'Field 1 is not a number, try again')
            result = 1.0 - res
        elif temp1 is not '' and temp2 is not '':
            try:
                res1 = LabelField.phi(float(temp1))
                res2 = LabelField.phi(float(temp2))
            except ValueError:
                self.label.config(text = \
                                  'Field 1 or 2 is not a number, try again')
            result = res2 - res1
        else:
            result = 1.0
        self.label.config(text = 'Gaussian probability: '+ \
                          str(round(result, 4)))

    def phi(x):
        ''' Taken from John D. Cook
            https://www.johndcook.com/blog/python_phi/'''
        # constants:
        a1 =  0.254829592
        a2 = -0.284496736
        a3 =  1.421413741
        a4 = -1.453152027
        a5 =  1.061405429
        p  =  0.3275911
    
        # Save the sign of x
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)/math.sqrt(2.0)
    
        # A&S formula 7.1.26
        t = 1.0/(1.0 + p*x)
        y = 1.0 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t*math.exp(-x*x)
    
        return 0.5*(1.0 + sign*y)
        
if __name__ == '__main__':
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()


