import tkinter as tk

root=tk.Tk()
l1=tk.Label(root,text='city name ')
e1=tk.Entry(root)


def data():
    
    import requests
    city_name =e1.get()
   
    API_key="9d746918120a04212a70514deb59e40d"
    ws=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}")
    if ws.json()['cod']=='404':
        n0.config(text=f"city name not found \n please refresh tha page and try again ")
    else:
        
        n1.config(text=f"City Name:  {city_name}")
        country=ws.json()['sys']['country']
        n2.config(text=f"City is in : {country}")
        
        lon=ws.json()['coord']['lon']
        n3.config(text=f"Longitude : {lon}")
        
        lat=ws.json()['coord']['lat']
        n4.config(text=f"Latitude : {lat}")
        
        weather=ws.json()['weather'][0]['main']
        n5.config(text=f"Weather of {city_name} : {weather}")
    
        temp=ws.json()['main']['temp']
        n6.config(text=f"Temp is  : {temp} (in k)")
        
        pressure=ws.json()['main']['pressure']
        n7.config(text=f"Pressure is : {pressure} mb")
        
        humidity=ws.json()['main']['humidity']
        n8.config(text=f"Humidity is : {humidity}%")
        
        wind_speed=ws.json()['wind']['speed']
        n9.config(text=f"Wind Speed : {wind_speed} m/s")
        

b=tk.Button(root,text="check",command=data)

l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
b.grid(row=2,column=1)

n0=tk.Label(root)
n0.grid(row=3,column=1)

n1=tk.Label(root)
n1.grid(row=3,column=1)

n2=tk.Label(root)
n2.grid(row=4,column=1)

n3=tk.Label(root)
n3.grid(row=5,column=1)

n4=tk.Label(root)
n4.grid(row=6,column=1)


n5=tk.Label(root)
n5.grid(row=7,column=1)

n6=tk.Label(root)
n6.grid(row=8,column=1)

n7=tk.Label(root)
n7.grid(row=9,column=1)

n8=tk.Label(root)
n8.grid(row=10,column=1)

n9=tk.Label(root)
n9.grid(row=11,column=1)

root.mainloop() 