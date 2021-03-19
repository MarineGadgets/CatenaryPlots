#!/usr/bin/env python3

# Catenary line plot controller

import tkinter as tk
from view import View
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from model import calculate


class Controller():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Catenary Calculator")
        self.view = View(self.root, self)
        self.root.geometry('800x600')
        self.root.mainloop()

    def update(self, dic, replot=False):
        self.view.viewPanel.canvas.get_tk_widget().destroy()
        if(replot):
            self.view.viewPanel.fig, self.view.viewPanel.ax = plt.subplots()
        (x,y) = calculate(dic['p'], float(dic['t0']), float(dic['h']), float(dic['dia']), float(dic['r']))
        # self.view.viewPanel.fig.add_subplot(111).plot(x, list(y))
        lines = self.view.viewPanel.ax.plot(x, list(y))
        self.view.viewPanel.ax.legend(range(1,100))

        self.view.viewPanel.canvas.draw()
        self.view.viewPanel.canvas = FigureCanvasTkAgg(self.view.viewPanel.fig, self.root)
        self.view.viewPanel.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


    # def replot(self, dic):
    #     self.view.viewPanel.canvas.get_tk_widget().destroy()
    #     self.view.viewPanel.fig = Figure(figsize=(5, 4), dpi=100)
    #     (x,y) = calculate(dic['p'], float(dic['t0']), float(dic['h']), float(dic['dia']), float(dic['r']))
    #     self.view.viewPanel.fig.add_subplot(111).plot(x, list(y))
    #     self.view.viewPanel.canvas.draw()
    #     self.view.viewPanel.canvas = FigureCanvasTkAgg(self.view.viewPanel.fig, self.root)
    #     self.view.viewPanel.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


