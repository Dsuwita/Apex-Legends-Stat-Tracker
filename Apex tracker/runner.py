from Apexrank import *
from tkinter import *

main = Tk()  
main.geometry("300x280") 
main.resizable(False,False)
main.title("Apex rank tracker")

username_input = StringVar()
platform_input = StringVar()

def addProfile_Clicked():
    username = username_input.get()
    platform = platform_input.get()

    if(platform == "PC (Steam/Origin)"):
        platform = "PC"
    else:
        platform = "Console"

    if(username != "" and platform != ""):
        addProfile(username,platform)

def compareProfile_Clicked():
    username = username_input.get()
    platform = platform_input.get()

    if(platform == "PC (Steam/Origin)"):
        platform = "PC"
    else:
        platform = "Console"

    if( username != "" and platform != ""):
        compareProfile(username,platform)

def updateProfile_Clicked():
    username = username_input.get()
    platform = platform_input.get()

    if(platform == "PC (Steam/Origin)"):
        platform = "PC"
    else:
        platform = "Console"

    if(username != "" and platform != ""):
        updateProfile(username,platform)

def deleteProfile_Clicked():
    username = username_input.get()
    platform = platform_input.get()

    if(username != ""):
        deleteProfile(username)

def recordGame_Clicked():
    username = username_input.get()
    platform = platform_input.get()

    if(platform == "PC (Steam/Origin)"):
        platform = "PC"
    else:
        platform = "Console"

    recordGame(username, platform)

title_banner = Label(main, 
                        text = "Apex rank tracker", 
                        font=("Helvetica", 18)
                        ).place(x = 60, y = 10) 
                   

username_label = Label(main, 
                        text = "Username   : ", 
                        font=("Helvetica",14)
                        ).place(x = 20, y = 60)        

platform_label = Label(main, 
                        text = "Platform      : ", 
                        font=("Helvetica",14)
                        ).place(x = 20, y = 100)     

username_input_area = Entry(main, 
                            textvariable=username_input,
                            width=20
                            ).place(x=150, y=67)


options = ["PC (Steam/Origin)", "Console (PS/Xbox)"]

platform_input.set(options[0])

w = OptionMenu(main, platform_input, *options)
w.pack()     
w.place(x = 145, y = 100)     


addProfile_button = Button(main, 
                           text = "   Add Profile   ", 
                           command=lambda: addProfile_Clicked()
                          ).place(x = 40, y = 160)

compareProfile_button = Button(main, 
                               text = "  Session Status  ", 
                               command=lambda: compareProfile_Clicked()
                              ).place(x = 170, y = 160)

updateProfile_button = Button(main, 
                              text = "  New Session  ", 
                              command=lambda: updateProfile_Clicked()
                             ).place(x = 40, y = 200)

deleteProfile_button = Button(main, 
                              text = "   Delete Profile  ", 
                              command=lambda: deleteProfile_Clicked()
                             ).place(x = 170, y = 200)

recordGame_button = Button(main, 
                              text = "                        Record Game                        ", 
                              command=lambda: recordGame_Clicked()
                             ).place(x = 40, y = 240)

main.mainloop()

