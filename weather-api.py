# imports

import tkinter as tk
import requests
from PIL import ImageTk,Image

# Width and Size value for the screen
HEIGHT = 600
WIDTH = 880


def format_output(weather):
    try:
        name = str(weather['name'])
        descrption = str(weather['weather'][0]['description'])
        temp = str(weather['main']['temp'])
        Pressure = str(weather['main']['pressure'])
        Humidity = str(weather['main']['humidity'])
        max= str(weather['main']['temp_max'])
        min = str(weather['main']['temp_min'])
        final_result = 'Name: {} \nCondition: {} \nTemperature (°F): {}\n'.format(name, descrption, temp)
        final_result2 = 'Pressure: {} \nHumidity: {}\n'.format(Pressure,Humidity)
        final_result3 = 'Min-temp: {} \nMaxtemp: {}'.format(min, max)
        final= final_result +  final_result2 + final_result3
    except Exception:
        final= 'Something went wrong while fetching details'

    return final


def get_weather(city):
    #weather_key ='70cfa302d957ee0b76e02ba5bc699eb8'
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=70cfa302d957ee0b76e02ba5bc699eb8&q='+city
    response = requests.get(url)
    weather_report = response.json()

    output_label['text'] = format_output(weather_report)


# Creating a main window
window = tk.Tk()
window.title('Weather Application')

# Creating the canvas for the window to increase the size
canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
background_image = tk.PhotoImage('C:/Users/Kabira1947/Desktop/download.gif')
background_label = tk.Label(window, image=background_image)
background_label.image = background_image
background_label.pack()
background_label.place(x=0, y=0, relwidth=1, relheight=1)
canvas.pack()

# Background image
'''
background_image = tk.PhotoImage(Image.open('./bg1.png'))
logo = tk.Label(window, image=background_image)
logo.pack()
'''

# Creating the frame
frame = tk.Frame(window, bg='#25CCF7', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# Creating entry feild
entry = tk.Entry(frame, font=('Monaco', 20))
entry.place(relwidth=0.65, relheight=1)

# creating button.
button = tk.Button(frame, font=('Monaco', 18), text="Get Weather", command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

# creating the output frame

output_frame = tk.Frame(window, bd=10, bg='#25CCF7')
output_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# creating the output label

output_label = tk.Label(output_frame, font=('Monaco', 18), justify='left', anchor='nw', bd=4)
output_label.place(relwidth=1, relheight=1)

window.mainloop()
()
