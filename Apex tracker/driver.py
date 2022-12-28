from Apexrank import *
from tkinter import *

main = Tk()  
main.geometry("300x300") 
main.resizable(False,False)
main.title("Apex rank tracker")

auth_input = StringVar()
username_input = StringVar()
platform_input = StringVar()

def addProfile_Clicked():
    auth = auth_input.get()
    username = username_input.get()
    platform = platform_input.get()

    if(platform == "PC (Steam/Origin)"):
        platform = "PC"
    else:
        platform = "Console"

    if(auth != "" and username != "" and platform != ""):
        addProfile(username,platform,auth)

def compareProfile_Clicked():
    auth = auth_input.get()
    username = username_input.get()
    platform = platform_input.get()

    if(platform == "PC (Steam/Origin)"):
        platform = "PC"
    else:
        platform = "Console"

    if(auth != "" and username != "" and platform != ""):
        compareProfile(username,platform,auth)

def updateProfile_Clicked():
    auth = auth_input.get()
    username = username_input.get()
    platform = platform_input.get()

    if(platform == "PC (Steam/Origin)"):
        platform = "PC"
    else:
        platform = "Console"

    if(auth != "" and username != "" and platform != ""):
        updateProfile(username,platform,auth)

def deleteProfile_Clicked():
    username = username_input.get()
    platform = platform_input.get()

    if(username != ""):
        deleteProfile(username)

def recordGame_Clicked():
    auth = auth_input.get()
    username = username_input.get()
    platform = platform_input.get()

    if(platform == "PC (Steam/Origin)"):
        platform = "PC"
    else:
        platform = "Console"

    recordGame(username, platform, auth)

title_banner = Label(main, 
                        text = "Apex rank tracker", 
                        font=("Helvetica", 18)
                        ).place(x = 60, y = 10) 
                
auth_label = Label(main, 
                    text = "Auth key      : ", 
                    font=("Helvetica",14)
                    ).place(x = 20, y = 60)       

username_label = Label(main, 
                        text = "Username   : ", 
                        font=("Helvetica",14)
                        ).place(x = 20, y = 90)        

platform_label = Label(main, 
                        text = "Platform      : ", 
                        font=("Helvetica",14)
                        ).place(x = 20, y = 120)     

username_input_area = Entry(main, 
                            textvariable=username_input,
                            width=20
                            ).place(x=150, y=97)

auth_input_area = Entry(main, 
                        textvariable=auth_input,
                        show='*',
                        width=20
                        ).place(x=150, y=67)

options = ["PC (Steam/Origin)", "Console (PS/Xbox)"]

platform_input.set(options[0])

w = OptionMenu(main, platform_input, *options)
w.pack()     
w.place(x = 145, y = 120)     


addProfile_button = Button(main, 
                           text = "   Add Profile   ", 
                           command=lambda: addProfile_Clicked()
                          ).place(x = 40, y = 180)

compareProfile_button = Button(main, 
                               text = "  Session Status  ", 
                               command=lambda: compareProfile_Clicked()
                              ).place(x = 170, y = 180)

updateProfile_button = Button(main, 
                              text = "  New Session  ", 
                              command=lambda: updateProfile_Clicked()
                             ).place(x = 40, y = 220)

deleteProfile_button = Button(main, 
                              text = "   Delete Profile  ", 
                              command=lambda: deleteProfile_Clicked()
                             ).place(x = 170, y = 220)

recordGame_button = Button(main, 
                              text = "                        Record Game                        ", 
                              command=lambda: recordGame_Clicked()
                             ).place(x = 40, y = 260)

main.mainloop()

