from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image,ImageTk
import json
from tkinter import*
import cv2

#Xây dựng màn hình nền 
root =Tk()
root.title('Ứng dụng dự báo thời tiết')
root.geometry('890x470+300+300')
root.configure(bg='#57adff')
root.resizable(False,False)
def getWeather():
    
    city = textfield.get()
    geolocator= Nominatim(user_agent='geoapiExercises')
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng = location.longitude,lat = location.latitude)
    timezone.config(text = result)
    long_lat.config(text=f'{round(location.latitude,4)}*N{round(location.longitude,4)}*E')
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time=local_time.strftime('%I:%M %p')    
    clock.config(text=current_time)
    #apiweather
    api = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=75b285a2616a12fd328c033e2b61d53f'
    #https://api.openweathermap.org/data/3.0/onecall?lat='+str(location.latitude)+'&lon='+str(location.longitude)+'&exclude=daily&appid=12949caca3f1ed6317c59c6285ef85e8
    json_data = requests.get(api).json()
    #current
    temp= json_data.get('main',{}).get('temp')
    humidity = json_data.get('main',{}).get('humidity')
    pressure = json_data.get('main',{}).get('pressure') 
    wind = json_data.get('wind',{}).get('speed')
    
    
    t.config(text=(round(temp-273,4),'*C'))
    h.config(text=(humidity,'%'))
    p.config(text=(pressure,'HPA'))
    w.config(text=(wind,'m/s'))

    #day
    first= datetime.now()
    day1.config(text = first.strftime('%A'))
        
    second = first + timedelta(days=1)
    day2.config(text = second.strftime('%A'))

    third = first + timedelta(days=2)
    day3.config(text = third.strftime('%A'))

    fourth = first + timedelta(days=3)
    day4.config(text = fourth.strftime('%A'))

    firth = first + timedelta(days=4)
    day5.config(text = firth.strftime('%A'))

    sixth = first + timedelta(days=5)
    day6.config(text = sixth.strftime('%A'))

    seventh = first + timedelta(days=6)
    day7.config(text = seventh.strftime('%A'))   

    #cell1
    firstdayimage =json_data['weather'][0]['icon']
    photo1 = ImageTk.PhotoImage(file =f'icon/{firstdayimage}@2x.png')
    firstimage.config(image=photo1)
    firstimage.image=photo1
    tempmin1 = json_data.get('main',{}).get('temp_min')
    tempmax1= json_data.get('main',{}).get('temp_max')
    day1temp.config(text=f'Max:{tempmin1}\n Min:{tempmax1}')


    #cell2
    seconddayimage =json_data['weather'][0]['icon']
    tempmin2 = json_data.get('main',{}).get('temp_min')
    tempmax2= json_data.get('main',{}).get('temp_max')
    day2temp.config(text=f'Max:{tempmin2}\n Mn:{tempmax2}')
    
    ##cell3
    thirddayimage =json_data['weather'][0]['icon']
    tempmin3 = json_data.get('main',{}).get('temp_min')
    tempmax3= json_data.get('main',{}).get('temp_max')
    day3temp.config(text=f'Min:{tempmin3}\n Max:{tempmax3}')
    

    #cell4
    fourthdayimage =json_data['weather'][0]['icon']
    
    tempmin4= json_data.get('main',{}).get('temp_min')
    tempmax4= json_data.get('main',{}).get('temp_max')
    day4temp.config(text=f'Min:{tempmin4}\n Max:{tempmax4}')
    

    #cell5
    firthdayimage =json_data['weather'][0]['icon']
    
    tempmin5 = json_data.get('main',{}).get('temp_min')
    tempmax5= json_data.get('main',{}).get('temp_max')
    day5temp.config(text=f'Min:{tempmin5}\n Max:{tempmax5}')
    

    #cell6
    sixthdayimage =json_data['weather'][0]['icon']
    
    tempmin6 = json_data.get('main',{}).get('temp_min')
    tempmax6= json_data.get('main',{}).get('temp_max')
    day6temp.config(text=f'Min:{tempmin6}\n Max:{tempmax6}')
    


    #cell7
    seventhdayimage =json_data['weather'][0]['icon']
    
    tempmin7 = json_data.get('main',{}).get('temp_min')
    tempmax7= json_data.get('main',{}).get('temp_max')
    day7temp.config(text=f'Min:{tempmin7}\n Night:{tempmax7}')
    

    

#icon
image_icon = PhotoImage(file='image/logo.png')
root.iconphoto(False,image_icon)
Round_box = PhotoImage(file='image/HCNBlack.png')
Label(root,image=Round_box,bg='#57adff').place(x=30,y=100)

#label
label1 = Label(root,text='Temperture',font=('Helvetica',11),fg = 'yellow',bg ='#203243')
label1.place(x=50,y=120)
label2 = Label(root,text='Humidity',font=('Helvetica',11),fg = 'yellow',bg ='#203243')
label2.place(x=50,y=140)
label3 = Label(root,text='Pressure',font=('Helvetica',11),fg = 'yellow',bg ='#203243')
label3.place(x=50,y=160)
label4 = Label(root,text='Wind Speed',font=('Helvetica',11),fg = 'yellow',bg ='#203243')
label4.place(x=50,y=180)


#SearchBox

