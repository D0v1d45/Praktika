from tkinter import *
import requests
import json
import credentials
from random import choice
import time
from datetime import datetime
import sys

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
def TerminateServer(server_id):
    server = credentials.master.terminate_server(server_id)


def DeployRandomServer():
    response=requests.get(ENDPOINT)
    assert response.status_code==200
    if(response.status_code==200):
        print("Serveris yra uzsakomas...")
        startftime = time.time()
        server = credentials.master.create_server(project_id="149121",
                                                hostname = "",
                                                image=setImage,
                                                region=setRegion,
                                                plan_id=(setPlan))
        
        start_time =datetime.now()
        while True:
            time.sleep(1)
            ServerID = credentials.master.get_server(server['id'],fields="id,state")
            if(ServerID['state'] == 'active'):
                    
                print("Serveris uzsakytas sekmingai")
                end_time = datetime.now()
                timex = end_time - start_time
                with open("logs.json", "a") as data:
                        server2 = credentials.master.get_server(server['id'],fields="plan,state,created_at")
                        server2["Deployment_Start_Time"] = start_time
                        server2["Test_Plan id"] = setPlan
                        server2["Test_Region"] = setRegion
                        server2["Test_Image"] = setImage
                        server2["Deployment_end_time"] = end_time
                        server2["Time taken for deployment"] = timex
                        server2["Test status"] = "Succesful"
                        json.dump(server2, data,indent=2,default=str)
                        time.sleep(60)
                        TerminateServer(server['id'])
                        print("Serveris istrintas")
                        UserInput = input("Baigiu darba")
                break
            else: 
                    endtime = time.time()
                    end_time = datetime.now()
                    timex = end_time - start_time
                    elapsed_time = endtime-startftime
                    if(elapsed_time >= 900):  
                        print("serverio uzsakyti nepavyko")
                        with open("logs.json", "a") as data:
                            server2["Deployment_Start_Time"] = start_time
                            server2["Test_Plan id"] = setPlan
                            server2["Test_Region"] = setRegion
                            server2["Test_Image"] = setImage
                            server2["Deployment_end_time"] = end_time
                            server2["Time taken for deployment"] = timex
                            server2["Test status"] = "Failed"
                            json.dump(server2, data,indent=2,default=str)
                            UserInput = input("Baigiu darba")
                        break
    else:
        print("Portalas nepasiekiamas")

def DeployServer(img,reg,id):
    response=requests.get(ENDPOINT)
    assert response.status_code==200
    if(response.status_code==200):
        print("Serveris yra uzsakomas...")
        startftime = time.time()
        server = credentials.master.create_server(project_id="149121", 
                                image=img, 
                                region=reg,
                                plan_id=id)
       
        start_time =datetime.now()
        while True:
            time.sleep(1)
            ServerID = credentials.master.get_server(server['id'],fields="id,state")
            if(ServerID['state'] == 'active'):
                    
                print("Serveris uzsakytas sekmingai")
                end_time = datetime.now()
                timex = end_time - start_time
                with open("logs.json", "a") as data:
                        server2 = credentials.master.get_server(server['id'],fields="id,plan,state,created_at")
                        server2["Deployment_Start_Time"] = start_time
                        server2["Test_Plan id"] = id
                        server2["Test_Region"] = reg
                        server2["Test_Image"] = img
                        server2["Deployment_end_time"] = end_time
                        server2["Time taken for deployment"] = timex
                        server2["Test status"] = "Succesful"
                        json.dump(server2, data,indent=2,default=str)
                        time.sleep(60)
                        TerminateServer(server['id'])
                        print("Serveris istrintas")
                        UserInput = input("Baigiu darba")
                break
            else: 
                    endtime = time.time()
                    end_time = datetime.now()
                    timex = end_time - start_time
                    elapsed_time = endtime-startftime
                    if(elapsed_time >= 780):  
                        print("serverio uzsakyti nepavyko")
                        with open("logs.json", "a") as data:
                            server2["Deployment_Start_Time"] = start_time
                            server2["Test_Plan id"] = id
                            server2["Test_Region"] = reg
                            server2["Test_Image"] = img
                            server2["Deployment_end_time"] = end_time
                            server2["Time taken for deployment"] = timex
                            server2["Test status"] = "Failed"
                            json.dump(server2, data,indent=2,default=str)
                            UserInput = input("Baigiu darba")
                        break
    else:
        print("Portalas nepasiekiamas")

print("Pasirinkite viena varijanta is 3 pateiktu ir spauskite skaiciu")
print('1-Atsitiktinio serverio uzsakymas')
print('2-Uzsakyti serveri su ivestais parametrais ')
print( '3-baigti darba')
while True:
    try:
     User_input = int(input("Iveskite skaiciu 1 arba 2 arba 3: "))
    except ValueError:
        print('Galima vesti tik skaicius')
        continue
    if User_input == 1:
        DeployRandomServer()
        User_inputt = (input)
        break
    elif User_input == 2:
        while True:
            img = input("Iveskite operacine sistema :")
            if(img in Image_List):
                while True:
                    reg = input("Iveskite regiona :")
                    if(reg in Region_list):
                            while True:
                                try:
                                    plan_id = int(input("Iveskite plano id :"))
                                except ValueError:
                                    print('Galima vesti tik skaicius arba klaidingas id')
                                    continue
                                if(plan_id in Plan_list):
                                    DeployServer(img,reg,plan_id)
                                    sys.exit()     
                                break
                    else:
                        print("Ivestis negali būti tuscia arba klaidingi parametrai")  
            else:
                print("Ivestis negali būti tuscia arba klaidingi parametrai")
                
    elif User_input == 3: 
        break             
    else:
        print("Blogai ivestas skaicius")

