# -*- coding: utf-8 -*-
"""
Revised on Sat Mar 31 14:30:23 2018
@author: Dirk

Calculates the area under the Gaussian bell curve between
the upper and lower limit (defining the interval). Uses the
cumulative distribution function phi(x) to calculate values.

INPUT: 
    left entry field takes the lower limit (set to -infinity if left empty)
    right entry field takes the upper limit (set to +infinity if left empty)
    
OUTPUT:
    probability that an individual of a population resides in the
    interval defined by the lower and upper limit
"""

import math
import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.header = LabelHeader(self)
        self.photo = LabelPhotoField(self)      
        self.intro = LabelIntroField(self)
        self.low = EntryFieldLowerLimit(self)
        self.up = EntryFieldUpperLimit(self)
        CheckButtonField(self)
        self.lab = LabelField(self, self.low, self.up) 
        ButtonField(self, self.low, self.up, self.lab)

class LabelHeader(tk.Frame):
    def __init__(self, parent):
        self.parent = parent        
        self.toplabel = tk.Label(root, text='Gaussian Normal Distribution', \
                                 font=(None, 14))
        self.toplabel.grid(row=0, column=0, columnspan = 2)
        
class LabelPhotoField(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.bild = tk.PhotoImage(file='gauss.gif')
        self.photoLabel = tk.Label(root, image=self.bild)
        self.photoLabel .grid(row=1, column=0, columnspan = 2)
      
class LabelIntroField(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        str = 'Calculate probability from lower and upper limit '
        str = str + '\nwithin Normal Distribution\n\n'
        str = str + 'Left limit              Right limit\n' 
        str = str + 'Leave empty if -\u221E        '
        str = str + '      Leave empty if +\u221E'
        self.label = tk.Label(root, text = str)
        self.label.grid(row=2, column=0, columnspan = 2)
                                 
class EntryFieldLowerLimit(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.entrylow = tk.StringVar()
        self.entrylow = tk.Entry(root, textvariable = self.entrylow)
        self.entrylow.grid(row=3, column=0)
        
class EntryFieldUpperLimit(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.entryhigh = tk.StringVar()
        self.entryhigh = tk.Entry(root, textvariable = self.entryhigh)
        self.entryhigh.grid(row=3, column=1)

class ButtonField(tk.Frame):
    def __init__(self, parent, fromEntryLow, fromEntryHigh, fromLabelField):
        self.parent = parent
        self.fromEntryLow = fromEntryLow
        self.fromEntryLow = fromEntryHigh
        self.fromLabelField = fromLabelField
        self.button = tk.Button(root, text = '        OK        ',
                      command = self.fromLabelField.extract)
        self.button.grid(row=4, column=1)
        self.cancelButton = tk.Button(root, text='Cancel', \
            width=10, command=root.destroy)
        self.cancelButton.grid(row=4, column=0)
        
class LabelField(tk.Frame):
    def __init__(self, parent, fromEntryLow, fromEntryHigh):
        self.parent = parent
        self.fromEntryLow = fromEntryLow
        self.fromEntryHigh = fromEntryHigh
        self.label = tk.Label(root, text = '', font=(None, 12), pady = 5)
        self.label.grid(row=5, column=0, columnspan = 2)
        
    def extract(self): 
        lower = self.fromEntryLow.entrylow.get()
        upper = self.fromEntryHigh.entryhigh.get()
        try:
            reslow = float(lower)
        except ValueError:
            self.label.config(text = 'Field 1 is not a number, try again')          
        try:
            resup = float(upper)
        except ValueError:
            self.label.config(text = 'Field 2 is not a number, try again')
        
        # Case: lower limit = -infinity and upper limit is number
        if lower is '' and upper is not '':
            res = LabelField.phi(-resup)
            result = 1.0 - res
            
        # Case: lower limit is number and upper limit = +infinity
        elif lower is not '' and upper is '':
            res = LabelField.phi(reslow)
            result = 1.0 - res
            
        # Case: lower and upper limit are numbers given by the user
        elif lower is not '' and upper is not '':
            result = LabelField.phi(resup) - LabelField.phi(reslow)
        
        # Case: lower limit = -infinity and upper limit = +infinity
        else:
            result = 1.0
    
        self.label.config(text = 'Gaussian probability: '+ \
                          str(round(result, 4)))

    def phi(x):
        ''' Calculates a value from the cumulative distribution function.
            Taken from John D. Cook
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


