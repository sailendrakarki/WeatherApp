import tkinter as tk ##to design desktop Application
from tkinter import font ##To load font Style
from datetime import datetime ## To derive Datetime
import requests ##To requests
import configparser as cp

class WeatherApp(object):
    HEIGTH=0
    WIDTH=0
    

    def __init__(self,height,width):
        self.HEIGTH=height
        self.WIDTH=width
        self.config= cp.ConfigParser()
        self.config.read('config.ini')
        self.loadCanvas()
    
    def getWeather(self,cityName):
        self.weatherkey=self.config.get('OPENMAPAPI','weatherKey')
        self.url=self.config.get('OPENMAPAPI','url')
        self.parameters={'APPID':eval(self.weatherkey),'q':cityName,'units':'imperial'}
        self.response = requests.get(eval(self.url),self.parameters)
        self.displayContent['text'] = self.formatJson(self.response.json())
    
    def formatJson(self,weatherDetail):
        try:
            self.city = weatherDetail['name']
            self.wtDescrp = weatherDetail['weather'][0]['description']
            self.temp= weatherDetail['main']['temp']
            self.requestTime= datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            self.information = 'City: %s \nWeather: %s \nTemperature: %s \nTime:%s ' %(self.city,self.wtDescrp,self.temp,self.requestTime)
        except:
            self.information='Unable to Retrieve information'
    
        return self.information

    
    def loadCanvas(self):
        self.root = tk.Tk()
        self.root.title("WeatherApp")
        self.canvas = tk.Canvas(self.root,height=self.HEIGTH,width=self.WIDTH)
        self.canvas.pack()
        
        self.top_frame=tk.Frame(self.root,bg='#80c1ff',bd=5)
        self.top_frame.place(relwidth=0.75,relheight=0.1,relx=0.5,rely=0.1,anchor='n')

        self.inputBox=tk.Entry(self.top_frame,font=('courier',30))
        self.inputBox.place(relwidth=0.65,relheight=1)

        self.clickButton=tk.Button(self.top_frame,text="Weather Update",command=lambda :self.getWeather(self.inputBox.get()))
        self.clickButton.place(relwidth=0.30,relheight=1,relx=0.70,rely=0)

        self.bw_frame=tk.Frame(self.root,bg='#88c1ff',bd=10)
        self.bw_frame.place(relwidth=0.75,relheight=.50,relx=0.5,rely=0.30,anchor='n')
        

        self.displayContent= tk.Label(self.bw_frame,font=('courier',30))
        self.displayContent.place(relheight=1,relwidth=1)
        self.root.mainloop()
    
def main():
    WeatherApp(700,800)

if __name__=='__main__':
    main()
