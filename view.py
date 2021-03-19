#!/usr/bin/env python3

# Catenary line plot view

import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

class View():
    def __init__(self, master, controller):
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.viewPanel = ViewPanel(master, controller)


class ViewPanel():
    def __init__(self, root, controller):
        self.controller = controller

        P_OPTIONS = [
            "Studless",
            "Stud"    ,
            "Wire"    ,
            "Polyester"
        ]

        def entry_update(*args):
            t0 = t0_entry.get()
            p = p_type.get()
            h = h_entry.get()
            d = dia_entry.get()
            r = radius_entry.get()
            controller.update({'p': p, 't0': t0, 'h': h, 'dia': d, 'r': r})

        def replot_update(*args):
            t0 = t0_entry.get()
            p = p_type.get()
            h = h_entry.get()
            d = dia_entry.get()
            r = radius_entry.get()
            controller.update({'p': p, 't0': t0, 'h': h, 'dia': d, 'r': r}, replot=True)


        param_group = tk.LabelFrame(root, text='Basic Params', padx=5, pady=5)
        param_group.pack(padx=10, pady=10)

        p_label = tk.Label(param_group, text="P Type: ")
        p_label.grid(column=0,row=0,ipadx=5, pady=5, sticky=tk.W+tk.N)

        p_type = tk.StringVar(param_group)
        p_type.set(P_OPTIONS[0]) # default to [0]
        w = tk.OptionMenu(param_group, p_type, *P_OPTIONS)
        w.grid(column=1,row=0,ipadx=5, pady=5, sticky=tk.W+tk.N)

        p_type.trace('w', entry_update)

        dia_label = tk.Label(param_group, text="diameter [inch]: ")
        dia_label.grid(column=0,row=1,ipadx=5, pady=5, sticky=tk.W+tk.N)

        dia_entry = tk.Entry(param_group)
        dia_entry.insert(0, "3")
        dia_entry.grid(column=1,row=1,ipadx=5, pady=5, sticky=tk.W+tk.N)

        t0_label = tk.Label(param_group, text="T_0 [kN]: ")
        t0_label.grid(column=0,row=2,ipadx=5, pady=5, sticky=tk.W+tk.N)

        t0_entry = tk.Entry(param_group)
        t0_entry.insert(0, "100")
        t0_entry.grid(column=1,row=2,ipadx=5, pady=5, sticky=tk.W+tk.N)

        h_label = tk.Label(param_group, text="Water depth [m]: ")
        h_label.grid(column=0,row=3,ipadx=5, pady=5, sticky=tk.W+tk.N)

        h_entry = tk.Entry(param_group)
        h_entry.insert(0, "100")
        h_entry.grid(column=1,row=3,ipadx=5, pady=5, sticky=tk.W+tk.N)

        radius_label = tk.Label(param_group, text="Radius [m]: ")
        radius_label.grid(column=0,row=4,ipadx=5, pady=5, sticky=tk.W+tk.N)

        radius_entry = tk.Entry(param_group)
        radius_entry.insert(0, "1000")
        radius_entry.grid(column=1,row=4,ipadx=5, pady=5, sticky=tk.W+tk.N)



        update_button = tk.Button(text='update',
                                  command=entry_update)
        update_button.pack()

        replot_button = tk.Button(text='replot',
                                  command=replot_update)
        replot_button.pack()


        # canvas
        # self.fig = Figure(figsize=(5, 4), dpi=100)
        self.fig, self.ax = plt.subplots()

        self.canvas = FigureCanvasTkAgg(self.fig, root)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
