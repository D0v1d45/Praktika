import tkinter as tk
from tkinter import *
import requests
import cherry
import json
from bs4 import BeautifulSoup

frame = tk.Tk()
frame.title('Bezdione')

window_width = 1000
window_height = 800

TextContainer = tk.Text(frame, height = 45, width = 90)

TextContainer.pack(side=tk.LEFT)


URL = "https://mesa.cherryservers.com/api/v1/client-sessions"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/json',
    'Origin': 'https://portal.cherryservers.com',
    'Connection': 'keep-alive',
    'Referer': 'https://portal.cherryservers.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',

}

data = '{username:,password:.}'
s=requests.session()
response = s.post(URL,data=data)
soup = BeautifulSoup(response.content,'html.parser')
print(response)
#response = requests.post('https://mesa.cherryservers.com/api/v1/client-sessions', headers=headers, data=data)


#-------------------------------FUNCTIONS----------------------------------------------------------------
def ClrScreen():
    TextContainer.delete("1.0","end")

def GetServerInfo(server_ID):
    if server_ID == "":
        TextContainer.insert(tk.END,"Klaidingas arba nenurodytas serverio_ID")
    master = cherry.Master(auth_token="")
    server = master.get_server(server_ID)
    TextContainer.insert(tk.END,server)

def OrderServer():
    master = cherry.Master(auth_token="")
    ips = []
    ssh_keys=['95']

    server = master.create_server(project_id="79813", 
                              name="super-duper",
                              hostname="bla.com",
                              image="Ubuntu 16.04 64bit", 
                              region="EU-Nord-1",
                              ip_addresses=ips,
                              ssh_keys=ssh_keys,
                              plan_id="161")
    TextContainer.insert(tk.END,"Server: %s" % server)
def SSHKEY(server_ID):
    master = cherry.Master(auth_token="")
    server = master.get_server(server_ID, fields="power,state,termination_date")
    OrderServer()
    TextContainer.insert(tk.INSERT,server)




    
#-----------------------------------------------------------------------------------------------------------
# screen dimenisons
screen_width = frame.winfo_screenwidth()
screen_height = frame.winfo_screenheight()

# center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
frame.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
ButtonStart = tk.Button(frame, text="Start", fg="green",width=30, command=quit)
ButtonStart.place(x=750,y=30)


frame.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
ButtonExit = tk.Button(frame, text="Exit", fg="red",width=30, command=quit)
ButtonExit.place(x=750,y=90)

frame.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
ButtonClear = tk.Button(frame, text="Clear the screen",font=('Helvetica 18 bold', 9), fg="red",width=30, command=ClrScreen)
ButtonClear.place(x=750,y=60)

frame.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
RefreshTextBox = tk.Button(frame, text="Refresh",font=('Helvetica 18 bold', 9), fg="black",width=30, command=GetServerInfo("485855"))
#RefreshTextBox = tk.Button(frame, text="Refresh",font=('Helvetica 18 bold', 9), fg="black",width=30, command=SSHKEY("485855"))
RefreshTextBox.place(x=750,y=120)

label = Label(frame, text='Server info')
label.place(x=350,y=5)


frame.mainloop()
