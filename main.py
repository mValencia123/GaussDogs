import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "C:/Users/maxva/Documents/Machine Learning/GaussDogs/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.xlsx*"),
                                                       ("all files",
                                                        "*.*")))
      
    df = pd.read_excel(filename, sheet_name='Hoja1')
    mu = df["Edad"].mean()
    std = df["Edad"].std()
    x = df["Edad"].tolist()
    x.sort()
    y = 1/(std * np.sqrt(2*np.pi)) * np.exp(-0.5*((x-mu)/std)**2)
    plt.plot(x,y,color="black")
    plt.show()

    x = np.linspace(mu - 3*std, mu + 3*std, 100)
    plt.plot(x, norm.pdf(x, mu, std))
    plt.show()

    print("Mean: "+mu)
    print("Std: "+std)

w = tk.Tk()
w.title("Dogs and Normal Distribution")
w.config(width=400, height=300)

title = ttk.Label(text="Normal Distribution Graphic")
title.place(x=130, y=20)

buttonLoad = ttk.Button(text="Load File and Watch Graphic", command=browseFiles)
buttonLoad.place(x=120, y=250)

w.mainloop()