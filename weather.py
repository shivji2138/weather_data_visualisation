import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


#main window for the gui app
app = ctk.CTk()
app.title("Weather Analysis")
app.geometry("900x650")
app.configure(fg_color="#435C9C")

# getting details from csv file
data = pd.read_csv("weather_jan24.csv")


#function for plotting a graph between preciptation on days
def preciptation_graph():
    win = tk.Toplevel(app)
    win.title("Percipitation graph")
    win.geometry("850x600")
    
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(data['date'].str[-2:], data['precipitation'], marker='o', color='blue')
    ax.set_title('Precipitation Trend Over Days')
    ax.set_xlabel('Date')
    ax.set_ylabel('Precipitation (mm)')
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig,master=win)
    canvas.draw()
    canvas.get_tk_widget().pack()

#function for plotting weather type: pie chart
def weather_type():
    win =tk.Toplevel(app)
    win.title("Weather Type Distribution")
    win.geometry("850x600")

    weather_count = data["weather"].value_counts()
    fig,ax =plt.subplots(figsize=(10,6))
    ax.pie(weather_count, labels=weather_count.index, autopct="%1.1f%%",startangle=90)
    ax.set_title("Weather Type Distribution")

    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack()


def mintemp_graph():
    win = tk.Toplevel(app)
    win.title("Minimum Temperature graph")
    win.geometry("850x600")
    
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(data['date'].str[-2:], data['temp_min'], marker='o', color='blue')
    ax.set_title('Minimum Temperature Over Days')
    ax.set_xlabel('Date')
    ax.set_ylabel('Temperature(C)')
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig,master=win)
    canvas.draw()
    canvas.get_tk_widget().pack()

#main window 
ctk.CTkLabel(app, text="🌦 Weather Data Visualization", font=("Segoe UI", 26, "bold")).pack(pady=30)


ctk.CTkButton(app, text="🌧 Precipitation Trend", command=preciptation_graph, width=250, height=40, corner_radius=10, fg_color="#007acc").pack(pady=15)
ctk.CTkButton(app, text="☁ Weather Type Trend", command=weather_type, width=250, height=40, corner_radius=10, fg_color="#4caf50").pack(pady=15)
ctk.CTkButton(app, text="🌡 Minimum Temperature Trend", command=mintemp_graph, width=250, height=40, corner_radius=10, fg_color="#e63946").pack(pady=15)

ctk.CTkButton(app, text="Exit", command=app.destroy, width=120, fg_color="#333333", hover_color="#000000").pack(pady=30)




app.mainloop()
