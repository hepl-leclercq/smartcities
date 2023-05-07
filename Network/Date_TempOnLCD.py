# Importing necessary libraries
from lcd1602 import LCD1602
import network
from machine import  I2C, Pin
import urequests as urequests
import json
import utime
import ntptime

# Setting up API key and Wi-Fi connection
key = {'lat':'50.40265576041325',
       'lon':'6.14072611895203',
       'appid':'96c3c8e0620f4a874b122e53026e8619',
       'units':'metric'}

wlan = network.WLAN (network.STA_IF)
wlan.active (True)
wlan.connect ("WiFi-2.4-1235", "0AE81F9309")
print (wlan.isconnected())

# Synchronizing with NTP server
ntptime.settime()

# Setting up RTC to the current time
rtc=machine.RTC()
tampon1=utime.time()
tampon2=tampon1+7200

(year, month, mday, hour, minute, second, weekday, yearday)=utime.localtime(tampon2)
rtc.datetime((year, month, mday, 0, hour, minute, second, 0))
utime.sleep (1)

# Setting up LCD screen
i2c_1 = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c_1, 2, 16)
d.display()
d.clear()

# Function to fetch data from OpenWeatherMap API
def get_data(api, key):
    params = "&".join([f"{k}={v}" for k, v in key.items()])
    url = f"{api}?{params}"
    response = urequests.get(url)
    if response.status_code == 200:
        print("sucessfully fetched the data")
        print(response.json())
        data = json.loads(response.content)
        global temperature
        global Lieu
        temperature = data['main']['temp']
        print(f"Temperature: {temperature}°C")
        Lieu = data['name']
        print(f"Lieu: {Lieu}")
    else:
        print(f"Hello person, there's a {response.status_code} error with your request")

# Fetching data for the first time
get_data("https://api.openweathermap.org/data/2.5/weather", key)

i = 1
# Main loop to display time and temperature on LCD screen
while(True):
    # Getting current time
    Date = utime.localtime()
    year = str (Date[0])
    month = str (Date[1])
    day = str (Date[2])
    hour = str(Date [3]) 
    minute = str(Date [4])
    second = (Date [5])
    STRsecond = str(second)
    
    # Updating display every minute
    if (second == 00):
        LCDHour = hour + ":" + minute
        LCDDate = day + "/" + month + "/" + year
        
        # Updating LCD display
        d.clear() 
        d.setCursor(0, 0)
        d.print (LCDDate)
        d.setCursor(10, 0)
        d.print (LCDHour)
        d.setCursor(0, 1)
        d.print (str(temperature))
        d.write(0b11011111)
        d.setCursor(7, 1)
        d.print ("> ")
        d.print (Lieu)
    
    # Fetching new data every 10 minutes
    if (int(minute)%10 == 0 and i == 1):
        get_data("https://api.openweathermap.org/data/2.5/weather", key)
        i = 0
    
    if (int(minute)%10 == 1 and i == 0):
        i = 1 
