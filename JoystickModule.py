import pygame
from time import sleep

#init pygame class
pygame.init()
#make a new controller object
controller = pygame.joystick.Joystick(0)
#initialize the controller
controller.init()
#make a dictionary for the buttons
buttons = {'x':0,'o':0,'t':0,'s':0,
           'L1':0,'R1':0,'L2':0,'R2':0,
           'share':0,'options':0,
           'axis1':0.,'axis2':0.,'axis3':0.,'axis4':0.}
#make a matrix for the 6 aksis
axiss=[0.,0.,0.,0.,0.,0.]


#create a function to get inputs from joystick
#name is if you want to choose spesific buttons
def getJS(name=''):
    global buttons
    #retrieve any events
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:      #analog sticks
            axiss[event.axis] = round(event.value,2)
        elif event.type == pygame.JOYBUTTONDOWN:
            for x, (key,value) in enumerate(buttons.items()):
                if x <10:
                    if controller.get_button(x): buttons[key] = 1
        elif event.type == pygame.JOYBUTTONDOWN:
            for x, (key,value)  in enumerate(buttons.items()):
                if x<10:
                    if event.button ==x[key] = 0

