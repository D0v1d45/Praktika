import tkinter as tk
from tkinter import *
import requests
import cherry
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import credentials

ENDPOINT = "https://www.cherryservers.com"

"""""
frame = tk.Tk()
frame.title('Bezdione')

window_width = 1000
window_height = 800

TextContainer = tk.Text(frame, height = 45, width = 90)

TextContainer.pack(side=tk.LEFT)


#-------------------------------FUNCTIONS----------------------------------------------------------------
def ClrScreen():
    TextContainer.delete("1.0","end")

def GetServerInfo(server_ID):
    if server_ID == "":
        TextContainer.insert(tk.END,"Klaidingas arba nenurodytas serverio_ID")
    server = master.get_server(server_ID)
    TextContainer.insert(tk.END,server)

def GetPlans():
    plans = master.get_plans(team_id="91958")
    for plan in plans:
     p = json.dumps(plan)
    parse_p = json.loads(p)
    TextContainer.insert("1.0","Plan id: %s -> Plan name: %s -> Av: %s" % (parse_p['id'], parse_p['name'], parse_p['available_regions']))
"""""
def GetTeams():
    teams = credentials.master.get_teams()
    for team in teams:
        t = json.dumps(team)
    parse_t = json.loads(t)
    print("Team ID: %s -> Team Name: %s" % (parse_t['id'], parse_t['name']))

def GetSpecificServerInfo(server_ID):
    server = credentials.master.get_server(server_ID, fields="power,state,termination_date")
    print(server)
def DeleteServer(server_id):
    server = credentials.master.terminate_server(server_id)
    print("Delete server: %s" % server)

def OrderServer():
    ips = []
    ssh_keys=['95']

    server = credentials.master.create_server(project_id="79813", 
                              name="Cloud_Vps_1",
                              hostname="bla.com",
                              image="Ubuntu 20.04 64bit", 
                              region="EU-Nord-1",
                              ip_addresses=ips,
                              ssh_keys=ssh_keys,
                              plan_id="161")
    #TextContainer.insert(tk.END,"Server: %s" % server)
"""def SSHKEY(server_ID):
    master = cherry.Master(auth_token="")
    server = master.get_server(server_ID, fields="power,state,termination_date")
    OrderServer()
    TextContainer.insert(tk.INSERT,server)
"""
def ListPlans():
    url = "https://api.cherryservers.com/v1/plans"
    response = requests.get(url,headers=credentials.headers)
    print(response.content)
#-----------------------TESTS------------------------------------------------------------------------------
def test_acess_to_regions():
    url = "https://api.cherryservers.com/v1/regions"
    response = requests.get(url,headers=credentials.headers)
   # assert response.status_code ==200
    print(response.status_code)

def test_accesibility_to_images(slug):
    url = "https://api.cherryservers.com/v1/servers/{slug}/actions"
    response = requests.get(url,headers=credentials.headers)
    assert response.status_code ==200

def test_accesibility_to_images():
    url = "https://api.cherryservers.com/v1/teams"
    response = requests.get(url,headers=credentials.headers)
    assert response.status_code ==200
    

def test_accesibility_to_plans():
    url = "https://api.cherryservers.com/v1/plans"
    response = requests.get(url,headers=credentials.headers)
    assert response.status_code ==200
    
def test_acess_to_portal():
    response=requests.get(ENDPOINT)
    assert response.status_code==200

def test_GetTeams():
    teams = credentials.master.get_teams()
    for team in teams:
        t = json.dumps(team)
    parse_t = json.loads(t)
    print("Team ID: %s -> Team Name: %s" % (parse_t['id'], parse_t['name']))

def test_GetSpecificServerInfo():
    server = credentials.master.get_server(485857, fields="power,state,termination_date")
    print(server)
#def test_DeleteServer(server_id):
 #   server = master.terminate_server(server_id)
  #  print("Delete server: %s" % server)
    
#-----------------------------------------------------------------------------------------------------------
"""""
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
RefreshTextBox = tk.Button(frame, text="Refresh",font=('Helvetica 18 bold', 9), fg="black",width=30, command=GetTeams)
RefreshTextBox.place(x=750,y=120)

label = Label(frame, text='Server info')
label.place(x=350,y=5)
"""""
ListPlans()
#frame.mainloop()