textfield=tk.Entry(root,justify='center',width = 17,font=('poppins',16,'bold'),bg ='#203243',border = 0,fg ='white')
textfield.place(x=453,y=104)
textfield.focus()

Search_icon = PhotoImage(file ='image/nutnhan.png')
myimage_icon = Button(image=Search_icon,borderwidth=0,cursor='hand2',bg='#203243',command = getWeather) 
myimage_icon.place(x=652,y=104)

#Bottom Box
frame=Frame(root,width=900,height=180,bg='#212120')
frame.pack(side = BOTTOM)
#Bottom boxes
firstbox = PhotoImage(file='image/HCNBlack.png')
secondbox = PhotoImage(file='image/khungden2.png')

Label(frame,image=firstbox,bg='#212120').place(x=10,y=12)
Label(frame,image=secondbox,bg='#212120').place(x=310,y=25)
Label(frame,image=secondbox,bg='#212120').place(x=410,y=25)
Label(frame,image=secondbox,bg='#212120').place(x=510,y=25)
Label(frame,image=secondbox,bg='#212120').place(x=610,y=25)
Label(frame,image=secondbox,bg='#212120').place(x=710,y=25)
Label(frame,image=secondbox,bg='#212120').place(x=810,y=25)

#Clock time
clock = Label(root,font =('Helvetica',20,'bold'),fg='white',bg='#57adff')
clock.place(x=30,y=20)

#Timezone
timezone = Label(root,font =('Helvetica',20),fg='white',bg='#57adff')
timezone.place(x=700,y=20)

long_lat = Label(root,font =('Helvetica',10),fg='white',bg='#57adff')
long_lat.place(x=700,y=60)

#thpwd
t = Label(root,font=('Helvetica',11),fg='yellow',bg='#203243')
t.place(x=200,y= 120)

h = Label(root,font=('Helvetica',11),fg='yellow',bg='#203243')
h.place(x=200,y= 140)

p = Label(root,font=('Helvetica',11),fg='yellow',bg='#203243')
p.place(x=200,y= 160)

w = Label(root,font=('Helvetica',11),fg='yellow',bg='#203243')
w.place(x=200,y= 180)

#1cell
firstframe = Frame(root,width=280,height = 157,bg='#282829')
firstframe.place(x=10,y=305)

day1 = Label(firstframe,font='arial 20',bg='#282829',fg='#fff')
day1.place(x=100,y=5)
firstimage = Label(firstframe,bg='#282829')
firstimage.place(x=1,y=15)

day1temp = Label(firstframe,bg='#282829',fg='#57adff',font='arial 15 bold')
day1temp.place(x=100,y=50)

#2cell
secondframe = Frame(root,width=70,height = 126,bg='#282829')
secondframe.place(x=310,y=315)

day2 = Label(secondframe,bg='#282829',fg='#fff')
day2.place(x=10,y=5)

secondimage = Label(secondframe,bg='#282829')
secondimage.place(x=7,y=20)

day2temp = Label(secondframe,bg='#282829',fg='#fff')
day2temp.place(x=10,y=70)
#3cell
thirdframe = Frame(root,width=70,height = 126,bg='#282829')
thirdframe.place(x=410,y=315)

day3 = Label(thirdframe,bg='#282829',fg='#fff')
day3.place(x=10,y=5)

thirdimage = Label(thirdframe,bg='#282829')
thirdimage.place(x=7,y=20)

day3temp = Label(thirdframe,bg='#282829',fg='#fff')
day3temp.place(x=10,y=70)
#4cell
fourthframe = Frame(root,width=70,height = 126,bg='#282829')
fourthframe.place(x=510,y=315)

day4 = Label(fourthframe,bg='#282829',fg='#fff')
day4.place(x=10,y=5)

fourthimage = Label(fourthframe,bg='#282829')
fourthimage.place(x=7,y=20)

day4temp = Label(fourthframe,bg='#282829',fg='#fff')
day4temp.place(x=10,y=70)

#5cell
firthframe = Frame(root,width=70,height = 126,bg='#282829')
firthframe.place(x=610,y=315)

day5 = Label(firthframe,bg='#282829',fg='#fff')
day5.place(x=10,y=5)

firthimage = Label(firthframe,bg='#282829')
firthimage.place(x=7,y=20)

day5temp = Label(firthframe,bg='#282829',fg='#fff')
day5temp.place(x=10,y=70)


#6cell
sixthframe = Frame(root,width=70,height = 126,bg='#282829')
sixthframe.place(x=710,y=315)

day6 = Label(sixthframe,bg='#282829',fg='#fff')
day6.place(x=10,y=5)

sixthimage = Label(sixthframe,bg='#282829')
sixthimage.place(x=7,y=20)

day6temp = Label(sixthframe,bg='#282829',fg='#fff')
day6temp.place(x=10,y=70)

#7cell
seventhframe=Frame(root,width=70,height=126,bg='#282829')
seventhframe.place(x=810,y=315)

day7 = Label(seventhframe,bg='#282829',fg='#fff')
day7.place(x=10,y=5)

seventhimage = Label(seventhframe,bg='#282829')
seventhimage.place(x=7,y=20)

day7temp = Label(seventhframe,bg='#282829',fg='#fff')
day7temp.place(x=10,y=70)

root.mainloop()
