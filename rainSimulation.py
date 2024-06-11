import customtkinter
import random
import math
import threading
import pygame
import os
import time



customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

#play a single rain sound on a random interval
def rainSoundplay_light():
    while switchRain_var.get() == "on":
        pygame.mixer.Channel(1).play(raindrop_light)
        time.sleep(random.random()*0.5)
    else:
        pygame.mixer.stop()
        return

def rainSoundplay_light2():
    while switchRain_var.get() == "on":
        pygame.mixer.Channel(2).play(raindrop_light)
        time.sleep(random.random()*0.5)
    else:
        pygame.mixer.stop()
        return


individual_drop = threading.Thread(target=rainSoundplay_light,)
individual_drop2 = threading.Thread(target=rainSoundplay_light2,)

#Function to play the rain noise
def rainSound():
    if switchRain_var.get() == "on":
        individual_drop.start()
        individual_drop2.start()
    else:
        individual_drop.join()
        individual_drop2.join()


#Function to exit program
def exit_program():
    exit()

app = customtkinter.CTk()
app.title('sleep sounds')
app.geometry("1920x1280")

#initialize switch in off position, declare var to track switch position
pygame.init()
pygame.mixer.init()
rain_bkgd = pygame.mixer.Sound('ForestRain_S08AM.37.wav')
raindrop_light = pygame.mixer.Sound('drip.mp3')
switchRain_var = customtkinter.StringVar(value="off")

#Frame of app
frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill='both', expand=True)

#Label inside the frame
label = customtkinter.CTkLabel(master=frame, text='Main Menu')
label.pack(pady=12, padx=10)

#Switch that will turn rain on and off
switchRain = customtkinter.CTkSwitch(master=frame, text="Rain", command=rainSound,
                                 variable=switchRain_var, onvalue="on", offvalue="off")
switchRain.pack(pady=40)

#Button to exit the program
button = customtkinter.CTkButton(master=frame, text='Exit', command=exit_program)
button.pack(pady=12, padx=10)

#Checkbox for no reason
checkbox = customtkinter.CTkCheckBox(master=frame, text='Pay no mind to this checkbox')
checkbox.pack(pady=12, padx=10)

#customtkinter function to make the GUI
app.mainloop()
