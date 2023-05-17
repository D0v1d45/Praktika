import tkinter as tk
from tkinter import *
import requests
import json
import credentials
from random import choice
import time


t = time.localtime()
ENDPOINT = "https://www.cherryservers.com"


Plan_list = list()
Region_list = list()
Image_List = list()

plans = credentials.master.get_plans(team_id="91958")
for plan in plans:
     p = json.dumps(plan)
     parse_p = json.loads(p)
     Plan_list.append(parse_p["id"])


Regions = credentials.master.get_plans(team_id="91958")
for plan in Regions:
    for region in plan['available_regions']:
        region=region['name']
        Region_list.append(region)

setRegion = choice(Region_list)
setPlan = choice(Plan_list)

images = credentials.master.get_images(plan_id=setPlan)
for image in images:
    im = json.dumps(image)
    parse_image = json.loads(im)
    Image_List.append(parse_image["name"])
                                 
setImage = choice(Image_List)

data ={
        "Plan Id": setPlan,
        "Region" : setRegion,
        "Image" : setImage
    }
#print(json.dumps(data))

def DeployRandomServer():
    
    server = credentials.master.create_server(project_id="149121",
                                               hostname = "",
                                               image=setImage,
                                               region=setRegion,
                                               plan_id=(setPlan))
    server2 = credentials.master.get_server(server['id'],fields="plan,power,state,created_at")
    current_time = time.strftime("%H:%M:%S", t)
    with open("logs.json", "a") as data:
        server2["Test_Started_Time"] = current_time
        server2['Test_Hostname'] = "hostname"
        server2["Test plan id"] = setPlan
        server2["Test Region"] = setRegion
        server2["Test image"] = setImage
        json.dump(server2, data,indent=2)
        """""
    while True:
        time.sleep(30)
        ServerID = credentials.master.get_server(server['id'],fields="id,state")
        
        if(ServerID['state'] == 'active'):
            print("Serveris uzsakytas sekmingai")
            break
        else:
            print("serverio uzsakyti nepavyko")
  """""
def test_DeployServer(hostname,img,reg,id):
    server = credentials.master.create_server(project_id="149121", 
                              hostname=hostname,
                              image=img, 
                              region=reg,
                              plan_id=id)
    server2 = credentials.master.get_server(server['id'],fields="id,plan,power,state,created_at")
    current_time = time.strftime("%H:%M:%S", t)
    with open("logs.json", "a") as data:
            server2["Test_Started_Time"] = current_time
            server2['Test_Hostname'] = hostname
            server2["Test_Plan id"] = id
            server2["Test_Region"] = reg
            server2["Test_Image"] = img
            json.dump(server2, data,indent=2)
    
    while True:
        time.sleep(30)
        ServerID = credentials.master.get_server(server['id'],fields="id,state")
        
        if(ServerID['state'] == 'active'):
            print("Serveris uzsakytas sekmingai")
            break
        else:
            print("serverio uzsakyti nepavyko")
    
def DeleteServer(server_id):
    server = credentials.master.terminate_server(server_id)
    print("Serveris istrintas: %s" % server["id"])

print("/////////////////////////////Bezdione Bot //////////////////////////////////////////")
print("pasirinkite viena varijanta is 2 pateiktu ir spauskite skaiciu")
print('1-Atsitiktinio serverio uzsakymas')
print('2-Uzsakyti serveri su ivestais parametrais ')
while True:
    User_input = int(input("Iveskite skaiciu (1 arba 2): "))

    if User_input == 1:
        DeployRandomServer()
        break
    elif User_input == 2:
        hostname = input("iveskite serverio pavadinima :")
        img = input("Iveskite operacine sistema :")
        reg = input("Iveskite regiona :")
        plan_id = input('Iveskite plano id :')
        
        test_DeployServer(hostname,img,reg,plan_id)
        break
    else:
        print("Blogai ivestas skaicius")




"""""
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
    """""
#-----------------------------------------------------------------------------------------------------------
