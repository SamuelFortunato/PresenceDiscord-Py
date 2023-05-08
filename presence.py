from pypresence import Presence
import time
import random
import os

a1 = input("Application ID : ")
a5 = input("Details : ")
a2 = input("Quote 1 : ")
a3 = input("Quote 2 : ")
a4 = input("Quote 3 : ")
a5 = input("Photo: ")
os.system("cls")

client_id = (a1)
RPC = Presence(client_id )
RPC.connect()

print("Connected Presence V.3 (ON)")
print("Developed by :  Mukasz / @mukasz_")

quotes =[
    (a2),
    (a3),
    (a4)
]

large_image_photo = (a5)

#url e botão

while True:
    RPC.update(
        details=(a5), 
        state=random.choice(quotes), 
        large_image=(a5),
        buttons=[{"label": "Clique!", "url": "URL HERE!"}]
    )
    time.sleep(5)